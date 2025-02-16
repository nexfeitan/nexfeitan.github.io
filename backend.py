from flask import Flask, render_template, request, send_file, redirect, url_for
from pytube import YouTube
import os

app = Flask(__name__)

# Ana Sayfa (GET metodu ile)
@app.route('/')
def index():
    return render_template('index.html')

# Eğer biri "/download" URL'sine elle giderse, ana sayfaya yönlendir
@app.route('/download', methods=['GET'])
def download_redirect():
    return redirect(url_for('index'))

# Video İndirme (Sadece POST metodu kabul eder)
@app.route('/download', methods=['POST'])
def download_video():
    url = request.form.get('url')
    
    if not url:
        return "Hata: URL alınamadı! Formdan bir URL gelmiyor."
    
    try:
        print(f"İndirilecek YouTube URL: {url}")  # Terminale URL yazdır
    
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        video_path = stream.download(output_path="downloads/")

        print(f"İndirildi: {video_path}")  # Terminale indirilen dosya yolu yazdır

        return send_file(video_path, as_attachment=True)

    except Exception as e:
        return f"Hata: {str(e)}"
if __name__ == '__main__':
    app.run(debug=True)
