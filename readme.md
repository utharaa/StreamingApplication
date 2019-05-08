# Streaming application

streaming application which reads data from realtime bitcoin transactions

# Installation

execute producer.py
execute consumer.py
and run the run.py

# API details

Show transaction

```
    http://127.0.0.1:5000/show_transactions
    
    Response
    {{'op': 'utx', 'x': {'lock_time': 0, 'ver': 1, 'size': 224, 'inputs': [{'sequence': 4294967295, 'prev_out': {'spent': True, 'tx_index': 444260666, 'type': 0, 'addr': 'bc1qzn0kdgjn30v66h6vs4fa40x5lx4n48dc0n376k', 'value': 447239, 'n': 1, 'script': '001414df66a2538bd9ad5f4c8553dabcd4f9ab3a9db8'}, 'script': ''}], 
'time': 1557133465, 'tx_index': 444269509, 'vin_sz': 1, 'hash': '1d1f9c00370228f9ddb8aa990be498d68e50bf0755dc4289cb83049df30d7ff6', 'vout_sz': 2, 'relayed_by': '0.0.0.0', 'out': [{'spent': False, 'tx_index': 444269509, 'type': 0, 'addr': 'bc1qe66wsyepfst9n67f9upr4rk43fzh9vm6u9x2ku', 'value': 29707, 'n': 0, 'script': '0014ceb4e813214c1659ebc92f023a8ed58a4572b37a'}, {'spent': False, 'tx_index': 444269509, 'type': 0, 'addr': '3Ca8JgdVrGrLArkNzrT3gaBJpnbyx3BqqC', 'value': 410339, 'n': 1, 'script': 'a914775bcc9114abb115501491e214f4478b16ba0d0887'}]}}}
    
``` 

high_addr

```
http://127.0.0.1:5000/high_value_addr

Response
{ 'bc1qe66wsyepfst9n67f9upr4rk43fzh9vm6u9x2ku':'1','12B5DVbvj631wZ7S1vZPBjKwHDmyvWqTxU':'2'}
```
transactions_count_per_minute

```
    http://127.0.0.1:5000/transactions_count_per_minute
    
    Response
    {"20:03": 251, "20:02": 254}
 ```
 
 