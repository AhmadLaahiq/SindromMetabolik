from flask import Flask, render_template, request
import os
import joblib
import numpy as np

app = Flask(__name__)

# Load model dan kolom fitur
model = joblib.load('model.joblib')
try:
    model_columns = joblib.load('random_forest_model.pkl')
except Exception:
    model_columns = None

# Route untuk landing page
@app.route('/')
def landing():
    return render_template('landing.html')

# Route untuk halaman edukasi
@app.route('/artikel')
def edukasi():
    return render_template('artikel.html')

# Route untuk halaman prediksi
@app.route('/prediksi', methods=['GET', 'POST'])
def prediksi():
    hasil = None
    probabilitas = None
    kriteria = 0
    terpenuhi = []
    model_prediksi = None
    if request.method == 'POST':
        nama = request.form.get('nama')
        jenis_kelamin = request.form.get('jenis_kelamin')
        status = request.form.get('status')
        ras = request.form.get('ras')
        usia = float(request.form.get('usia') or 0)
        lingkar_pinggang = float(request.form.get('lingkar_pinggang') or 0)
        bmi = float(request.form.get('bmi') or 0)
        albuminuria = float(request.form.get('albuminuria') or 0)
        acr = float(request.form.get('acr') or 0)
        asam_urat = float(request.form.get('asam_urat') or 0)
        glukosa = float(request.form.get('glukosa') or 0)
        hdl = float(request.form.get('hdl') or 0)
        trigliserida = float(request.form.get('trigliserida') or 0)
        tekanan_sistolik = float(request.form.get('tekanan_sistolik') or 0)
        tekanan_diastolik = float(request.form.get('tekanan_diastolik') or 0)
        # Lingkar pinggang besar (standar sesuai ras dan jenis kelamin)
        if ras in ['White', 'Black']:
            batas_pria = 94
            batas_wanita = 80
            label = "Lingkar pinggang besar (≥94 cm untuk pria, ≥80 cm untuk wanita pada ras White/Black)"
        else:
            batas_pria = 90
            batas_wanita = 80
            label = "Lingkar pinggang besar (≥90 cm untuk pria, ≥80 cm untuk wanita pada ras Asian/Hispanic/Other)"
        if (jenis_kelamin == 'Male' and lingkar_pinggang >= batas_pria) or (jenis_kelamin == 'Female' and lingkar_pinggang >= batas_wanita):
            kriteria += 1
            terpenuhi.append(label)
        if trigliserida >= 150:
            kriteria += 1
            terpenuhi.append("Kadar trigliserida tinggi (≥150 mg/dL)")
        if (jenis_kelamin == 'Male' and hdl < 40) or (jenis_kelamin == 'Female' and hdl < 50):
            kriteria += 1
            terpenuhi.append("Kadar kolesterol HDL rendah (<40 mg/dL untuk pria, <50 mg/dL untuk wanita)")
        if tekanan_sistolik >= 130 or tekanan_diastolik >= 85:
            kriteria += 1
            terpenuhi.append("Tekanan darah tinggi (≥130/85 mmHg)")
        if glukosa >= 100:
            kriteria += 1
            terpenuhi.append("Kadar gula darah puasa tinggi (≥100 mg/dL)")
        if kriteria == 0:
            probabilitas = "2%"
        elif kriteria == 1:
            probabilitas = "10%"
        elif kriteria == 2:
            probabilitas = "30%"
        elif kriteria == 3:
            probabilitas = "70%"
        elif kriteria == 4:
            probabilitas = "90%"
        elif kriteria == 5:
            probabilitas = "99%"
        else:
            probabilitas = "0%"
        if kriteria >= 3:
            hasil = 'POSITIF'
        else:
            hasil = 'NEGATIF'

        # --- Prediksi model ML ---
        if model_columns:
            input_dict = {
                'Sex': jenis_kelamin,
                'Marital': status,
                'Race': ras,
                'Age': usia,
                'WaistCirc': lingkar_pinggang,
                'BMI': bmi,
                'Albuminuria': albuminuria,
                'UrAlbCr': acr,
                'UricAcid': asam_urat,
                'BloodGlucose': glukosa,
                'HDL': hdl,
                'Triglycerides': trigliserida,
                'SystolicBP': tekanan_sistolik,
                'DiastolicBP': tekanan_diastolik
            }
            print('Input dict:', input_dict)
            print('Model columns:', model_columns)
            input_data = [input_dict.get(col, 0) for col in model_columns]
            print('Input data (ordered):', input_data)
            input_array = np.array(input_data).reshape(1, -1)
            print('Input array shape:', input_array.shape)
            try:
                model_prediksi = model.predict(input_array)[0]
                model_proba = model.predict_proba(input_array)[0][1]
                print('Model prediction:', model_prediksi, 'Prob:', model_proba)
                model_proba_percent = round(model_proba * 100, 2)
            except Exception as e:
                print('Model prediction error:', e)
                model_prediksi = None
                model_proba = None
        else:
            print('Model columns not found!')
            model_prediksi = None
            model_proba = None

        return render_template(
            'prediksi.html',
            nama=nama,
            jenis_kelamin=jenis_kelamin,
            status=status,
            ras=ras,
            usia=usia,
            lingkar_pinggang=lingkar_pinggang,
            bmi=bmi,
            albuminuria=albuminuria,
            acr=acr,
            asam_urat=asam_urat,
            glukosa=glukosa,
            hdl=hdl,
            trigliserida=trigliserida,
            tekanan_sistolik=tekanan_sistolik,
            tekanan_diastolik=tekanan_diastolik,
            hasil=hasil,
            probabilitas=probabilitas,
            kriteria=kriteria,
            terpenuhi=terpenuhi,
            model_prediksi=model_prediksi,
            model_proba=model_proba,
            model_proba_percent=model_proba_percent if 'model_proba_percent' in locals() else None
        )
    return render_template(
        'prediksi.html',
        nama=None,
        jenis_kelamin=None,
        status=None,
        ras=None,
        usia=None,
        lingkar_pinggang=None,
        bmi=None,
        albuminuria=None,
        acr=None,
        asam_urat=None,
        glukosa=None,
        hdl=None,
        trigliserida=None,
        tekanan_sistolik=None,
        tekanan_diastolik=None,
        hasil=None,
        probabilitas=None,
        kriteria=None,
        terpenuhi=None,
        model_prediksi=None,
        model_proba=None,
        model_proba_percent=None
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
