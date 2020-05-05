#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import json

user = {'email':'korisnik@email.com', 
        'password':'korisnik'}
tokens_url = "http://localhost/tokens"

r = requests.post(url = tokens_url, json = user)
token = json.loads(r.text)["token"]

thing = json.loads(requests.get("http://localhost/things?name=wind",
            headers={"Authorization":token}).text)["things"][0]
channel = json.loads(requests.get("http://localhost/things/"+thing["id"]+"/channels",
            headers={"Authorization":token}).text)['channels'][0]


# In[ ]:


import paho.mqtt.client as mqtt
import random
from datetime import datetime

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_disconnect(client, userdata, rc):
    client.reconnect()
    
def on_publish(client, userdata, mid):
    print("published")
    
def send_msg():
    message = json.dumps(
        [{"value":random.randrange(0,120),
          "time":datetime.now().isoformat()}])
    
    print(message)
    client.publish(
    "channels/"+channel['id']+"/messages/wind",
    payload=message)
    
    
client = mqtt.Client()
client.on_connect = on_connect

client.username_pw_set(thing['id'], thing['key'])
client.connect("localhost")


# In[ ]:


import schedule
import time

schedule.every(5).seconds.do(send_msg)
while(1):
    schedule.run_pending()
    time.sleep(1)


# In[ ]:




