# FUTURE_ML_03

# 🤖 Task 3 – Customer Support Chatbot

This project was completed as part of the **Future Interns Machine Learning Internship (Task 3)**.  
The goal was to build an **AI-powered chatbot** that provides automated customer support using **Dialogflow + Streamlit**.

---

## 🔑 Features  
- 👋 Greeting message (*“Hi! How can I help you?”*)  
- ❓ Answers for common FAQs (orders, technical issues, etc.)  
- 🧠 Smart fallback when input is not understood  
- 📊 Extracts structured info (order numbers, names) using Dialogflow entities  
- 💻 Simple, interactive frontend with **Streamlit** 

---

## 🛠️ Tools & Libraries
- **Dialogflow** (Natural Language Processing & intent detection)  
- **Streamlit** (Frontend web app)  
- **Google Cloud SDK** (service account authentication)  

---

## 📂 Repository Structure
```
Customer_Support_Chatbot/
│── notebooks/
│   └── chatbot_dev.ipynb         # (Optional) if you want to show intent/entity training process
│
│── src/
│   └── app.py                    # Main chatbot app (Streamlit + Dialogflow)
│
│── configs/
│   └── service_account.json       # Dialogflow credentials (DO NOT share publicly)
│
│── screenshots/
│   └── chatbot_ui.png            # Screenshot of chatbot interface
│
│── reports/
│   └── chatbot_demo.pdf          # (Optional) PDF with workflow & explanation
│
│── requirements.txt              # Python dependencies
│── README.md                     # Documentation
│── .gitignore                    # Ignore credentials, cache, pyc, etc.
```

---

---

## 📸 Demo Screenshot

<img width="1919" height="1028" alt="Screenshot 2025-09-30 190527" src="https://github.com/user-attachments/assets/693001a6-d7df-4a0d-8106-8b1d984988a4" />

<img width="1915" height="1022" alt="Screenshot 2025-09-30 190550" src="https://github.com/user-attachments/assets/b9b5710c-ee72-4955-8e5b-1c4450661b71" />

<img width="1919" height="1024" alt="Screenshot 2025-09-30 190604" src="https://github.com/user-attachments/assets/3b5b0994-c21b-46bd-a555-688792f3807e" />

---

## 🚀 How to Run
1. Clone this repo  
   ```bash
   git clone https://github.com/SheldonDsouzaML/FUTURE_ML_03.git
2. Navigate into the project folder:
   cd FUTURE_ML_03/code

3. Install dependencies:
   pip install -r requirements.txt

4.Add your Dialogflow credentials file:
   Place your service_account.json in the project folder.
   Update app.py if your filename differs.
   
4.  Run the Streamlit app:
    ```bash
    streamlit run chatbot_app.py
    ```

📌 Internship Details

- **Internship Program** : Future Interns – Machine Learning Internship

- **Candidate ID (CIN)** : FIT/SEP25/ML2769


- **Task** : Customer Support Chatbot (Task 3)

---

## 👨‍💻 Internship
This project is part of **Future Interns – Machine Learning Internship**.  

---

