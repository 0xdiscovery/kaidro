import requests
import random
import time

# Configurations
base_url = "https://kaidro.com/nft/journal_nft/"
output_file = "ids_gaias.txt"
min_delay = 0  # seconds
max_delay = 5  # seconds
start_id = 0
end_id = 1000

def fetch_nft_data(nft_id):
    url = f"{base_url}{nft_id}.json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def random_delay():
    # Generate a random delay between min_delay and max_delay seconds
    return random.uniform(min_delay, max_delay)

def main():
    print("Starting the process...")
    # Loop within the range of IDs
    for nft_id in range(start_id, end_id + 1):
        print(f"Requesting data for ID {nft_id}...")
        nft_data = fetch_nft_data(nft_id)
        if nft_data and nft_data.get("properties", {}).get("type") == "gaias":
            print(f"ID {nft_id} found as type 'gaias'. Saving...")
            # If the type is "gaias", save the ID to a text file
            with open(output_file, "a") as f:
                f.write(f"{nft_id}\n")
        else:
            print(f"ID {nft_id} does not correspond to type 'gaias'.")
        # Wait for a random period of time before the next request
        delay = random_delay()
        print(f"Waiting for {delay:.2f} seconds before the next request...")
        time.sleep(delay)
    print("Process completed!")

if __name__ == "__main__":
    main()
