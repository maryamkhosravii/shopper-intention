# 🛒 Online Shoppers Intention Prediction

End-to-End Machine Learning Project for predicting whether an online shopper will generate revenue.  
This project is designed as a production-ready ML system that covers data preprocessing (pipeline), modeling with Keras, API deployment with FastAPI, user interface with Streamlit, and containerization with Docker.


## 🔹 Project Highlights

✅ Full ML lifecycle: from raw dataset → preprocessing → modeling → deployment 
✅ Advanced preprocessing (pipeline): outlier handling (Winsorization), encoding, scaling, correlation analysis  
✅ Applied SMOTE oversampling to handle class imbalance  
✅ Designed Sequential Neural Network with L2 regularization & EarlyStopping
✅ Model evaluation using precision, recall, F1-score, ROC-AUC, confusion matrix  
✅ Built secure FastAPI backend with authentication (JWT) & authorization & SQLite DB  
✅ Developed Streamlit frontend for real-time predictions  
✅ Packaged everything with Docker & Docker Compose for easy deployment  

---

## 🔹 Dataset

The dataset is not included in this repository due to its size. Please download the Online Shoppers Intention Dataset manually from the UCI Machine Learning Repository (or Kaggle, if available)

Online Shoppers Intention dataset (UCI)](https://archive.ics.uci.edu/ml/datasets/online+shoppers+purchasing+intention+dataset)
- Samples: 12,330  
- Features: 17  
- Target: `Revenue` (binary classification: 0 = no purchase, 1 = purchase)


## 🔹 Tech Stack
•	Python (scikit-learn, imbalanced-learn, pandas, numpy)
•	Keras (TensorFlow) for model training
•	FastAPI + SQLite for backend & DB
•	Streamlit for frontend
•	Docker + Docker Compose for deployment
 


## 🔹 Model Architecture (Keras Sequential)

- Input layer with normalized features  
- Hidden layers with **Dense + ReLU**, `kernel_regularizer=L2`  
- Output layer: **sigmoid activation** (binary classification)  
- Loss: `binary_crossentropy`  
- Optimizer: Adam  
- Metrics: `accuracy`, `precision`, `recall`, `AUC`  
- **EarlyStopping** based on validation loss  


## 🔹 Model Evaluation

- **Threshold**: 0.5 on predicted probabilities  
- Confusion Matrix used to analyze class-wise performance  
- Classification Report (Test Set):
  - Precision (class 0): 0.93
  - Recall (class 0): 0.93
  - Precision (class 1): 0.61
  - Recall (class 1): 0.62  
- **ROC-AUC**: ~0.89  


## 🔹 Deployment

### FastAPI Backend
- JWT-based authentication (signup/login)
- Prediction endpoint (`/predict/`)
- Stores results in SQLite:
- id, username, features, probability, prediction, timestamp

### Streamlit Frontend
- User Sign Up
- User login  
- Input form for features  
- Real-time prediction with probability score  

### Docker
- Dockerfile for FastAPI  
- Dockerfile.streamlit for Streamlit  
- docker-compose.yml to run everything together

## 🛠️ Installation & Setup
#### Clone the repository
git clone https://github.com/maryamkhosravii/shopper-intention.git
cd shopper-intention
### Install dependencies
pip install -r requirements.txt
### Run FastAPI
uvicorn main:app --reload
### Run Streamlit
streamlit run app.py
### OR Docker (recommended)
docker-compose build
docker-compose up
•	FastAPI → http://localhost:8000
Streamlit → http://localhost:8501 Contac
 

## Contact
Email – mrm.khosravi@yahoo.com

Project Link: https://github.com/maryamkhosravii/shopper-intention

Made with ❤️ by Maryam Khosravi













