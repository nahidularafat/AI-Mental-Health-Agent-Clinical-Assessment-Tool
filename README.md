# 🧠 AI Mental Health Agent & Clinical Assessment Tool

A comprehensive, AI-driven mental health support platform built with **Django**. This project integrates a conversational AI agent (using LangGraph and Gemini) with a highly accurate PyTorch Neural Network to provide empathetic support, clinical stress prediction, and automated therapist recommendations.

📖 **[Download User Manual (PDF)](https://github.com/user-attachments/files/29550665/User_Manual_Stress_Level_App.pdf)**

---

## 📸 Project Screenshots

<details>
  <summary><b>👉 Click here to view application screenshots</b></summary>
  <br>
  <img width="100%" alt="Screenshot 1" src="https://github.com/user-attachments/assets/000f5cf8-8081-4483-a27e-112560bf351f" />
  <br><br>
  <img width="100%" alt="Screenshot 2" src="https://github.com/user-attachments/assets/ac86c005-bba2-49ac-bf3b-78b80bef4f21" />
  <br><br>
  <img width="100%" alt="Screenshot 3" src="https://github.com/user-attachments/assets/29c7cc5d-c1e5-45dc-a7bb-a81e14e1267a" />
  <br><br>
  <img width="100%" alt="Screenshot 4" src="https://github.com/user-attachments/assets/9fce6730-28a1-4630-ad6a-432f48b24cd9" />
  <br><br>
  <img width="100%" alt="Screenshot 5" src="https://github.com/user-attachments/assets/a8cde961-eed0-40d2-abf0-e9bcab0391c8" />
</details>

---

## ✨ Key Features

* **💬 Intelligent ReAct Agent:** An empathetic conversational agent powered by LangGraph and Gemini 2.5 Flash that listens, supports, and intelligently triggers specific tools based on user context.
* **📊 Clinical Stress Assessment (Explainable AI):** A custom-trained PyTorch Neural Network (`MediumNN`) that predicts user stress levels (Low, Moderate, Critical) with **92.12% accuracy** based on 20 distinct psychological and environmental metrics.
* **👨‍⚕️ Dynamic Therapist Recommendation:** Automatically fetches and recommends nearby specialized psychiatrists from a custom database (`doctor_list.csv`) when moderate or high stress is detected.
* **🚨 Emergency Crisis Intervention:** Integrates with Twilio API to automatically trigger emergency safety phone calls if suicidal ideation or self-harm intent is detected.
* **📈 Mood Tracking Dashboard:** Visualizes the user's emotional state over time using interactive charts.
* **🩺 Therapist Portal:** A dedicated dashboard for professionals to monitor patient progress and trigger proactive SMS check-ins.

## 🛠️ Technology Stack

* **Backend Framework:** Django, Python
* **Machine Learning:** PyTorch, Scikit-learn, Pandas, NumPy
* **AI/LLM:** LangChain, LangGraph, Google Gemini API, Ollama (MedGemma)
* **External APIs:** Twilio (SMS & Voice Calls)
* **Frontend:** HTML, Tailwind CSS, JavaScript





## 📂 Project Structure

```text
├── chat/
│   ├── ai_agent.py        # LangGraph ReAct Agent setup and tool definitions
│   ├── tools.py           # Custom tools (MedGemma, Twilio Emergency)
│   ├── models.py          # Database models (ChatSession, Message, Resources)
│   ├── views.py           # Core logic, ML inference, and routing
│   └── templates/         # Tailwind-styled HTML templates
├── champion_model.pth     # Trained PyTorch Neural Network (92.12% Accuracy)
├── framework_scaler.pkl   # StandardScaler for input normalization
├── doctor_list.csv        # Custom dataset for therapist recommendations
├── manage.py              # Django project manager
└── requirements.txt       # Python dependencies  ""
