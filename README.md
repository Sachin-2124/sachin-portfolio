<div align="center">

# 🕷️ Sachin Lad — Full-Stack & Python Developer Portfolio

<p align="center">
  <img src="static/images/sachin_profile.jpg" alt="Sachin Lad" width="160" height="160" style="border-radius: 50%; border: 3px solid #ef4444; object-fit: cover; object-position: center 20%; box-shadow: 0 0 25px rgba(239, 68, 68, 0.6);" />
</p>

### **Sachin Lad** | MCA Graduate • Python & Django Specialist
*Building scalable web applications, relational database architectures, and futuristic cyber-themed user experiences.*

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.1-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)

[![Education](https://img.shields.io/badge/Degree-MCA%20(GLS%20University)-8b5cf6?style=flat-square)](https://glsuniversity.ac.in/)
[![Location](https://img.shields.io/badge/Location-Ahmedabad%2C%20Gujarat-ef4444?style=flat-square)](https://maps.app.goo.gl/wSg2aD7qZpU6)
[![Status](https://img.shields.io/badge/Status-Available%20for%20Opportunities-10b981?style=flat-square)](#-connect-with-me)

---

[🚀 Explore Live Demos](#-featured-projects--live-demos) • [🛠️ Features](#-core-features--technologies) • [⚡ Installation](#-installation--quick-start) • [🛡️ Admin Dashboard](#-custom-admin-dashboard--panel) • [📫 Connect](#-connect-with-me)

</div>

---

## 🌟 Overview

This repository contains the complete source code for **Sachin Lad's Interactive Developer Portfolio**. Built with a robust **Django & SQLite3** backend and a custom high-performance **HTML5, CSS3 & JavaScript** frontend with cyber-hero aesthetics, 3D particle physics, real-time Web Audio synthesizer, and live interactive project demos.

---

## 🛠️ Core Features & Technologies

### 🎨 Frontend Experience:
- ⚡ **Cyber Core Loader**: Sleek loading screen with laser scanner, percentage counter, and status check.
- 🕷️ **3D Spider-Web Particle Canvas**: Interactive particle web in HTML5 Canvas reacting in real time to mouse physics.
- 🕸️ **"THWIP!" Click Shooting Effect**: Shoots web threads from screen origins toward any clicked point.
- 🪐 **Smooth 3D Orbiting Badges**: Revolving upright contact badges (WhatsApp, LinkedIn, Phone, GitHub) with hover-pause.
- 🎵 **Spider-Man Theme Web Audio Synthesizer**: Native Web Audio API synthesizing brass leads, walking bass, and drums without heavy MP3 files.
- 📍 **Embedded Google Maps GPS Pin**: Real-time live navigation to Ahmedabad location.
- 📱 **100% Fully Responsive**: Pixel-perfect across Android, iOS Safari, iPads, and Desktop screens.

### ⚙️ Backend & Architecture:
- 🐍 **Django 6.1 Architecture**: Modular structure with MVT (Model-View-Template) pattern.
- 🗄️ **SQLite3 Relational Database**: Structured schemas for Profile, Projects, Education, Skill Categories, and Contact Messages.
- 🛡️ **Custom Dark Admin Portal (`/panel/`)**: Full CRUD dashboard to manage projects, edit profile info, read inquiries, and reset credentials.
- 📩 **AJAX Asynchronous Contact Pipeline**: Real-time message storage with live status feedback.

---

## 💼 Featured Projects & Live Demos

| Project Name | Tech Stack | Live Demo & Source |
| :--- | :--- | :--- |
| **🌍 Tour and Travels Management System** | Python, Django, SQLite, Bootstrap, JS | [🔗 Interactive Demo](http://127.0.0.1:8000/demo/tour/) • [📦 GitHub Repo](https://github.com/Sachin-2124/tour-and-travels-management-system) |
| **📄 SmartResume (AI & ATS Builder)** | Python, Django, AI Prompts, PDF Kit, SQLite | [🔗 Interactive Demo](http://127.0.0.1:8000/demo/smartresume/) • [📦 GitHub Repo](https://github.com/Sachin-2124/SmartResume) |
| **🏟️ Stadium Management System** | Python, Django, SQLite, Seat Engine | [🔗 Interactive Demo](http://127.0.0.1:8000/demo/stadium/) |
| **🏠 PG (Paying Guest) Management System** | Python, Django, SQLite, Room Booking | [🔗 Interactive Demo](http://127.0.0.1:8000/demo/pg/) |

---

## 📁 Repository Structure

```text
sachin_portfolio/
├── manage.py                     # Django CLI utility
├── db.sqlite3                    # Relational database
├── sachin_portfolio/             # Project configuration
│   ├── settings.py               # Settings & static/media configs
│   ├── urls.py                   # Master URL routing
│   └── wsgi.py                   # WSGI server entry point
├── portfolio_app/                # Main portfolio application
│   ├── models.py                 # Profile, Project, Education, Message models
│   ├── views.py                  # Public, Demo & Admin views
│   ├── urls.py                   # Application routes
│   ├── forms.py                  # Django Forms for CRUD operations
│   └── admin.py                  # Standard Django admin configuration
├── templates/                    # HTML5 templates
│   └── portfolio_app/
│       ├── index.html            # Main portfolio landing page
│       ├── demos/                # Live interactive demo views
│       └── admin/                # Custom dark admin dashboard templates
├── static/                       # Static assets
│   ├── css/style.css             # Cyber styling & animations
│   ├── js/main.js                # Particles, THWIP, Orbit & Audio Synth
│   └── images/                   # Profile & project banner images
└── media/                        # User-uploaded files & photos
```

---

## ⚡ Installation & Quick Start

Follow these simple steps to run this project locally on your machine:

### 1. Clone the repository:
```bash
git clone https://github.com/Sachin-2124/sachin-portfolio.git
cd sachin-portfolio
```

### 2. Create and activate a virtual environment (Optional but Recommended):
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Django:
```bash
pip install django pillow
```

### 4. Apply database migrations:
```bash
python manage.py migrate
```

### 5. Start the development server:
```bash
python manage.py runserver
```

### 6. Open in your browser:
- 🌐 **Public Portfolio:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- 🛡️ **Admin Portal:** [http://127.0.0.1:8000/panel/](http://127.0.0.1:8000/panel/)

---

## 🛡️ Custom Admin Dashboard (`/panel/`)

A dedicated, customized Dark-Themed Control Center is included for complete content management without needing Django's default UI:

- **Dashboard:** [http://127.0.0.1:8000/panel/](http://127.0.0.1:8000/panel/)
- **Default Username:** `admin`
- **Default Password:** `admin123`
- **Password Reset:** [http://127.0.0.1:8000/panel/forgot-password/](http://127.0.0.1:8000/panel/forgot-password/) *(Verified via Registered Email or Master Key)*

---

## 🎓 Academic Qualifications

- **Master of Computer Applications (MCA)** — GLS University, Ahmedabad (2024 - 2026) • *CPI: 7.00*
- **Bachelor of Computer Applications (BCA)** — GLS University, Ahmedabad (2021 - 2024) • *CPI: 7.74*
- **HSC (12th Standard)** — Gujarat Board (2020 - 2021) • *Percentile: 71.05%*
- **SSC (10th Standard)** — Gujarat Board (2018 - 2019) • *Percentage: 63.66%*

---

## 📫 Connect With Me

<div align="center">

[![WhatsApp](https://img.shields.io/badge/WhatsApp-Chat%20Now-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/917487095241)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Let's%20Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sachin-lad-a75a61)
[![GitHub](https://img.shields.io/badge/GitHub-Follow%20Repos-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Sachin-2124)
[![Email](https://img.shields.io/badge/Email-slad20401%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:slad20401@gmail.com)

**📱 Phone:** +91 7487095241 | **📍 Location:** Ahmedabad, Gujarat, India

</div>

---

<div align="center">
  <sub>Designed & Developed with ❤️ by <strong>Sachin Lad</strong> | Powered by Python & Django</sub>
</div>
