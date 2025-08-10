import streamlit as st
from PIL import Image

st.set_page_config(page_title="Deteksi Sindrom Metabolik", layout="wide")

# --- Sidebar Navigasi ---
st.sidebar.title("🧭 Navigasi")
menu = st.sidebar.selectbox("Pilih Halaman", ["📖 Artikel", "🩺 Prediksi"])

# --- Load Gambar ---
image = Image.open("SM.jpg")

# --- Halaman Artikel ---
if menu == "📖 Artikel":
    st.title("📖 Edukasi Sindrom Metabolik")

    # Header dengan styling
    st.markdown("# Sindrom Metabolik: Mengenali Ancaman Tersembunyi dari Gaya Hidup Modern")
    
    # Gambar di bawah judul dan di tengah
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(image, caption="Infografis Penyakit Metabolik - Kemenkes", width=600)

    st.markdown("""
    Apa yang dimaksud dengan Sindrom metabolik? Metabolic syndrome atau sindrom metabolik adalah sekumpulan kondisi yang dapat meningkatkan risiko penyakit jantung, stroke, dan diabetes pada seseorang. Contohnya kadar gula darah dan tekanan darah tinggi, kenaikan kadar kolesterol, serta lemak berlebihan di sekitar pinggang. Suatu penyakit dikatakan sindrom metabolik bila terdapat setidaknya tiga dari kondisi di atas.

    Apabila hanya mengalami salah satu dari kondisi tersebut, maka belum bisa dikatakan bahwa Anda terkena sindrom metabolik. Namun tetap saja, salah satu dari kondisi itu dapat meningkatkan risiko penyakit serius. Sindrom metabolik sering dialami oleh orang-orang berusia lanjut. Meski begitu, baik anak-anak ataupun orang berusia muda tetap perlu mewaspadai sindrom metabolik.

    Sindrom metabolik adalah kumpulan dari beberapa kondisi medis yang terjadi secara bersamaan dan secara signifikan meningkatkan risiko seseorang terkena penyakit jantung, stroke, dan diabetes tipe 2. Menurut National Heart, Lung, and Blood Institute (NHLBI), seseorang dinyatakan mengalami sindrom metabolik jika memiliki setidaknya tiga dari lima faktor risiko utama:

    - Tekanan darah tinggi (≥130/85 mmHg)
    - Kadar gula darah puasa tinggi (≥100 mg/dL)
    - Kadar trigliserida tinggi (≥150 mg/dL)
    - Kadar kolesterol HDL rendah (<40 mg/dL untuk pria, <50 mg/dL untuk wanita)
    - Lingkar pinggang besar (≥90 cm untuk pria, ≥80 cm untuk wanita di Asia)

    ## Penyebab
    Hingga kini belum diketahui secara pasti penyebab sindrom metabolik. Tetapi, diketahui bahwa sindrom ini erat kaitannya dengan kondisi resistensi insulin. Insulin adalah hormon yang diproduksi oleh organ pankreas dan fungsinya membantu tubuh memetabolisme gula dari makanan.

    Resistensi insulin membuat sel-sel dalam tubuh tidak merespon secara normal terhadap insulin, sehingga glukosa tidak dapat termetabolisme dengan baik dan menyebabkan kadar gula dalam darah meningkat. Hal ini dapat memicu penyakit diabetes.

    Selain resistensi insulin, sindrom metabolik juga berkaitan dengan kondisi seperti kelebihan berat badan (obesitas) serta kurangnya aktivitas fisik. Adapun beberapa gaya hidup kurang sehat yang berpotensi memicu sindrom metabolik adalah sebagai berikut:

    - Jarang berolahraga
    - Stres berkepanjangan
    - Merokok atau sering terpapar asap rokok
    - Terlalu banyak mengonsumsi makanan rendah serat serta tinggi karbohidrat dan lemak

    Sindrom metabolik tidak disebabkan oleh satu faktor tunggal, melainkan merupakan hasil dari kombinasi beberapa penyebab utama:

    - **Obesitas sentral (lemak di perut)**: Indikator utama resistensi insulin
    - **Resistensi insulin**: Ketika insulin tidak dapat bekerja secara efektif
    - **Gaya hidup tidak aktif**: Kurangnya aktivitas fisik
    - **Pola makan buruk**: Konsumsi berlebih gula, garam, lemak jenuh
    - **Faktor genetik dan usia**: Riwayat keluarga dan usia di atas 45 tahun

    ## Dampak
    Jika tidak ditangani, sindrom metabolik bisa menyebabkan komplikasi serius:
    - Penyakit jantung koroner dan stroke
    - Diabetes tipe 2
    - Kerusakan organ lainnya (ginjal, hati berlemak non-alkohol)

    Beberapa faktor tersebut dapat meningkatkan risiko Anda terkena sindrom metabolik. Meski begitu, sindrom ini dapat menyerang siapa saja, tak terkecuali bagi Anda yang tidak memiliki salah satu dari risiko-risiko di atas.

    ## Gejala
    Seperti yang sudah dibahas sebelumnya bahwa sindrom metabolik adalah sekumpulan kondisi yang berbeda-beda tetapi dalam kurun waktu bersamaan. Oleh sebab itu, gejala sindrom metabolik bergantung pada kondisi yang dialami.

    Dalam artian, jika Anda mengalami salah satu kondisi seperti gula darah tinggi, maka Anda akan merasakan beberapa gejala layaknya penderita diabetes. Di antaranya yaitu sering buang air kecil, mudah merasa lapar, serta sering merasa lemas.

    Perlu Anda ketahui bahwa umumnya gejala kolesterol tinggi, tekanan darah tinggi, atau gula darah tinggi muncul secara perlahan, sehingga sulit untuk dideteksi dengan dini. Oleh karenanya, Anda disarankan untuk rutin melakukan pemeriksaan tes darah atau pengecekan tekanan darah.

    ## Pencegahan
    Beberapa langkah pencegahan yang dapat dilakukan:
    - Pola makan seimbang (tinggi serat, rendah lemak jenuh)
    - Rutin berolahraga (30 menit setiap hari)
    - Berhenti merokok dan hindari alkohol
    - Pantau berat badan dan lingkar pinggang
    - Cek kesehatan secara rutin

    ## Penanganan
    Pengobatan sindrom metabolik disesuaikan dengan kondisi yang dikeluhkan pasien. Apabila pasien mengalami peningkatan kadar kolesterol, maka dokter mungkin akan meresepkan obat penurun kolesterol seperti statin.


    Jenis obat tersebut biasanya diberikan kepada pasien dengan riwayat penyakit diabetes, penyakit jantung, atau memiliki kadar kolesterol baik (HDL) yang rendah. Dokter juga akan memberikan obat yang dapat menurunkan risiko serangan jantung, penggumpalan darah, serta tekanan darah tinggi.


    Adapun beberapa pengobatan di rumah yang dapat Anda lakukan untuk mengatasi sindrom metabolik adalah sebagai berikut:


    - Membatasi konsumsi garam.
    - Menjaga berat badan ideal dengan melakukan diet sehat.
    - Rutin berolahraga ringan setiap hari, seperti jalan kaki. Lakukan setidaknya 30 menit per hari.
    - Memulai gaya hidup sehat dengan mengubah pola makan untuk menurunkan kolesterol.
    - Menghindari makanan yang mengandung lemak jenuh.
    
    Jika sudah terdiagnosis, penanganan meliputi:
    - Perubahan gaya hidup total
    - Pengobatan medis (sesuai resep dokter)
    - Pendampingan nutrisi dan olahraga
    - Manajemen stres (yoga, meditasi, relaksasi)

    **Referensi:**
    - https://www.siloamhospitals.com/informasi-siloam/artikel/apa-itu-sindrom-metabolik
    - https://www.nhlbi.nih.gov/health/metabolic-syndrome
    - https://www.who.int/news-room/fact-sheets/detail/noncommunicable-diseases
    - https://www.heart.org/en/health-topics/metabolic-syndrome
    """)

# --- Halaman Prediksi ---
elif menu == "🩺 Prediksi":
    st.title("🩺 Prediksi Sindrom Metabolik")

    with st.form("form_pasien"):
        nama = st.text_input("Nama")
        jenis_kelamin = st.selectbox("Jenis Kelamin", ["Male", "Female"])
        status = st.selectbox("Status Pernikahan", ["Single", "Married"])
        ras = st.selectbox("Ras", ["White", "Black", "Asian", "Hispanic", "Other"])
        usia = st.number_input("Usia", min_value=1, max_value=120, value=25)
        lingkar_pinggang = st.number_input("Lingkar Pinggang (cm)", min_value=0.0)
        bmi = st.number_input("BMI (opsional)", min_value=0.0)
        albuminuria = st.number_input("Albuminuria (opsional)", min_value=0.0)
        acr = st.number_input("Urine Albumin-Creatinine Ratio (opsional)", min_value=0.0)
        asam_urat = st.number_input("Asam Urat (opsional)", min_value=0.0)
        glukosa = st.number_input("Glukosa Darah", min_value=0.0)
        hdl = st.number_input("HDL", min_value=0.0)
        trigliserida = st.number_input("Trigliserida", min_value=0.0)
        tekanan_sistolik = st.number_input("Tekanan Darah Sistolik (mmHg)", min_value=0)
        tekanan_diastolik = st.number_input("Tekanan Darah Diastolik (mmHg)", min_value=0)

        submitted = st.form_submit_button("Prediksi")

    if submitted:
        st.subheader("🔍 Hasil Prediksi")

        # Evaluasi sederhana (rule-based sesuai standar medis)
        kriteria = 0
        terpenuhi = []
        # Lingkar pinggang besar (standar sesuai ras dan jenis kelamin)
        if ras == "White" or ras == "Black":
            batas_pria = 94
            batas_wanita = 80
            label = "Lingkar pinggang besar (≥94 cm untuk pria, ≥80 cm untuk wanita pada ras White/Black)"
        elif ras == "Asian" or ras == "Hispanic" or ras == "Other":
            batas_pria = 90
            batas_wanita = 80
            label = "Lingkar pinggang besar (≥90 cm untuk pria, ≥80 cm untuk wanita pada ras Asian/Hispanic/Other)"
        else:
            batas_pria = 90
            batas_wanita = 80
            label = "Lingkar pinggang besar (≥90 cm untuk pria, ≥80 cm untuk wanita)"
        if (jenis_kelamin == "Male" and lingkar_pinggang >= batas_pria) or (jenis_kelamin == "Female" and lingkar_pinggang >= batas_wanita):
            kriteria += 1
            terpenuhi.append(label)
        # Kadar trigliserida tinggi (≥150 mg/dL)
        if trigliserida >= 150:
            kriteria += 1
            terpenuhi.append("Kadar trigliserida tinggi (≥150 mg/dL)")
        # Kadar kolesterol HDL rendah (<40 mg/dL untuk pria, <50 mg/dL untuk wanita)
        if (jenis_kelamin == "Male" and hdl < 40) or (jenis_kelamin == "Female" and hdl < 50):
            kriteria += 1
            terpenuhi.append("Kadar kolesterol HDL rendah (<40 mg/dL untuk pria, <50 mg/dL untuk wanita)")
        # Tekanan darah tinggi (≥130/85 mmHg)
        if tekanan_sistolik >= 130 or tekanan_diastolik >= 85:
            kriteria += 1
            terpenuhi.append("Tekanan darah tinggi (≥130/85 mmHg)")
        # Kadar gula darah puasa tinggi (≥100 mg/dL)
        if glukosa >= 100:
            kriteria += 1
            terpenuhi.append("Kadar gula darah puasa tinggi (≥100 mg/dL)")

        # Tentukan probabilitas berdasarkan jumlah kriteria
        if kriteria == 0:
            probabilitas = "5.00%"
        elif kriteria == 1:
            probabilitas = "14.00%"
        elif kriteria == 2:
            probabilitas = "35.00%"
        elif kriteria == 3:
            probabilitas = "85.00%"
        elif kriteria == 4:
            probabilitas = "93.00%"
        elif kriteria == 5:
            probabilitas = "98.00%"
        else:
            probabilitas = "0.00%"  # fallback

        if kriteria >= 3:
            hasil = "POSITIF"
            warna = "red"
        else:
            hasil = "NEGATIF"
            warna = "green"

        st.success(f"**Kemungkinan mengalami sindrom metabolik: {hasil}**")
        st.metric("Probabilitas", probabilitas)
        st.subheader("📋 Evaluasi Klinis")
        st.info(f"Pasien hanya memenuhi {kriteria} dari 5 kriteria.")

        # Tampilkan kriteria yang terpenuhi
        if terpenuhi:
            st.markdown("**Kriteria yang terpenuhi:**")
            for t in terpenuhi:
                st.markdown(f"- {t}")
        else:
            st.markdown("Tidak ada kriteria yang terpenuhi.")

        # Tambahkan pesan motivasi/anjuran sesuai hasil
        if hasil == "POSITIF":
            st.warning(f"{nama if nama else 'Pasien'}, konsultasikan kondisi Anda dengan dokter untuk mendapatkan penanganan terbaik sejak dini.")
        else:
            st.info(f"{nama if nama else 'Pasien'}, jangan menunggu sakit untuk mulai hidup sehat. Mulailah dari langkah kecil hari ini.")

if __name__ == "__main__":
    st.run(debug=True)
