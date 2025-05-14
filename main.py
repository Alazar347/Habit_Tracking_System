import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

def show_response(response):
    try:
        data = response.json()
        if data.get("isSuccess"):
            print(f" SUCCESS: {data.get('message')}")
        else:
            print(f" ERROR: {data.get('message')}")
    except Exception:
        print("Could not parse response:", response.text)

def validate_credentials(username, token):
    """Validate the token by accessing a protected endpoint (e.g., graphs)."""
    url = f"{PIXELA_ENDPOINT}/{username}/graphs"
    headers = {"X-USER-TOKEN": token}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return True
    else:
        try:
            print(f" Login failed: {response.json().get('message')}")
        except:
            print(" Login failed: Unknown error.")
        return False


def login_or_create_account():
    while True:
        print("\n Pixela Login System ")
        print("1. Create a new account")
        print("2. Log in to existing account")
        choice = input("Enter 1 or 2: ")

        username = input("Enter your username: ")
        token = input("Enter your token: ")

        if choice == '1':
            user_params = {
                'token': token,
                'username': username,
                'agreeTermsOfService': 'yes',
                'notMinor': 'yes'
            }
            response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
            show_response(response)
            if response.json().get("isSuccess"):
                return username, token
        elif choice == '2':
            if validate_credentials(username, token):
                print("Login successful!")
                return username, token
            else:
                print("Invalid credentials. Please try again.")
        else:
            print("Invalid selection. Choose 1 or 2.")

def create_graph(username, token):
    print("\n--- Create a Graph ---")
    graph_id = input("Graph ID: ")
    name = input("Graph name: ")
    unit = input("Unit (e.g., km, hours): ")
    data_type = input("Data type (int or float): ")
    color = input("Color (shibafu, momiji, sora, ichou, ajisai, kuro): ")

    graph_config = {
        'id': graph_id,
        'name': name,
        'unit': unit,
        'type': data_type,
        'color': color
    }

    headers = {'X-USER-TOKEN': token}
    graph_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs"
    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    show_response(response)

    if response.json().get("isSuccess"):
        graph_url = f"{PIXELA_ENDPOINT}/{username}/graphs/{graph_id}" + ".html"
        print(f"View your graph here: {graph_url}")

    return graph_id

def add_pixel(username, token, graph_id):
    print("\n--- Add Today's Data ---")
    quantity = input("How much did you do today? ")
    today = datetime.now().strftime('%Y%m%d')
    pixel_data = {
        'date': today,
        'quantity': quantity
    }
    headers = {'X-USER-TOKEN': token}
    pixel_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs/{graph_id}"
    response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
    show_response(response)

def update_pixel(username, token, graph_id):
    print("\n--- Update Pixel Data ---")
    date = input("Enter the date (YYYYMMDD): ")
    quantity = input("Enter the new quantity: ")
    headers = {'X-USER-TOKEN': token}
    update_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs/{graph_id}/{date}"
    update_data = {'quantity': quantity}
    response = requests.put(url=update_endpoint, json=update_data, headers=headers)
    show_response(response)

def delete_pixel(username, token, graph_id):
    print("\n--- Delete Pixel Data ---")
    date = input("Enter the date (YYYYMMDD): ")
    headers = {'X-USER-TOKEN': token}
    delete_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs/{graph_id}/{date}"
    response = requests.delete(url=delete_endpoint, headers=headers)
    show_response(response)

def main():
    username, token = login_or_create_account()

    while True:
        print("\n What would you like to do?")
        print("1. Create a new graph")
        print("2. Add today's data")
        print("3. Update past data")
        print("4. Delete data")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            create_graph(username, token)
        elif choice == '2':
            graph_id = input("Graph ID: ")
            add_pixel(username, token, graph_id)
        elif choice == '3':
            graph_id = input("Graph ID: ")
            update_pixel(username, token, graph_id)
        elif choice == '4':
            graph_id = input("Graph ID: ")
            delete_pixel(username, token, graph_id)
        elif choice == '5':
            print("Goodbye! Keep tracking your progress.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()


