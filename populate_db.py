import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sachin_portfolio.settings')
django.setup()

from portfolio_app.models import Profile, Education, SkillCategory, Skill, Project

def populate():
    print("Seeding database with Sachin Lad's resume & GitHub details...")

    # 1. Profile
    Profile.objects.all().delete()
    profile = Profile.objects.create(
        name="Sachin Lad",
        title="Full-Stack Python & Django Developer",
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
    print(f"Created Profile: {profile.name}")

    # 2. Education
    Education.objects.all().delete()
    educations = [
        {
            "degree": "Master of Computer Applications (MCA)",
            "category": "mca",
            "institution": "GLS University, Ahmedabad",
            "duration": "Aug 2024 – Apr 2026",
            "score_label": "CGPA",
            "score_value": "7.0 / 10 (Pursuing)",
            "curriculum": "Advanced Python & Django Architecture; Database Management & Query Optimization; Software Engineering Methodologies; Enterprise Web Application Development",
            "order": 1
        },
        {
            "degree": "Bachelor of Computer Applications (BCA)",
            "category": "bca",
            "institution": "Navgujarat College of Computer Applications",
            "duration": "Jul 2021 – Apr 2024",
            "score_label": "CGPA",
            "score_value": "6.9 / 10 (First Class)",
            "curriculum": "Object Oriented Programming in Java & C; Database Management Systems (SQL, Oracle); Web Technologies (HTML, CSS, JavaScript); Data Structures & Algorithms",
            "order": 2
        },
        {
            "degree": "Higher Secondary Certificate (12th Standard)",
            "category": "12th",
            "institution": "H.H Patel High School",
            "duration": "Jun 2020 – Apr 2021",
            "score_label": "Percentage",
            "score_value": "70%",
            "curriculum": "Higher Secondary Education; Mathematics & Computer Fundamentals; Academic Excellence",
            "order": 3
        },
        {
            "degree": "Secondary School Certificate (10th Standard)",
            "category": "10th",
            "institution": "H.H Patel High School",
            "duration": "Jun 2018 – Apr 2019",
            "score_label": "Percentage",
            "score_value": "60%",
            "curriculum": "General Secondary School Curriculum; Science, Mathematics & Information Technology basics",
            "order": 4
        },
    ]
    for edu in educations:
        e = Education.objects.create(**edu)
        print(f"Created Education: {e.degree}")

    # 3. Skills Categories & Skills
    SkillCategory.objects.all().delete()
    Skill.objects.all().delete()

    skills_data = [
        {
            "category": "Programming & Web Languages",
            "icon": "code",
            "order": 1,
            "skills": [
                ("Python", "emerald"),
                ("Django", "emerald"),
                ("Java", "amber"),
                ("C", "sky"),
                ("JavaScript (ES6+)", "amber"),
                ("HTML5", "rose"),
                ("CSS3", "sky"),
            ]
        },
        {
            "category": "Databases & Storage",
            "icon": "database",
            "order": 2,
            "skills": [
                ("SQL", "sky"),
                ("SQLite3", "emerald"),
                ("Oracle Database", "rose"),
                ("Microsoft Access", "amber"),
            ]
        },
        {
            "category": "Developer Tools & IDEs",
            "icon": "tool",
            "order": 3,
            "skills": [
                ("VS Code", "sky"),
                ("Eclipse", "purple"),
                ("Android Studio", "emerald"),
                ("Git & GitHub", "rose"),
            ]
        },
        {
            "category": "AI Tools & Modern Workflow",
            "icon": "brain",
            "order": 4,
            "skills": [
                ("Claude Code", "purple"),
                ("ChatGPT", "emerald"),
                ("Cursor AI", "sky"),
                ("AI Assisted Coding", "amber"),
            ]
        },
    ]

    for cat_data in skills_data:
        cat = SkillCategory.objects.create(
            name=cat_data["category"],
            icon_name=cat_data["icon"],
            order=cat_data["order"]
        )
        for skill_name, color in cat_data["skills"]:
            Skill.objects.create(category=cat, name=skill_name, badge_color=color)
        print(f"Created Category with skills: {cat.name}")

    # 4. Projects (Including your live GitHub projects & Live Demos!)
    Project.objects.all().delete()
    projects = [
        {
            "title": "Tour and Travels Management System",
            "subtitle": "Python, Django, SQLite, HTML5, CSS3, JavaScript",
            "tag": "Travel Booking Engine",
            "date_label": "Featured Project",
            "description": "A comprehensive web portal for managing tourism and travel agency operations. It enables users to browse holiday packages, view destination itineraries, book tour slots, and process payments. Administrators can manage travel packages, customer inquiries, bookings, and vehicle allocations through a powerful backend.",
            "features": "Interactive tour package catalog & destination guide; Secure user booking pipeline & ticket reservation; Admin control dashboard for package pricing and bookings; Automated invoice and confirmation generation; Customer feedback and inquiry portal",
            "tech_stack": "Python, Django, SQLite3, HTML5, CSS3, JavaScript, Bootstrap",
            "github_url": "https://github.com/Sachin-2124/tour-and-travels-management-system",
            "live_url": "/demo/tour/",
            "is_featured": True,
            "order": 1
        },
        {
            "title": "SmartResume — AI & Dynamic Resume Builder",
            "subtitle": "Python, Django, SQLite, HTML5, CSS3, JavaScript",
            "tag": "ATS Optimization & Career Tool",
            "date_label": "Featured Project",
            "description": "An intelligent Resume building web application designed to help job seekers create professional, ATS-optimized resumes. Users can input their academic and project credentials, select customizable modern templates, receive formatting recommendations, and generate instant downloadable resumes.",
            "features": "Dynamic multi-step resume builder with real-time preview; Pre-formatted ATS-friendly styling and typography; User profile saving & multiple resume version management; Instant PDF formatting and export functionality; Clean, responsive UI with modern design standards",
            "tech_stack": "Python, Django, SQLite3, HTML5, CSS3, JavaScript, PDF Engine",
            "github_url": "https://github.com/Sachin-2124/SmartResume",
            "live_url": "/demo/smartresume/",
            "is_featured": True,
            "order": 2
        },
        {
            "title": "Stadium Management System",
            "subtitle": "Python, Django, HTML, CSS, JavaScript, SQLite",
            "tag": "Sports Venue & Ticketing Operations",
            "date_label": "Jan 2024",
            "description": "A comprehensive software system designed to efficiently manage all aspects of stadium operations. Includes Event Scheduling Management for organizing matches, Ticketing & Access authentication, Customer Relationship Management (CRM) for fan engagement, and Staff Security coordination.",
            "features": "Secure multi-role login for Admin and Users; Match and event schedule manager with calendar planning; Real-time ticket booking and confirmation system; Fan engagement CRM & feedback tracking; Staff and security duty allocation module",
            "tech_stack": "Python, Django, SQLite3, HTML5, CSS3, JavaScript, Bootstrap",
            "github_url": "https://github.com/Sachin-2124",
            "live_url": "/demo/stadium/",
            "is_featured": True,
            "order": 3
        },
        {
            "title": "PG Management System",
            "subtitle": "Python, Django, HTML, CSS, JavaScript, SQLite",
            "tag": "Paying Guest & Tenant Portal",
            "date_label": "Feb 2026",
            "description": "A Paying Guest Accommodation web application used to manage tenant records, room occupancy, rent collections, and dispute resolution. Helps property administrators seamlessly track tenant verification details, automate room allocation, and monitor rent histories.",
            "features": "Secure authentication for Admin and Paying Tenants; Live visual room availability and bed allocation; Automated rent payment tracking & invoice history; Online complaint submission and resolution tracker; Tenant verification and documentation management",
            "tech_stack": "Python, Django, SQLite3, HTML5, CSS3, JavaScript, Responsive UI",
            "github_url": "https://github.com/Sachin-2124",
            "live_url": "/demo/pg/",
            "is_featured": True,
            "order": 4
        }
    ]

    for p_data in projects:
        p = Project.objects.create(**p_data)
        print(f"Created Project: {p.title}")

    print("Database seeding completed successfully!")

if __name__ == '__main__':
    populate()

