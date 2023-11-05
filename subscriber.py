import paho.mqtt.client as mqtt

# Define the on_connect event handler
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected to MQTT Broker! Subscribed to topic '{topic}'")
    else:
        print(f"Failed to connect, return code {rc}")

# Define the on_message event handler
def on_message(client, userdata, msg):
    print(f"Received `{msg.payload.decode()}` from topic `{msg.topic}`")

# Setup the MQTT client
broker = 'localhost'
port = 1883
topic = []
topics = input("Enter the topic to subscribe to ('layoffs' or 'profits'): ")
topics_split = topics.split(' ') 

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker and subscribe to the topic
client.connect(broker, port)

for x in topics_split:
    if x == 'layoffs' or x== 'profits':
        topic.append(x) 
        client.subscribe(x)
    else:
        print(x, ' is not a valid topic')


# Start the loop
client.loop_forever()
