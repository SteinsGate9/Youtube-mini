# YouTube Clone
Youtube video uploading, real-time streaming and bullet screen.

Developed on Django, supported by Sqlite3, Nginx, FFMpeg, Opencv, Channels Websocket, Redis and JavaScript

This is a small project to play around with the basic usage of these frameworks and back-end
and front-end concepts. The basic HTTP web framework is Django which helps to build the backbone of the application.
The video is stored on local filesystem and the metadata are stored in sqlite. Streaming are supported by nginx proxy server and FFmpeg package.
Real-time bullet screen chat is supported by Websocket and Redis. The frontend is written in HTML and JS.
Reference: https://github.com/Asymptote/asymptote.github.io/wiki/Getting-started-with-nginx-rtmp https://github.com/tabvn/video-streaming-service https://github.com/geekswaroop/YouTube-Clone


 ## How to run


To install dependencies, run:
1. conda create -n youtube_mini python=3.7 && conda activate youtube_mini
2. python -m pip install --upgrade pip (Upgrading pip)
3. pip3 install -r requirements.txt
4. pip install django-crispy-forms

To initialize the Database (sqlite3 file)
1. python manage.py makemigrations
2. python manage.py migrate

To configure & run nginx server
1. edit nginx.conf file, change line 28/48 to your own path
2. nginx -c `pwd`/nginx/nginx.conf

To install FFMpeg
1. if you are doing it on a mac like me, run brew install brew update && brew upgrade ffmpeg
2. pip install ffprobe

To install Opencv
1. pip install opencv-python

To install Websockets
1. python -m pip install -U channels

In order to run this project, execute:
1. python manage.py runserver
2. open http://127.0.0.1:8000/ on your browser
