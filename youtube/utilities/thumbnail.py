# this file is created for thumbnail algorithm
import ffmpeg

# creating a object
def create_thumbnaiL(video_path, image_path):
	import sys
	sys.path.append('youtube/static/libs/ffmpeg')
	print()
	probe = ffmpeg.probe(video_path)
	video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
	width = int(video_stream['width'])
	height = int(video_stream['height'])

	(
		ffmpeg
			.input(video_path, ss=2)
			.filter('scale', width, -1)
			.output(image_path, vframes=1)
			.run()
	)

	return
