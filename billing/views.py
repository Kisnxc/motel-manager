from django.shortcuts import render,redirect,get_object_or_404
from .models import Bill,Room
from .forms import BillForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def bill_list(request):
    bills = Bill.objects.filter(room__owner = request.user)
    return render(request, 'billing/bill_list.html', {'bills':bills})

@login_required
def bill_create(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            room = form.cleaned_data['room']
            month = form.cleaned_data['month']
            if Bill.objects.filter(room = room, month__month = month.month, month__year = month.year).exists():
                form.add_error(None, f"Hóa đơn cho phòng {room} trong tháng {month.strftime('%m/%Y')} đã tồn tại.")
            else:
                form.save()
                return redirect('room_detail', room.id)
    else:
        form = BillForm()
    form.fields['room'].queryset = request.user.room_set.all()
    return render(request, 'billing/bill_form.html', {'form': form})

@login_required
def bill_create_for_room(request, room_id):
    room = get_object_or_404(Room, id=room_id, owner=request.user)
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            month = form.cleaned_data['month']
            # Check trùng
            if Bill.objects.filter(room=room, month__month=month.month, month__year=month.year).exists():
                form.add_error(None, f"Hóa đơn cho phòng {room} trong tháng {month.strftime('%m/%Y')} đã tồn tại.")
            else:
                bill = form.save(commit=False)
                bill.room = room
                bill.save()
                return redirect('room_detail', room_id)
    else:
        form = BillForm()
    return render(request, 'billing/bill_form.html', {'form': form, 'room': room})

    
        
    
