from confluent_kafka import Consumer
import redis
import time

consumer = Consumer({
	'bootstrap.servers': 'localhost:9092',
	'group.id': 'group1',
	# 'auto.offset.reset': 'earliest'
})
consumer.subscribe(['test'])
client = redis.Redis(host='localhost', port=6379, db=0)


if __name__ == "__main__":
	print("kafka and redis set!")
	while True:
		msg = consumer.poll(1.0)

		if msg is None:
			continue
		if msg.error():
			print("Consumer error: {}".format(msg.error()))
			continue

		msg = msg.value().decode('utf-8')
		now = time.time()

		if "/" not in msg:
			print("wrong message " + msg)
			continue

		time_ = msg.split("/")[1]
		msg = msg.split("/")[0]
		client.zadd("messages", {msg: int(float(now)) - int(float(time_))})  # time since connection
		print("good message " + str(int(float(now)) - int(float(time_))) + " " + msg)

	client.close()
