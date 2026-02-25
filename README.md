# 🏦 Bank Customer Churn Prediction

A Machine Learning web application that predicts whether a bank customer is likely to churn (exit) based on financial and demographic information.

This project uses **PyTorch** for model building and **Streamlit** for deployment.

---

## 📌 Project Overview

Customer churn prediction is important for banks to identify customers who are likely to leave.  
This application allows users to input customer details and get:

- ✅ Churn Prediction (Stay / Exit)
- 📊 Probability Score

---

## 🧠 Features Used

The model was trained using the following features:

- CreditScore  
- Age  
- Tenure  
- Balance  
- NumOfProducts  
- HasCrCard  
- IsActiveMember  
- EstimatedSalary  
- Geography_Germany  
- Geography_Spain  
- Gender_Male  

### 🌍 Geography Encoding

France is used as the baseline:

| Country  | Germany | Spain |
|----------|----------|--------|
| France   | 0        | 0      |
| Germany  | 1        | 0      |
| Spain    | 0        | 1      |

---

## 🏗️ Tech Stack

- Python
- PyTorch
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Streamlit

---

## 📂 Project Structure

```
project/
│
├── app.py                                 # Streamlit application
├── Customer Churn Prediction.ipynb        # IPYNB File
├── model.pkl                              # Trained model
├── requirements.txt                       # Dependencies
└── README.md                              # Project documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/NikeshGangwar41/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate environment:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the Application

```bash
streamlit run app.py
```

The application will open at:

```
http://localhost:8501
```

---

## 📊 Model Training Details

- Framework: PyTorch  
- Loss Function: Binary Cross Entropy  
- Optimizer: Adam  
- Feature Scaling: StandardScaler  
- Train/Test Split: scikit-learn  
- Evaluation Metric: Accuracy Score  

---

## 🌍 Deployment

This app can be deployed on:

- Streamlit Community Cloud
- Render
- HuggingFace Spaces
- Railway

### Deployment Checklist:

- ✅ `app.py` in root directory  
- ✅ `requirements.txt` included  
- ✅ Model file uploaded  
- ✅ GitHub repository connected  

---

## 🔮 Future Improvements

- Add CSV batch prediction
- Add model performance dashboard
- Add feature importance visualization
- Improve UI design
- Add Docker support

---


## 📜 License

This project is for educational and portfolio purposes.
