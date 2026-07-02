import streamlit as st
import pandas as pd
import pickle

# 1. Load file pkl
try:
    with open('model_padi.pkl', 'rb') as file:
        model = pickle.load(file)
    with open('fitur_kolom.pkl', 'rb') as file:
        fitur_kolom = pickle.load(file)
except:
    st.error("File pkl tidak ditemukan.")

st.title("🕵️‍♂️ Pelacakan Fitur Model Padi")

# Menampilkan jumlah fitur yang diminta oleh model asli
st.write(f"Model kamu meminta: **{model.n_features_in_} fitur**")

# Menampilkan daftar nama kolom yang tersimpan di file pkl kamu
st.write("Daftar fitur asli dari Google Colab kamu:")
st.json(fitur_kolom)
