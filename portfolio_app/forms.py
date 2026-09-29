from django import forms
from .models import Profile, Project, Education, Skill, SkillCategory

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name', 'title', 'tagline', 'bio', 'degree_badge',
            'email', 'phone', 'whatsapp', 'address',
            'linkedin_url', 'github_url', 'profile_image', 'resume_file', 'status_text'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tagline': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'degree_badge': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control'}),
            'github_url': forms.URLInput(attrs={'class': 'form-control'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
            'resume_file': forms.FileInput(attrs={'class': 'form-control'}),
            'status_text': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'title', 'subtitle', 'tag', 'date_label',
            'description', 'features', 'tech_stack',
            'image', 'github_url', 'live_url', 'is_featured', 'order'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Travel Booking Engine'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Python, Django, SQLite, JavaScript'}),
            'tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full-Stack Web App'}),
            'date_label': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Featured / Jan 2024'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'features': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Feature 1; Feature 2; Feature 3'}),
            'tech_stack': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Python, Django, SQLite, HTML5, CSS3, JS'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'github_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://github.com/...'}),
            'live_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'category', 'institution', 'duration', 'score_label', 'score_value', 'curriculum', 'order']
        widgets = {
            'degree': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'institution': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
            'score_label': forms.TextInput(attrs={'class': 'form-control'}),
            'score_value': forms.TextInput(attrs={'class': 'form-control'}),
            'curriculum': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Topic 1; Topic 2; Topic 3'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['category', 'name', 'badge_color']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Django REST Framework'}),
            'badge_color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'emerald / sky / rose / amber'}),
        }
