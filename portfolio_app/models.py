from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100, default="Sachin Lad")
    title = models.CharField(max_length=150, default="Full-Stack & Python Developer")
    tagline = models.CharField(max_length=255, default="Building scalable web applications with Python & Django.")
    bio = models.TextField(default="Seeking opportunities in the IT industry where I can apply technical skills, problem-solving abilities, and passion for technology while contributing to organizational growth.")
    degree_badge = models.CharField(max_length=50, default="MCA")
    email = models.EmailField(default="slad20401@gmail.com")
    phone = models.CharField(max_length=20, default="+91 7487095241")
    whatsapp = models.CharField(max_length=20, default="917487095241")
    address = models.CharField(max_length=255, default="B-203 Nandanvan, Society Motera Road, Sabarmati, Ahmedabad - 380005")
    linkedin_url = models.URLField(default="https://www.linkedin.com/in/sachin-lad-a75a61")
    github_url = models.URLField(default="https://github.com/SachinLad")
    profile_image = models.ImageField(upload_to="profile/", null=True, blank=True)
    resume_file = models.FileField(upload_to="resume/", null=True, blank=True)
    status_text = models.CharField(max_length=100, default="Available for Opportunities")

    @property
    def google_maps_url(self):
        query = self.address.replace(' ', '+').replace(',', '%2C')
        return f"https://www.google.com/maps/search/?api=1&query={query}"

    @property
    def google_maps_embed_url(self):
        query = self.address.replace(' ', '+').replace(',', '%2C')
        return f"https://maps.google.com/maps?q={query}&t=&z=15&ie=UTF8&iwloc=&output=embed"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Profile Information"
        verbose_name_plural = "Profile Information"


class Education(models.Model):
    DEGREE_CHOICES = [
        ('mca', 'MCA'),
        ('bca', 'BCA'),
        ('12th', '12th Standard'),
        ('10th', '10th Standard'),
        ('cert', 'Certification'),
    ]
    degree = models.CharField(max_length=150)
    category = models.CharField(max_length=20, choices=DEGREE_CHOICES, default='mca')
    institution = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    score_label = models.CharField(max_length=50, default="CGPA / Percentage")
    score_value = models.CharField(max_length=50)
    curriculum = models.TextField(help_text="Separate points with semicolons (;)", default="Core Software Engineering; Database Architecture; Web Technologies")
    order = models.PositiveIntegerField(default=1)

    def get_curriculum_list(self):
        return [item.strip() for item in self.curriculum.split(';') if item.strip()]

    def __str__(self):
        return f"{self.degree} - {self.institution}"

    class Meta:
        ordering = ['order']
        verbose_name = "Education Record"
        verbose_name_plural = "Education Records"


class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    icon_name = models.CharField(max_length=50, default="code", help_text="e.g. code, database, tool, brain, server")
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
        verbose_name = "Skill Category"
        verbose_name_plural = "Skill Categories"


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, related_name="skills", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    badge_color = models.CharField(max_length=30, default="cyan", help_text="e.g. red, cyan, emerald, amber, purple")

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class Project(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=150, default="Python, Django, HTML, CSS, JavaScript")
    tag = models.CharField(max_length=100, default="Django & SQLite")
    date_label = models.CharField(max_length=50, default="Jan 2024")
    description = models.TextField()
    features = models.TextField(help_text="Separate points with semicolons (;)", default="Secure login for admin and user; Manage schedules; Send updates and notifications")
    tech_stack = models.CharField(max_length=255, default="Python, Django, HTML5, CSS3, JavaScript, SQLite")
    image = models.ImageField(upload_to="projects/", null=True, blank=True)
    live_url = models.URLField(blank=True, null=True, help_text="Live project preview URL")
    github_url = models.URLField(blank=True, null=True, help_text="GitHub repository URL")
    is_featured = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=1)

    def get_features_list(self):
        return [f.strip() for f in self.features.split(';') if f.strip()]

    def get_tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name = "Project"
        verbose_name_plural = "Projects"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} - {self.email} ({self.created_at.strftime('%d-%b-%Y')})"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
