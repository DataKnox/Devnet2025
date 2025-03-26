import requests
import json

# Webex API configuration
WEBEX_ACCESS_TOKEN = "-d6d4-4e58-9294-0fa22ab39d78"
BASE_URL = "https://webexapis.com/v1"

# Headers for API requests
HEADERS = {
    "Authorization": f"Bearer {WEBEX_ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

def create_team(team_name):
    """Create a new Webex team."""
    url = f"{BASE_URL}/teams"
    payload = {
        "name": team_name
    }
    
    response = requests.post(url, headers=HEADERS, json=payload)
    if response.status_code == 200:
        return response.json()["id"]
    else:
        print(f"Error creating team: {response.text}")
        return None

def create_space(team_id, space_name):
    """Create a new space in the team."""
    url = f"{BASE_URL}/rooms"
    payload = {
        "title": space_name,
        "teamId": team_id
    }
    
    response = requests.post(url, headers=HEADERS, json=payload)
    if response.status_code == 200:
        return response.json()["id"]
    else:
        print(f"Error creating space: {response.text}")
        return None

def add_member_to_space(space_id, email):
    """Add a member to the space."""
    url = f"{BASE_URL}/memberships"
    payload = {
        "roomId": space_id,
        "personEmail": email,
        "isModerator": False
    }
    
    response = requests.post(url, headers=HEADERS, json=payload)
    if response.status_code == 200:
        print(f"Successfully added {email} to the space")
    else:
        print(f"Error adding member: {response.text}")

def add_member_to_team(team_id, email):
    """Add a member to the team."""
    url = f"{BASE_URL}/team/memberships"
    payload = {
        "teamId": team_id,
        "personEmail": email,
        "isModerator": False
    }
    
    response = requests.post(url, headers=HEADERS, json=payload)
    if response.status_code == 200:
        print(f"Successfully added {email} to the team")
    else:
        print(f"Error adding member to team: {response.text}")


def post_message(space_id, message):
    """Post a message to the space."""
    url = f"{BASE_URL}/messages"
    payload = {
        "roomId": space_id,
        "text": message
    }
    
    response = requests.post(url, headers=HEADERS, json=payload)
    if response.status_code == 200:
        print("Message posted successfully")
    else:
        print(f"Error posting message: {response.text}")



def main():
    # Create a team
    team_name = "DEVASC2025 Team"
    team_id = create_team(team_name)
    if not team_id:
        return
    
    # Create a space in the team
    space_name = "DEVASC2025 Space"
    space_id = create_space(team_id, space_name)
    if not space_id:
        return
    
    # Add members to the team and space
    members = [
        "member1@example.com",
        "member2@example.com"
    ]
    
    
    # First add members to the team
    for email in members:
        add_member_to_team(team_id, email)
    
    for email in members:
        add_member_to_space(space_id, email)
    
    # Post a message to the space
    message = "Hello everyone! This is a test message from the Webex API script."
    post_message(space_id, message)

if __name__ == "__main__":
    main()
