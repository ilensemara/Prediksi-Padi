import streamlit as st
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

# Form Input dari Pengguna (5 Fitur Utama)
tahun = st.number_input("📅 Tahun", min_value=1990, max_value=2030, value=2026, step=1)
luas_panen = st.number_input("📐 Luas Panen (Ha)", min_value=0.0, value=100000.0, step=500.0)
curah_hujan = st.number_input("🌧️ Curah Hujan (mm)", min_value=0.0, value=1500.0, step=10.0)
kelembapan = st.number_input("💧 Kelembapan (%)", min_value=0.0, max_value=100.0, value=80.0, step=0.5)
suhu = st.number_input("🌡️ Suhu Rata-rata (°C)", min_value=0.0, max_value=50.0, value=26.0, step=0.1)

st.markdown("---")

# 3. Tombol Eksekusi Prediksi
if st.button("🔮 Hitung Prediksi Produksi"):
    
    # Mengubah input langsung menjadi format matriks angka 2D (tanpa nama kolom Pandas)
    # Urutan sesuai dengan urutan X saat training: [Tahun, Luas Panen, Curah Hujan, Kelembapan, Suhu]
    input_data = np.array([[tahun, luas_panen, curah_hujan, kelembapan, suhu]])
    
    try:
        # Lakukan prediksi langsung dari numpy array
        hasil_prediksi = model.predict(input_data)
        
        # Tampilkan hasil ke layar web jika sukses
        st.success(f"### Estimasi Produksi Padi: **{hasil_prediksi[0]:,.2f} Ton**")
        
    except Exception as e:
        st.error(f"Terjadi kesalahan saat pemrosesan model. Kemungkinan urutan/jumlah fitur model tidak sesuai.")
        st.info("Pesan Error Sistem: " + str(e))
