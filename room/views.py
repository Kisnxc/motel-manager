from django.shortcuts import render,redirect,get_object_or_404
from .models import Room
from .forms import RoomForm
from django.contrib.auth.decorators import login_required

@login_required
def room_list(request):
    rooms = Room.objects.filter(owner = request.user)
    return render(request, 'room/room_list.html', {'rooms': rooms})

@login_required
def room_create(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.owner = request.user
            room.save()
            return redirect('home')
    else:
        form = RoomForm
    rooms = Room.objects.filter(owner=request.user).order_by('room_name') # chỉ hiển thị phòng của user đăng nhập
    return render(request, 'room/room_form.html', {'form': form})
    

@login_required
def room_update(request, pk):
    room = get_object_or_404(Room, pk = pk, owner=request.user)
    form = RoomForm(request.POST or None, instance=room)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'room/room_form.html', {'form': form})

@login_required
def room_delete(request,pk):
    room = get_object_or_404(Room, pk=pk, owner=request.user)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'room/room_confirm_delete.html', {'room': room})
    
@login_required
def home_view(request):
    rooms = Room.objects.filter(owner=request.user).order_by('room_name') # chỉ hiển thị phòng của user đăng nhập
    return render(request, 'room/home.html', {'rooms': rooms})
    
@login_required
def room_detail_view(request, room_id):
    room = get_object_or_404(Room, id=room_id, owner=request.user)
    tenants = room.tenant_set.all()
    bills = room.bill_set.all().order_by('-month')  # hóa đơn mới nhất lên đầu

    return render(request, 'room/room_detail.html', {
        'room': room,
        'tenants': tenants,
        'bills': bills,
    })