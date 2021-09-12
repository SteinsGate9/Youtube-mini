# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from confluent_kafka import Producer
import time

class ChatConsumer(WebsocketConsumer):
	def connect(self):
		self.room_name = self.scope['url_route']['kwargs']['room_name']
		self.room_group_name = 'chat_%s' % self.room_name

		# Join room group
		async_to_sync(self.channel_layer.group_add)(
			self.room_group_name,
			self.channel_name
		)

		self.accept()

	def disconnect(self, close_code):
		# Leave room group
		async_to_sync(self.channel_layer.group_discard)(
			self.room_group_name,
			self.channel_name
		)

	# Receive message from WebSocket
	def receive(self, text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json['message']

		# Send message to room group
		async_to_sync(self.channel_layer.group_send)(
			self.room_group_name,
			{
				'type': 'chat_message',
				'message': message
			}
		)

	# Receive message from room group
	def chat_message(self, event):
		message = event['message']

		# Send message to WebSocket
		self.send(text_data=json.dumps({
			'message': message
		}))


# def delivery_report(err, msg):
# 	""" Called once for each message produced to indicate delivery result.
# 		Triggered by poll() or flush(). """
# 	if err is not None:
# 		print('Message delivery failed: {}'.format(err))
# 	else:
# 		print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))
#
#
# class ChatConsumer(WebsocketConsumer):
# 	def connect(self):
# 		self.room_name = self.scope['url_route']['kwargs']['room_name']
# 		self.room_group_name = 'chat_%s' % self.room_name
#
# 		# create kafka
# 		self.p = Producer({'bootstrap.servers': 'localhost:9092'})
# 		self.cur_time = time.time()
#
# 		# accept
# 		self.accept()
#
# 	def disconnect(self, close_code):
# 		pass
# 		# Leave room group
# 		# async_to_sync(self.channel_layer.group_discard)(
# 		# 	self.room_group_name,
# 		# 	self.channel_name
# 		# )
#
# 	# Receive message from WebSocket
# 	def receive(self, text_data):
# 		# get message from websocket
# 		text_data_json = json.loads(text_data)
# 		message = text_data_json['message']
#
# 		# send message to kafka
# 		# Trigger any available delivery report callbacks from previous produce() calls
# 		self.p.poll(0)
#
# 		# Asynchronously produce a message, the delivery report callback
# 		# will be triggered from poll() above, or flush() below, when the message has
# 		# been successfully delivered or failed permanently.
# 		message += "/" + str(self.cur_time)
# 		self.p.produce('test', message.encode('utf-8'), callback=delivery_report)
#
# 		# Send message to room group
# 		# async_to_sync(self.channel_layer.group_send)(
# 		# 	self.room_group_name,
# 		# 	{
# 		# 		'type': 'chat_message',
# 		# 		'message': message
# 		# 	}
# 		# )
#
# 	# Receive message from room group
# 	def chat_message(self, event):
# 		message = event['message']
#
# 		# Send message to WebSocket
# 		# self.send(text_data=json.dumps({
# 		# 	'message': message
# 		# }))
