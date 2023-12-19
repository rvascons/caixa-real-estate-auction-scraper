# Caixa Real Estate Auction Scraper

## Overview
This project is designed to scrape the Caixa platform to collect information about upcoming real estate auctions. It efficiently gathers data and formats it into an Excel (`.xlsx`) file for easy analysis and review. This tool is particularly useful for investors, real estate analysts, and anyone interested in the Brazilian real estate auction market.

## Features
- **Data Extraction**: Automatically scrapes data about real estate auctions from the Caixa platform.
- **Data Transformation**: Converts the scraped data into a structured format.
- **Excel Export**: Outputs the collected data into a well-organized `.xlsx` file.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Dependencies: See `requirements.txt`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/rvascons/caixa-real-estate-auction-scraper.git
    ```
2. Navigate to the project directory: 
    ```bash
    cd caixa-imoveis-scraper
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Usage
To start scraping data, run the following command:
```bash
cd caixa-imoveis-scraper
```

### How It Works
The scraper accesses the Caixa platform, identifies upcoming real estate auctions, and extracts relevant information such as auction date, property details, location, starting bid, and other pertinent data.

### Output Format
The output is an Excel file (data.xlsx) containing the following columns:

Auction Date
Property Details
Location
Starting Bid
[Other relevant columns]
Contributing
### Contributions to this project are welcome. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes and commit them (git commit -am 'Add some feature').
4. Push to the branch (git push origin feature-branch).
5. Create a new Pull Request.
### License
This project is licensed under the MIT License.

### Disclaimer
This tool is not affiliated with, endorsed by, or in any way officially connected with Caixa or any of its subsidiaries or affiliates. The information obtained by this tool is for educational and informational purposes only.

### Contact
For any queries or further assistance, please contact Rafael Vasconcelos at rvascons@gmail.com.