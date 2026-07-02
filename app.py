import streamlit as st
import pandas as pd
import numpy as np
import pickle

# 1. Load model padi dari file pkl
try:
    with open('model_padi.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Error: File 'model_padi.pkl' tidak ditemukan di folder GitHub kamu!")

# 2. Membuat Tampilan Aplikasi Web
st.set_page_config(page_title="Prediksi Padi Sumatera", page_icon="🌾")
st.title("🌾 Aplikasi Estimasi Produksi Padi Sumatera")
st.write("Masukkan indikator di bawah ini untuk memprediksi jumlah produksi padi (Ton):")

st.markdown("---")

# Daftar Provinsi di Sumatera beserta nilai encoding-nya sesuai alfabetis training
provinsi_dict = {
    "Aceh": 0,
    "Bengkulu": 1,
    "Jambi": 2,
    "Lampung": 3,
    "Riau": 4,
    "Sumatera Barat": 5,
    "Sumatera Selatan": 6,
    "Sumatera Utara": 7
}

# Form Input dari Pengguna (Sekarang Pas 6 Fitur)
pilihan_provinsi = st.selectbox("📍 Pilih Provinsi", list(provinsi_dict.keys()))
tahun = st.number_input("📅 Tahun", min_value=1990, max_value=2030, value=2026, step=1)
luas_panen = st.number_input("📐 Luas Panen (Ha)", min_value=0.0, value=100000.0, step=500.0)
curah_hujan = st.number_input("🌧️ Curah Hujan (mm)", min_value=0.0, value=1500.0, step=10.0)
kelembapan = st.number_input("💧 Kelembapan (%)", min_value=0.0, max_value=100.0, value=80.0, step=0.5)
suhu = st.number_input("🌡️ Suhu Rata-rata (°C)", min_value=0.0, max_value=50.0, value=26.0, step=0.1)

st.markdown("---")

# 3. Tombol Eksekusi Prediksi
if st.button("🔮 Hitung Prediksi Produksi"):
    
    # Ambil nilai angka encoding berdasarkan provinsi yang dipilih user
    provinsi_encoded = provinsi_dict[pilihan_provinsi]
    
    # Susun data sesuai dengan urutan fitur asli di model:
    # ['Tahun', 'Luas Panen', 'Curah hujan', 'Kelembapan', 'Suhu rata-rata', 'Provinsi_Encoded']
    input_values = [tahun, luas_panen, curah_hujan, kelembapan, suhu, provinsi_encoded]
    
    # Ubah format menjadi array 2D untuk dimasukkan ke model
    input_data = np.array([input_values])
    
    try:
        # Lakukan prediksi langsung dari numpy array
        hasil_prediksi = model.predict(input_data)
        
        # Tampilkan hasil ke layar web jika sukses
        st.success(f"### Estimasi Produksi Padi di {pilihan_provinsi}: **{hasil_prediksi[0]:,.2f} Ton**")
        
    except Exception as e:
        st.error(f"Terjadi kesalahan saat pemrosesan model: {e}")
