# Gunakan image Python resmi sebagai base image
FROM python:3.10-slim

# Set direktori kerja di dalam container
WORKDIR /app

# Copy file requirements.txt terlebih dahulu (agar cache build lebih efisien)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install joblib numpy

# Copy semua file aplikasi ke dalam container
COPY . .

# Expose port Flask (default 5000)
EXPOSE 5000

# Jalankan aplikasi Flask
CMD ["python", "app.py"]
