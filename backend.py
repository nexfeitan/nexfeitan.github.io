from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form.get('url')
    if url:
        try:
            # YouTube video indir
            yt = YouTube(url)
            stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
            video_path = stream.download(output_path="downloads/")
            
            # Videoyu kullanıcıya gönder
            return send_file(video_path, as_attachment=True)

        except Exception as e:
            return f"Error: {str(e)}"
    return "Enter"

if __name__ == '__main__':
    app.run(debug=True)
