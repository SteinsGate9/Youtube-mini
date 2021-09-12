import subprocess
import cv2
import threading
from multiprocessing import Process

cap = cv2.VideoCapture(0)

# gather video info to ffmpeg
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


def do_streaming(url):
	p = Process(target=do_streaming_ori, args=(url,))
	p.start()
	# thread = threading.Thread(target=do_streaming_ori, args=(url,))
	# thread.start()
	return p.pid


def do_streaming_ori(url):
	# command and params for ffmpeg
	command = ['ffmpeg',
	           '-re',
	           '-f', 'rawvideo',
	           '-vcodec', 'rawvideo',
	           '-pix_fmt', 'yuv420p',
	           '-an',
	           '-use_wallclock_as_timestamps', '1',
	           '-s', "{}x{}".format(width, height),
	           '-i', '-',
	           '-c:v', 'libx264',
	           '-b:v', '512k',
	           '-bufsize', '512k',
	           '-minrate', '256k',
	           '-maxrate', '600k',
	           '-tune', 'zerolatency',
	           '-preset', 'ultrafast',
	           '-f', 'flv',
	           url]

	# using subprocess and pipe to fetch frame data
	p = subprocess.Popen(command, stdin=subprocess.PIPE)

	while cap.isOpened():
		ret, frame = cap.read()
		# print("writing")
		if not ret:
			break

		# write to pipe
		p.stdin.write(frame.tobytes())


if __name__ == "__main__":
	do_streaming("rtmp://localhost:1935/live/19")
