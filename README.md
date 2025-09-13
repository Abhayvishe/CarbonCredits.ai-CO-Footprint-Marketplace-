# Carbon Credit Marketplace & CO₂ Emissions Predictor  

![Python](https://img.shields.io/badge/python-3.10-blue)  
![Streamlit](https://img.shields.io/badge/streamlit-1.28-green)  
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-RandomForest-orange)  
![License](https://img.shields.io/badge/license-MIT-yellow)  

**Streamlit app to predict CO₂ emissions and simulate a carbon credit marketplace.**  

This project demonstrates **end-to-end ML deployment**, combining a trained `RandomForestRegressor` with an interactive marketplace simulation for carbon credits.  

---

## 🚀 Features  

### 🔹 1. CO₂ Emissions Prediction  
- Predicts annual CO₂ emissions (tons/year) using inputs:  
  - Energy consumption (kWh)  
  - Transport distance (km)  
  - Household waste (kg/year)  
  - Flights per year  
- Recommends **carbon credits** to offset predicted emissions.  

### 🔹 2. Carbon Credit Marketplace Simulation  
- **List credits** (seller adds credits for sale).  
- **View available credits** (marketplace table).  
- **Buy credits** (buyer purchases, transaction moves to `transactions.csv`).  

### 🔹 3. Interactive Web App  
- Built with **Streamlit** for real-time predictions.  
- Runs locally at `http://localhost:8501`.  

---








---

## ⚡ Installation  

1. Clone the repository:  
```bash
git clone https://github.com/yourusername/carbon-credit-marketplace.git
cd carbon-credit-marketplace






Install dependencies:
pip install -r requirements.txt



Run the Streamlit app:
streamlit run app.py


Skills & Technologies

Machine Learning: RandomForestRegressor, scikit-learn

Python Libraries: pandas, numpy, joblib

Deployment & UI: Streamlit

Data Handling: CSV-based simulation of marketplace

Project Lifecycle: Data preprocessing → Model training → Deployment → Marketplace simulation



Future Enhancements

📊 Live dashboards: visualize credits traded & CO₂ offsets in real-time

🗄️ Database integration: replace CSVs with SQL/NoSQL backend

🔑 User authentication: secure accounts for buyers/sellers

☁️ Cloud deployment: deploy on AWS/GCP/Heroku for public access

⛓️ Smart contracts: blockchain-based verification of transactions




## Screenshots

### CO₂ Prediction Page
![Prediction Screenshot](screenshots/prediction.png)

### Marketplace View
![Marketplace Screenshot](screenshots/marketplace.png)





## 📂 Project Structure  

