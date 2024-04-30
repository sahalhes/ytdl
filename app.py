
from flask import Flask, request
from pytube import YouTube
import os
from flask import Flask, request
from pytube import YouTube

app = Flask(__name__)


@app.route('/download', methods=['POST'])
def download_video():
    url = request.form['url']
    location = request.form['location']  # Get the selected location from the request

    try:
        yt = YouTube(url)
        yt.streams.first().download(output_path=location)  # Specify the output path
        return 'Download successful!'
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True)
