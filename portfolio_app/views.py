from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile, Education, SkillCategory, Skill, Project, ContactMessage
from .forms import ProfileForm, ProjectForm, EducationForm, SkillForm

# ==========================================
# Public Views
# ==========================================

def index_view(request):
    profile = Profile.objects.first()
    if not profile:
        profile = Profile.objects.create(
            name="Sachin Lad",
            title="Full-Stack & Python Developer",
            tagline="Building scalable web apps with clean architecture, Python, Django & SQLite.",
            bio="Seeking opportunities in the IT industry where I can apply technical skills, problem-solving abilities, and passion for technology while contributing to organizational growth.",
            degree_badge="MCA",
            email="slad20401@gmail.com",
            phone="+91 7487095241",
            whatsapp="917487095241",
            address="B-203 Nandanvan, Society Motera Road, Sabarmati, Ahmedabad - 380005",
            linkedin_url="https://www.linkedin.com/in/sachin-lad-a75a61",
            github_url="https://github.com/Sachin-2124",
            profile_image="profile/sachin_profile.jpg",
            status_text="Available for Opportunities"
        )
    elif profile.title != "Full-Stack & Python Developer":
        profile.title = "Full-Stack & Python Developer"
        profile.save(update_fields=['title'])
    
    education_records = Education.objects.all().order_by('order')
    skill_categories = SkillCategory.objects.prefetch_related('skills').all().order_by('order')
    projects = list(Project.objects.filter(is_featured=True).order_by('order'))

    demo_map = {
        'Tour and Travels Management System': '/demo/tour/',
        'SmartResume — AI & Dynamic Resume Builder': '/demo/smartresume/',
        'Stadium Management System': '/demo/stadium/',
        'PG Management System': '/demo/pg/',
    }

    for p in projects:
        if not p.live_url or p.live_url == '#':
            for title_key, url in demo_map.items():
                if title_key.lower() in p.title.lower() or p.title.lower() in title_key.lower():
                    p.live_url = url
                    p.save(update_fields=['live_url'])
                    break

    context = {
        'profile': profile,
        'education_records': education_records,
        'skill_categories': skill_categories,
        'projects': projects,
    }
    return render(request, 'portfolio_app/index.html', context)


@require_POST
def contact_submit(request):
    name = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip()
    subject = request.POST.get('subject', '').strip()
    message = request.POST.get('message', '').strip()

    if not name or not email or not message:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'error', 'message': 'Please fill out all required fields.'}, status=400)
        messages.error(request, 'Please fill out all required fields.')
        return redirect('index')

    ContactMessage.objects.create(
        name=name,
        email=email,
        subject=subject or 'Portfolio Inquiry',
        message=message
    )

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'status': 'success',
            'message': f'Thank you {name}! Your message has been received successfully.'
        })

    messages.success(request, f'Thank you {name}! Your message has been received successfully.')
    return redirect('index')


# ==========================================
# Live Interactive Project Demos
# ==========================================

def demo_tour(request):
    """Live interactive preview of Tour & Travels Management System"""
    return render(request, 'portfolio_app/demos/tour_demo.html')

def demo_smartresume(request):
    """Live interactive preview of SmartResume AI & ATS Builder"""
    return render(request, 'portfolio_app/demos/smartresume_demo.html')

def demo_stadium(request):
    """Live interactive preview of Stadium Management System"""
    return render(request, 'portfolio_app/demos/stadium_demo.html')

def demo_pg(request):
    """Live interactive preview of PG Management System"""
    return render(request, 'portfolio_app/demos/pg_demo.html')


# ==========================================
# Custom Admin Panel Authentication & Views
# ==========================================

def admin_login_view(request):
    # Ensure default superuser exists
    if not User.objects.filter(is_superuser=True).exists():
        User.objects.create_superuser(username='admin', email='slad20401@gmail.com', password='admin123')

    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin_dashboard')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid admin username or password.')

    return render(request, 'portfolio_app/admin/login.html')


def admin_forgot_password_view(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin_dashboard')

    if request.method == 'POST':
        identifier = request.POST.get('identifier', '').strip()
        new_password = request.POST.get('new_password', '').strip()

        if not new_password:
            messages.error(request, 'Please provide a valid new password.')
            return render(request, 'portfolio_app/admin/forgot_password.html')

        # Allowed: User's registered email or secret recovery key
        valid_keys = ['slad20401@gmail.com', 'sachin2026', 'slad2026']
        cleaned_id = identifier.replace(" ", "").lower()
        is_valid = any(k.lower() == cleaned_id for k in valid_keys)

        if is_valid:
            user = User.objects.filter(is_superuser=True).first()
            if not user:
                user = User.objects.filter(username='admin').first()
            if not user:
                user = User.objects.create_superuser(username='admin', email='slad20401@gmail.com', password=new_password)
            else:
                user.set_password(new_password)
                user.save()

            messages.success(request, f'Password successfully updated for "{user.username}"! You can now log in.')
            return redirect('admin_login')
        else:
            messages.error(request, 'Verification failed. Please enter your registered Email or Secret Recovery Key.')

    return render(request, 'portfolio_app/admin/forgot_password.html')


def admin_logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('admin_login')


@login_required(login_url='admin_login')
def admin_dashboard(request):
    total_projects = Project.objects.count()
    total_messages = ContactMessage.objects.count()
    unread_messages = ContactMessage.objects.filter(is_read=False).count()
    total_skills = Skill.objects.count()

    recent_messages = ContactMessage.objects.all().order_by('-created_at')[:5]
    projects = Project.objects.all().order_by('order')[:4]
    profile = Profile.objects.first()

    context = {
        'total_projects': total_projects,
        'total_messages': total_messages,
        'unread_messages': unread_messages,
        'total_skills': total_skills,
        'recent_messages': recent_messages,
        'projects': projects,
        'profile': profile,
        'active_page': 'dashboard',
    }
    return render(request, 'portfolio_app/admin/dashboard.html', context)


# --- Projects CRUD ---
@login_required(login_url='admin_login')
def admin_projects_list(request):
    projects = Project.objects.all().order_by('order')
    return render(request, 'portfolio_app/admin/projects.html', {
        'projects': projects,
        'active_page': 'projects',
    })


@login_required(login_url='admin_login')
def admin_project_add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            messages.success(request, f'Project "{project.title}" created successfully!')
            return redirect('admin_projects')
    else:
        form = ProjectForm()

    return render(request, 'portfolio_app/admin/project_form.html', {
        'form': form,
        'title': 'Add New Project',
        'active_page': 'projects',
    })


@login_required(login_url='admin_login')
def admin_project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, f'Project "{project.title}" updated successfully!')
            return redirect('admin_projects')
    else:
        form = ProjectForm(instance=project)

    return render(request, 'portfolio_app/admin/project_form.html', {
        'form': form,
        'project': project,
        'title': f'Edit Project: {project.title}',
        'active_page': 'projects',
    })


@login_required(login_url='admin_login')
def admin_project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        title = project.title
        project.delete()
        messages.success(request, f'Project "{title}" deleted successfully.')
    return redirect('admin_projects')


# --- Contact Messages ---
@login_required(login_url='admin_login')
def admin_messages_list(request):
    contact_messages = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'portfolio_app/admin/messages.html', {
        'contact_messages': contact_messages,
        'active_page': 'messages',
    })


@login_required(login_url='admin_login')
def admin_message_toggle_read(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)
    msg.is_read = not msg.is_read
    msg.save()
    status_str = "read" if msg.is_read else "unread"
    messages.info(request, f'Message from {msg.name} marked as {status_str}.')
    return redirect('admin_messages')


@login_required(login_url='admin_login')
def admin_message_delete(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)
    if request.method == 'POST':
        msg.delete()
        messages.success(request, 'Message deleted successfully.')
    return redirect('admin_messages')


# --- Profile Edit ---
@login_required(login_url='admin_login')
def admin_profile_edit(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile details and photos updated successfully!')
            return redirect('admin_profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'portfolio_app/admin/profile.html', {
        'form': form,
        'profile': profile,
        'active_page': 'profile',
    })


# --- Education CRUD ---
@login_required(login_url='admin_login')
def admin_education_list(request):
    educations = Education.objects.all().order_by('order')
    return render(request, 'portfolio_app/admin/education.html', {
        'educations': educations,
        'active_page': 'education',
    })


@login_required(login_url='admin_login')
def admin_education_add(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Education record added!')
            return redirect('admin_education')
    else:
        form = EducationForm()

    return render(request, 'portfolio_app/admin/education_form.html', {
        'form': form,
        'title': 'Add Education Record',
        'active_page': 'education',
    })


@login_required(login_url='admin_login')
def admin_education_edit(request, pk):
    edu = get_object_or_404(Education, pk=pk)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=edu)
        if form.is_valid():
            form.save()
            messages.success(request, f'{edu.degree} record updated!')
            return redirect('admin_education')
    else:
        form = EducationForm(instance=edu)

    return render(request, 'portfolio_app/admin/education_form.html', {
        'form': form,
        'edu': edu,
        'title': f'Edit Education: {edu.degree}',
        'active_page': 'education',
    })


@login_required(login_url='admin_login')
def admin_education_delete(request, pk):
    edu = get_object_or_404(Education, pk=pk)
    if request.method == 'POST':
        edu.delete()
        messages.success(request, 'Education record deleted.')
    return redirect('admin_education')


# --- Skills Management ---
@login_required(login_url='admin_login')
def admin_skills_list(request):
    categories = SkillCategory.objects.prefetch_related('skills').all().order_by('order')
    form = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save()
            messages.success(request, f'Skill "{skill.name}" added!')
            return redirect('admin_skills')

    return render(request, 'portfolio_app/admin/skills.html', {
        'categories': categories,
        'form': form,
        'active_page': 'skills',
    })


@login_required(login_url='admin_login')
def admin_skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill deleted successfully.')
    return redirect('admin_skills')
