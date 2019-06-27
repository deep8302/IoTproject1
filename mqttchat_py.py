'''
Code Written @ TechieNest Pvt Ltd
Terminal chat client with Paho's Python MQTT implementation.
'''

# Import Paho and time libraries
import paho.mqtt.client as mqtt
import time

# Define various MQTT callback functions - we'll only be using some of these,
# but the others are defined here to help with debugging should you need them
def on_connect(client, userdata, flags, rc):
    print("Connected! rc:", rc)

def on_message(client, userdata, message):
    if str(message.topic) != pubtop:
        print(str(message.topic), str(message.payload.decode("utf-8")))

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed:", str(mid), str(granted_qos))

def on_unsubscribe(client, userdata, mid):#mid to track publish message
    print("Unsubscribed:", str(mid))

def on_publish(client, userdata, mid):
    print("Publish:", client)

def on_log(client, userdata, level, buf):
    print("log:", buf)

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")

# Set the address of your broker and your port. For a local broker, use the IP
# address. Otherwise, use the web address.
broker_address = "iot.eclipse.org"
# broker_address = <insert your IP address here>
port = 1883
# port = 1883 # port for TLS/SSL

# Create the MQTT client and set the callback functions you want to use
client = mqtt.Client()
client.on_subscribe = on_subscribe
client.on_unsubscribe = on_unsubscribe
client.on_connect = on_connect
client.on_message = on_message
time.sleep(1) # Sleep for a beat to ensure things occur in order

# Input username, password, and pub/sub topics in the terminal
user = input('Username: ')
pw = input('Password: ')
pubtop = input('Publish topic: ')
subtop = input('Subscribe topic: ')

# Set user/pass, connect to the broker, start the loop, and subscribe.
# - It's important to do this in order! Subscribing before connecting won't work
client.username_pw_set(user, pw)
client.connect(broker_address, port)
client.loop_start()
client.subscribe(subtop)

# Chat loop
while True:
    chat = input()
    if chat == 'QUIT':
        break
    elif chat == 'SUBSCRIBE':
        new_subtop = input('Subscribe to topic: ')
        client.subscribe(new_subtop)
    elif chat == 'UNSUBSCRIBE':
        unsubtop = input('Unsubscribe from topic: ')
        client.unsubscribe(unsubtop)
    elif chat == 'PUBLISH':
        pubtop = input('Publish to new topic: ')
    else:
        client.publish(pubtop, chat)

# Disconnect and stop the loop!
client.disconnect()
client.loop_stop()
