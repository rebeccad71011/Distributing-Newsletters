import paho.mqtt.client as mqtt
import json
from datetime import datetime, time
import time as time_module

# Define the on_connect event handler
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker for dispatching messages.")
    else:
        print(f"Failed to connect, return code {rc}")

# Setup the MQTT client
broker = 'localhost'
port = 1883
client = mqtt.Client()
client.on_connect = on_connect
client.connect(broker, port)
client.loop_start()

QUEUE_FILE = 'message_queue.json'

# Function to publish messages
def dispatch_messages():
    try:
        # Load the messages from the queue
        with open(QUEUE_FILE, 'r') as file:
            messages = json.load(file)
        
        # Publish each message
        for message_data in messages:
            client.publish(message_data['topic'], message_data['message'])
            print(f"Dispatched message to topic `{message_data['topic']}`")

        # Clear the queue file after dispatching
        with open(QUEUE_FILE, 'w') as file:
            json.dump([], file)
    except FileNotFoundError:
        print("No queued messages to dispatch.")

# Main loop that checks the time and dispatches messages at 10 PM
while True:
    current_time = datetime.now().time()
    if current_time >= time(16, 40) and current_time <= time(16, 41):
        dispatch_messages()
        # Sleep to prevent multiple dispatches between specified tim
        time_module.sleep(60)
    time_module.sleep(10)  # Check the time every 10 seconds
