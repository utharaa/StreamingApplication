import flask
import redis
import json
from flask.helpers import make_response
from datetime import datetime, timedelta

app = flask.Flask(__name__)
app.config["DEBUG"] = True

r = redis.Redis(host='localhost', port=6379, db=0)


@app.route('/show_transactions', methods=['GET'])
def show_transactions():
    response = {}
    i = 0
    for key in sorted(r.scan_iter(match="transaction_*", count=100), reverse=True):
        response[i] = json.loads(r.get(key))
        i += 1

    result = make_response(json.dumps(response))
    result.mimetype = 'application/json'
    return result


@app.route('/transactions_count_per_minute', methods=['GET'])
def transactions_count_per_minute():
    transaction_dict = {}
    last_one_hour_time = datetime.now() - timedelta(hours=1)
    for key in sorted(r.scan_iter(match="transaction_*", count=100), reverse=True):
        count = 1
        data = json.loads(r.get(key))
        if data is not None:
            transaction_time = datetime.fromtimestamp(data["x"]["time"])
            diff = transaction_time - last_one_hour_time
            if diff.seconds <= 3600:
                key = transaction_time.strftime('%H:%M')
                if key in transaction_dict.keys():
                    available_count = transaction_dict[key]
                    transaction_dict[key] = available_count + 1
                else:
                    transaction_dict[key] = count
    if len(transaction_dict) == 0:
        return "There are no active transactions"
    else:
        result = make_response(json.dumps(transaction_dict))
        result.mimetype = 'application/json'

    return result


@app.route('/high_value_addr', methods=['GET'])
def high_value_addr():
    addr_dict = {}
    for key in sorted(r.scan_iter(match="transaction_*", count=100), reverse=True):
        count = 1
        data = json.loads(r.get(key))
        if data is not None:
            for out in data["x"]["out"]:
                if out["addr"] is not None:
                    key = str(out["addr"])
                    if key in addr_dict.keys():
                        print("keys already available, key:", key)
                        available_count = addr_dict[key]
                        addr_dict[key] = available_count + 1
                    else:
                        print("no keys already available")
                        addr_dict[key] = count
        else:
            print("UnExpected error occurred looks like there is no value for the key:", key)

    if len(addr_dict) == 0:
        return "There are no active transactions"
    else:
        result = make_response(json.dumps(addr_dict))
        result.mimetype = 'application/json'

    return result


if __name__ == '__main__':
    app.run(debug=True)