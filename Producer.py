import websocket
import json
import time
from threading import Thread
from kafka import KafkaProducer


_producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda v: json.dumps(v).encode('utf-8'))


def publish_message(topic_name, message):
    try:
        _producer.send(topic_name, message)
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def on_message(ws, message):
    message_json = json.loads(message)
    publish_message("BITCOINTRANSACTION", message_json)
    msg_json = json.loads(message)
    print("received message:",msg_json)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    def run(*args):
        for i in range(100):
            ws.send("{\"op\":\"unconfirmed_sub\"}")
            time.sleep(1)
        time.sleep(1)
        ws.close()
        print("Thread terminating...")
    Thread(target=run).start()


def initiate():
    websocket.enableTrace(True)
    host = "wss://ws.blockchain.info/inv"
    ws = websocket.WebSocketApp(host,on_close=on_close,on_message=on_message,on_error=on_error)
    ws.on_open = on_open
    ws.run_forever()


if __name__ == '__main__':
    initiate()