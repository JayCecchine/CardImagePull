# MTG Card Image Fetcher

A Python script that fetches and saves Magic: The Gathering card images from Scryfall based on a provided card list.

## Features

- Fetches high-resolution card images from Scryfall's API
- Supports fuzzy card name matching
- Handles multiple copies of the same card
- Simple command-line interface for inputting card lists
- Automatically saves images with numbered suffixes for multiple copies

## Requirements

```
requests>=2.25.1
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/mtg-card-fetcher.git
cd mtg-card-fetcher
```

2. Install the required dependencies:
```bash
pip install requests
```

## Usage

1. Run the script:
```bash
python mtg_card_fetcher.py
```

2. When prompted, paste your card list in the following format:
```
1 Black Lotus
4 Lightning Bolt
2 Counterspell
```

3. Press Enter twice to submit the list and begin downloading.

The script will create image files in the current directory with names like:
- `Black_Lotus_1.jpg`
- `Lightning_Bolt_1.jpg`
- `Lightning_Bolt_2.jpg`
- `Lightning_Bolt_3.jpg`
- `Lightning_Bolt_4.jpg`
- `Counterspell_1.jpg`
- `Counterspell_2.jpg`

## Error Handling

The script handles various error cases:
- Invalid card names
- Network connection issues
- Missing card images
- API response errors

Error messages will be printed to the console if any issues occur during the download process.

## API Usage

The script uses the Scryfall API to fetch card data. Please be mindful of Scryfall's [rate limits](https://scryfall.com/docs/api) when using this script for large card lists.

## Contributing

Feel free to submit issues and pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Scryfall](https://scryfall.com/) for providing the card data and images
- The Magic: The Gathering community

## Disclaimer

This script is not affiliated with or endorsed by Wizards of the Coast, Scryfall, or any other entity. Card images are property of Wizards of the Coast LLC.
