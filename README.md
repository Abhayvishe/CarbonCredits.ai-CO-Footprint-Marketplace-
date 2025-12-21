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





### Planned improvements (short-term & long-term)

We plan to evolve the project across several axes to increase reliability, transparency, and usability:

- Model & Data
  - Add rigorous evaluation (MAE, RMSE, cross-validation) and baseline comparisons.
  - Provide explainability (SHAP) and prediction uncertainty (prediction intervals).
  - Improve data provenance and preprocessing pipelines.

- Platform & DevOps
  - Containerize the app with Docker and provide docker-compose for local testing.
  - Add CI/CD with GitHub Actions (tests, linting, build).
  - Introduce model & dataset versioning (MLflow/DVC) and monitoring for data drift.

- Marketplace Features
  - Replace CSVs with a transactional database (Postgres/SQLite) and a REST API (FastAPI).
  - Add user authentication, seller verification, and an escrow/payment integration (Stripe).
  - Implement audit trails and support uploads of certification documents for credits.

- Trust & Verification
  - Integrate with recognized carbon registries (e.g., Verra, Gold Standard) or allow attachment of verification docs.
  - Implement MRV (Measurement, Reporting, Verification) workflow for sellers.

- UX, Security & Scale
  - Improve marketplace UX (search, filters, pagination) and accessibility.
  - Add logging, monitoring (Prometheus/Grafana), and Sentry for error tracking.
  - Plan for cloud deployment and horizontal scaling with caching (Redis).

Contributions welcome — see CONTRIBUTING.md for how to help.

