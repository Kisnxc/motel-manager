from django.shortcuts import render,redirect,get_object_or_404
from .forms import TenantForm
from .models import Tenant
from django.contrib.auth.decorators import login_required
from room.models import Room

@login_required
def tenant_list(request):
    tenants = Tenant.objects.filter(room__owner=request.user)
    return render(request,'tenant/tenant_list.html', {'tenants' : tenants})

@login_required
def tenant_create(request):
    if request.method == 'POST':
        form = TenantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tenant_list')
    else:
        form = TenantForm()
    
    form.fields['room'].queryset = Room.objects.filter(owner = request.user)
    return render(request,'tenant/tenant_form.html', {'form' : form})

@login_required
def tenant_create_for_room(request, room_id):
    room = get_object_or_404(Room, id=room_id, owner=request.user)
    if request.method == 'POST':
        form = TenantForm(request.POST)
        if form.is_valid():
            tenant = form.save(commit=False)
            tenant.room = room
            tenant.save()
            return redirect('room_detail', room_id)
    else:
        form = TenantForm()
    return render(request, 'tenant/tenant_form.html', {'form': form, 'room': room})
