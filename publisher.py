import json
from datetime import datetime

# Assume we're using a JSON file as our queue
QUEUE_FILE = 'message_queue.json'

def queue_message(topic, message):
    # Append a message to the queue file
    try:
        # Load the existing data
        with open(QUEUE_FILE, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    # Append the new message with a timestamp
    data.append({
        'topic': topic,
        'message': message,
        'timestamp': datetime.now().isoformat()
    })

    # Save the updated data
    with open(QUEUE_FILE, 'w') as file:
        json.dump(data, file)

try:
    while True:
        topic = input("Enter the topic to publish to ('layoffs' or 'profits'): ")
        if topic not in ['layoffs', 'profits']:
            print("Invalid topic. Please use 'layoffs' or 'profits'.")
            continue
        message = input("Enter the message to queue: ")
        queue_message(topic, message)
        print(f"Queued message on topic `{topic}`")
except KeyboardInterrupt:
    print("Publisher is stopped.")
