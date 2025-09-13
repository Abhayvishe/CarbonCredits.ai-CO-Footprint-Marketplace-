
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

st.set_page_config(page_title="CarbonCredits.ai", layout="wide")
st.title("🌍 CarbonCredits.ai — CO₂ Footprint & Marketplace Demo")

# Load model
MODEL_PATH = "../model/model.joblib" if os.path.exists("../model/model.joblib") else "model/model.joblib"
if not os.path.exists(MODEL_PATH):
    st.error("Model not found. Run the training notebook first.")
    st.stop()
model = joblib.load(MODEL_PATH)

# --- Section 1: Prediction ---
st.header("1. Estimate your annual CO₂ emissions")
col1, col2 = st.columns(2)
with col1:
    energy_kwh = st.number_input("Annual electricity (kWh)", min_value=0.0, value=3600.0, step=10.0)
    transport_km = st.number_input("Annual transport (km)", min_value=0.0, value=5000.0, step=10.0)
with col2:
    waste_kg = st.number_input("Annual waste (kg)", min_value=0.0, value=200.0, step=1.0)
    flights = st.number_input("Flights per year", min_value=0, value=1, step=1)

features = np.array([[energy_kwh, transport_km, waste_kg, flights]])
prediction = model.predict(features)[0]
prediction = max(prediction, 0.0)

st.metric("Estimated CO₂ emissions", f"{prediction:.2f} tons")
st.info(f"Recommended credits: {prediction:.2f}")

# --- Section 2: Marketplace ---
st.markdown("---")
st.header("2. Carbon Credit Marketplace (Demo)")

MARKET_CSV = "../data/marketplace.csv" if os.path.exists("../data/marketplace.csv") else "data/marketplace.csv"
TRANS_CSV = "../data/transactions.csv" if os.path.exists("../data/transactions.csv") else "data/transactions.csv"
os.makedirs(os.path.dirname(MARKET_CSV), exist_ok=True)

# Add listing
with st.expander("List credits for sale"):
    with st.form("list_form"):
        seller = st.text_input("Your name", value="seller1")
        credits_tons = st.number_input("Credits (tons)", min_value=0.1, value=1.0, step=0.1)
        price_per_ton = st.number_input("Price per ton", min_value=0.1, value=300.0, step=1.0)
        submit = st.form_submit_button("List for sale")
    if submit:
        df_new = pd.DataFrame([{
            "id": pd.Timestamp.now().strftime("%Y%m%d%H%M%S"),
            "seller": seller,
            "credits_tons": credits_tons,
            "price_per_ton": price_per_ton
        }])
        if os.path.exists(MARKET_CSV):
            df_new.to_csv(MARKET_CSV, mode="a", header=False, index=False)
        else:
            df_new.to_csv(MARKET_CSV, index=False)
        st.success("✅ Listing added!")

# Show listings
if os.path.exists(MARKET_CSV):
    market_df = pd.read_csv(MARKET_CSV)
    st.dataframe(market_df)

# Buy listing
if os.path.exists(MARKET_CSV) and not pd.read_csv(MARKET_CSV).empty:
    market_df = pd.read_csv(MARKET_CSV)
    options = market_df["id"].astype(str).tolist()
    pick = st.selectbox("Select listing ID to buy", options=options)
    buyer = st.text_input("Buyer name", value="buyer1")
    if st.button("Buy"):
        row = market_df[market_df["id"].astype(str) == pick].iloc[0]
        trans = pd.DataFrame([{
            "tx_id": pd.Timestamp.now().strftime("%Y%m%d%H%M%S"),
            "listing_id": row["id"],
            "seller": row["seller"],
            "buyer": buyer,
            "credits_tons": row["credits_tons"],
            "price_per_ton": row["price_per_ton"]
        }])
        if os.path.exists(TRANS_CSV):
            trans.to_csv(TRANS_CSV, mode="a", header=False, index=False)
        else:
            trans.to_csv(TRANS_CSV, index=False)
        # remove from marketplace
        market_df = market_df[market_df["id"].astype(str) != pick]
        market_df.to_csv(MARKET_CSV, index=False)
        st.success("✅ Purchase completed!")
