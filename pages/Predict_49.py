import streamlit as st
import joblib
import numpy as np
from xgboost import XGBClassifier
from utils import *

st.title('Predictive Diagnosis Assistant')

# Load trained model
model = joblib.load('replace with your path/predictive-diagnosis-assistant/trained_models/xgboost_49.joblib')

