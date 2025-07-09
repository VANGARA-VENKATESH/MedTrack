# MedTrack - AWS Cloud-Enabled Healthcare Management System
![MedTrack Banner](static/med_track_logo.png)
## 🚀 Project Overview

**MedTrack** is a cloud-integrated healthcare management system that allows patients to easily book appointments, access lab results, and securely communicate with doctors. Designed using **Flask** for backend and **AWS services** for deployment and security, MedTrack provides a modern, responsive web experience.

## 🌐 Live Demo :

👉 [Open File on Google Drive](https://drive.google.com/file/d/1tyDcfKP3ZWG6uDnCSghopN0xWIw0KHlM/view?usp=drivesdk)





## 🛠️ Features

### 👩‍⚕️ Patient Features:
- Register/Login securely
- Book appointments with available doctors
- View appointment history
- Access lab test results
- Submit secure complaints

### 👨‍⚕️ Doctor Features:
- View scheduled appointments
- Access patient information
- Manage schedule availability
- Use smart AI-powered booking insights

### 💻 Admin Features (Planned):
- Manage users
- Monitor system logs
- Data analytics dashboard (via AWS CloudWatch/QuickSight)

---

## 📁 Project Structure

MedTrack/
│
├── static/
│ └── style.css, images (logo, backgrounds, etc.)
├── templates/
│ ├── index.html
│ ├── homepage.html
│ ├── login.html
│ ├── register.html
│ ├── dashboard.html
│ ├── patient_dashboard.html
│ ├── doctor_dashboard.html
│ ├── book_appointment.html
│ ├── lab_results.html
│ ├── secure_complaint.html
│ ├── schedule.html
│ ├── smart_booking.html
│ ├── view_appointment.html
│ └── more...
├── app.py
├── app.log
└── .env

## ⚙️ Tech Stack

| Technology      | Description                          |
|----------------|--------------------------------------|
| **Python Flask** | Backend web framework                |
| **HTML/CSS**    | Frontend layout and styling         |
| **AWS EC2**     | Hosting the backend                  |
| **AWS SNS/DynamoDB** | Notifications & Data storage       |
| **GitHub**      | Version control & collaboration     |

## 🔐 Security Measures
- Environment variables using `.env`
- Input validations on forms
- Encrypted password handling
- Role-based access (Doctor vs Patient)
  
## 🧠 AI/ML Integrations (Future Scope)
- Smart appointment suggestions
- AI-based health risk analysis
- Chatbot for medical queries

## 🧪 Installation & Setup

1. **Clone the repo**:
   ```bash
   git clone https://github.com/your-username/MedTrack.git
   cd MedTrack
   
2. Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Install dependencies:

pip install -r requirements.txt

4.Run the app:

python app.py
