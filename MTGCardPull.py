import requests

def fetch_mtg_card_image(card_name, quantity):
    # Create the API URL for the card on Scryfall
    base_url = "https://api.scryfall.com/cards/named?fuzzy="
    search_url = base_url + card_name.replace(" ", "+")  # Format the card name for URL
    response = requests.get(search_url)

    if response.status_code == 200:
        card_data = response.json()
        image_url = card_data.get("image_uris", {}).get("normal")

        if image_url:
            print(f"Image found for {card_name}: {image_url}")

            # Download the image
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                # Save the image for each quantity
                for i in range(quantity):
                    image_name = f"{card_name.replace(' ', '_')}_{i+1}.jpg"
                    with open(image_name, 'wb') as img_file:
                        img_file.write(image_response.content)
                    print(f"Image saved as {image_name}")
            else:
                print(f"Failed to download the image for {card_name}.")
        else:
            print(f"No image URL found for {card_name}.")
    else:
        print(f"Failed to retrieve card details for {card_name}. Status code: {response.status_code}")

def process_card_list(card_list):
    for card in card_list.splitlines():
        if card.strip():  # Skip empty lines
            quantity, card_name = card.split(" ", 1)
            fetch_mtg_card_image(card_name.strip(), int(quantity))

if __name__ == "__main__":
    # Paste the card list directly into the prompt
    print("Paste your card list below (e.g., '1 Card Name') and press Enter twice to submit:")
    card_list = ""
    while True:
        line = input()
        if not line:
            break
        card_list += line + "\n"

    # Process the card list
    process_card_list(card_list)
