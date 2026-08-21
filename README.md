# 🧠 AI Mental Health Agent & Clinical Assessment Tool

A comprehensive, AI-driven mental health support platform built with **Django**. This project integrates a conversational AI agent (using LangGraph and Gemini) with a highly accurate PyTorch Neural Network to provide empathetic support, clinical stress prediction, and automated therapist recommendations.


## 📸 Project Screenshots



  <br>

  <table>
    <tr>
      <td>
        <img src="https://github.com/user-attachments/assets/000f5cf8-8081-4483-a27e-112560bf351f" alt="Screenshot 1" width="100%">
      </td>
      <td>
        <img src="https://github.com/user-attachments/assets/ac86c005-bba2-49ac-bf3b-78b80bef4f21" alt="Screenshot 2" width="100%">
      </td>
      <td>
        <img src="https://github.com/user-attachments/assets/29c7cc5d-c1e5-45dc-a7bb-a81e14e1267a" alt="Screenshot 3" width="100%">
      </td>
    </tr>
    <tr>
      <td>
        <img src="https://github.com/user-attachments/assets/9fce6730-28a1-4630-ad6a-432f48b24cd9" alt="Screenshot 4" width="100%">
      </td>
      <td>
        <img src="https://github.com/user-attachments/assets/a8cde961-eed0-40d2-abf0-e9bcab0391c8" alt="Screenshot 5" width="100%">
      </td>
      <td>/td>
      
    </tr>
  </table>

<table>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/ef32420d-bfae-4979-a550-482775c5ffea" alt="Screenshot 1" width="100%">
    </td>
    <td>
      <img src="https://github.com/user-attachments/assets/91132fac-6b49-49b7-926d-c3dd10615c04" alt="Screenshot 2" width="100%">
    </td>
    <td>
      <img src="https://github.com/user-attachments/assets/bd947a56-c87f-4507-99a6-ab297cb4e2db" alt="Screenshot 3" width="100%">
    </td>
  </tr>

  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/004e8587-04fc-42ed-b203-45a01412aa2c" alt="Screenshot 4" width="100%">
    </td>
    <td>
      <img src="https://github.com/user-attachments/assets/edbd128f-069e-4925-b86f-eae69d6ad273" alt="Screenshot 5" width="100%">
    </td>
    <td>
      <img src="https://github.com/user-attachments/assets/84d7a2e4-2868-4005-bda2-0c4f1fc44d8a" alt="Screenshot 6" width="100%">
    </td>
  </tr>

  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/c63d1b08-89e4-4eac-a3fc-52232deb0626" alt="Screenshot 7" width="100%">
    </td>
    <td></td>
    <td></td>
  </tr>
</table>
---

📖 **[Download User Manual (PDF)](https://github.com/user-attachments/files/29550665/User_Manual_Stress_Level_App.pdf)**

---


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


🚀 Installation & Setup
Follow these steps to run the project locally:

1. Clone the repository:


2. Create a virtual environment and activate it:

Bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Linux/Mac:
source venv/bin/activate
3. Install dependencies:

Bash
pip install -r requirements.txt
4. Configure Environment Variables:
Update the chat/config.py file with your API keys:

GOOGLE_API_KEY

TWILIO_ACCOUNT_SID

TWILIO_AUTH_TOKEN

5. Apply Database Migrations:

Bash
python manage.py makemigrations
python manage.py migrate
6. Run the local server:

Bash
python manage.py runserver
Navigate to http://127.0.0.1:8000/ in your browser.

🔐 Demo Access
To explore the platform without registering, you can use the following demo credentials:

Patient Account: Username: demo_patient | Password: Demo@12345

Therapist Account: Username: demo_therapist | Password: Demo@12345

🧠 Machine Learning Architecture
The Clinical Assessment Tool utilizes a Multi-Layer Perceptron (MLP) architecture named MediumNN. It features:

Input Layer: 20 features (anxiety level, sleep quality, academic performance, etc.)

Hidden Layers: 32 neurons -> 16 neurons with Batch Normalization and ReLU activation functions.

Output Layer: 3 classes (Low, Moderate, Critical Stress).

Training Methodology: Augmented training data with carefully tuned micro-noise injection, achieving robust performance without overfitting.

🤝 Contribution
This project is developed as a Capstone/Thesis project. Feedback, bug reports, and pull requests are welcome!





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
