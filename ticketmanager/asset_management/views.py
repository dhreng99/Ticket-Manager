from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Asset, AssetCategory
from .forms import AssetForm, AssetCategoryForm, CustomUserChangeForm
from django.contrib.auth.models import Permission

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.user_permissions.add(
                Permission.objects.get(codename='can_view_asset'),
                Permission.objects.get(codename='can_add_asset'),
                Permission.objects.get(codename='can_change_asset')
            )
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@permission_required('asset_management.can_view_asset')
def asset_list(request):
    assets = Asset.objects.all()
    return render(request, 'asset_list.html', {'assets': assets})

@permission_required('asset_management.can_add_asset')
def add_asset(request):
    categories = AssetCategory.objects.all()
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            if Asset.objects.filter(name=name).exists():
                form.add_error('name', 'An asset with this name already exists.')
            else:
                form.save()
                return redirect('asset_list')
    else:
        form = AssetForm()

    return render(request, 'add_asset.html', {'form': form, 'categories': categories})

@permission_required('asset_management.can_change_asset')
def update_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    if request.method == 'POST':
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('asset_list')
    else:
        form = AssetForm(instance=asset)
    return render(request, 'update_asset.html', {'form': form})

@permission_required('asset_management.can_delete_asset')
def delete_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    if request.method == 'POST':
        asset.delete()
        return redirect('asset_list')
    return render(request, 'delete_asset.html', {'asset': asset})

def home(request):
    return render(request, 'home.html')

@login_required
def user_profile(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = CustomUserChangeForm(instance=user)

    return render(request, 'user_profile.html', {'user': user, 'form': form})