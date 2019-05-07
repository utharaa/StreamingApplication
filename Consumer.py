from kafka import KafkaConsumer
import json
import redis

r = redis.Redis(host='localhost', port=6379, db=0)


if __name__ == '__main__':
    consumer = KafkaConsumer(
            'BITCOINTRANSACTION',
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            value_deserializer=lambda x:json.loads(x.decode('utf-8')))

    for message in consumer:
        data = message.value
        time = data["x"]["time"]
        index = data["x"]["tx_index"]

        key = "transaction_"+str(time)+"_"+str(index)
        try:
            r.set(key, json.dumps(data))
            r.expire(key, 10800)
            print("Message pushed into redis successfully")
        except Exception as ex:
            print('Exception in publishing message')
            print(str(ex))
    consumer.close()