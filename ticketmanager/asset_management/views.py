from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Asset, AssetCategory
from .forms import AssetForm, AssetCategoryForm, CustomUserChangeForm, AssetUpdateForm
from django.contrib.auth.models import Permission
from django.contrib import messages

# Handles user registration.
# Allows new users to register by creating a new account.
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

# Handles user login.
# Allows registered users to log in to the application.
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
        else:
            # Authentication failed, show error messages
            if 'username' in form.errors:
                messages.error(request, 'Username field is required.')
            elif 'password' in form.errors:
                messages.error(request, 'Password field is required.')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})

# Displays a list of assets.
# Requires the user to have the 'can_view_asset' permission.
@permission_required('asset_management.can_view_asset')
def asset_list(request):
    assets = Asset.objects.all()
    return render(request, 'asset_list.html', {'assets': assets})

# Handles the addition of new assets.
# Requires the user to have the 'can_add_asset' permission.
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
                messages.success(request, 'Asset added successfully!')
                return redirect('asset_list')
    else:
        form = AssetForm()

    return render(request, 'add_asset.html', {'form': form, 'categories': categories})

# Handles updating an existing asset.
# Requires the user to have the 'can_change_asset' permission.
@permission_required('asset_management.can_change_asset')
def update_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    if request.method == 'POST':
        form = AssetUpdateForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Asset updated successfully!')
            return redirect('asset_list')
    else:
        form = AssetUpdateForm(instance=asset)
    return render(request, 'update_asset.html', {'form': form})

# Handles deleting an existing asset.
# Requires the user to have the 'can_delete_asset' permission.
@permission_required('asset_management.can_delete_asset')
def delete_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    if request.method == 'POST':
        asset.delete()
        messages.success(request, 'Asset deleted successfully!')
        return redirect('asset_list')
    return render(request, 'delete_asset.html', {'asset': asset})

# Displays the user's home page.
def home(request):
    return render(request, 'home.html')

# Displays and handles the user's profile.
# Allows users to view and update their profiles.
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