import requests
import json

# Webex API configuration
WEBEX_TOKEN = "-d6d4-4e58-9294-0fa22ab39d78"
BASE_URL = "https://webexapis.com/v1"

# Headers for API requests
headers = {
    "Authorization": f"Bearer {WEBEX_TOKEN}",
    "Content-Type": "application/json"
}

def get_room_id(room_name):
    """Get the room ID for a given room name."""
    response = requests.get(
        f"{BASE_URL}/rooms",
        headers=headers
    )
    if response.status_code == 200:
        rooms = response.json().get("items", [])
        for room in rooms:
            if room.get("title") == room_name:
                return room.get("id")
    return None

def get_messages(room_id):
    """Get all messages in a room."""
    response = requests.get(
        f"{BASE_URL}/messages",
        params={"roomId": room_id},
        headers=headers
    )
    if response.status_code == 200:
        return response.json().get("items", [])
    return []

def delete_message(message_id):
    """Delete a specific message."""
    response = requests.delete(
        f"{BASE_URL}/messages/{message_id}",
        headers=headers
    )
    return response.status_code == 204

def create_message(room_id, text):
    """Create a new message in the room."""
    data = {
        "roomId": room_id,
        "text": text
    }
    response = requests.post(
        f"{BASE_URL}/messages",
        headers=headers,
        json=data
    )
    return response.status_code == 200

def main():
    # Get the room ID
    room_name = "DEVASC2025 Space"
    room_id = get_room_id(room_name)
    
    if not room_id:
        print(f"Could not find room: {room_name}")
        return
    
    print(f"Found room: {room_name}")
    
    # Get all messages
    messages = get_messages(room_id)
    
    # Find and delete the specific message
    target_text = "Hello everyone! This is a test message from the Webex API script."
    for message in messages:
        if message.get("text") == target_text:
            message_id = message.get("id")
            if delete_message(message_id):
                print("Successfully deleted the target message")
            else:
                print("Failed to delete the message")
            break
    
    # Create new message
    new_message = "Previous post did not meet guidelines."
    if create_message(room_id, new_message):
        print("Successfully created new message")
    else:
        print("Failed to create new message")

if __name__ == "__main__":
    main() 