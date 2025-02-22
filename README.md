# eBay Product Scraper  

## Overview  
The **eBay Product Scraper** is a web scraper that extracts product listings from eBay based on a given search query. It retrieves product names, prices, URLs, and ratings, then saves the data in JSON and CSV formats. The scraper uses **Selenium** for web automation and **BeautifulSoup** for parsing, ensuring accurate data extraction.  

## Features  
- Scrapes product listings from eBay  
- Uses **Selenium** for web automation and **BeautifulSoup** for parsing  
- Supports dynamic scrolling to load all products  
- Saves extracted data as **JSON** and **CSV** files  
- Includes **unit tests** to validate functionality  

## Setup  

### Prerequisites  
Ensure you have **Python 3.8+** installed.  

### Installation  
1. **Clone the repository:**  
   ```sh  
   git clone https://github.com/your-username/ebay-scraper.git  
   cd ebay-scraper  
   ```  

2. **Create and activate a virtual environment (recommended):**  
   ```sh  
   python -m venv venv  
   source venv/bin/activate  # On Windows: venv\Scripts\activate  
   ```  

3. **Install dependencies:**  
   ```sh  
   pip install -r requirements.txt  
   ```  

## Usage  

### Running the Scraper  
Execute the scraper with:  
```sh  
python scrape.py  
```  
This will fetch eBay product listings based on the specified search query and save the results in **`ebay_products.json`** and **`ebay_products.csv`**.  

### Running Tests  
To run unit tests and validate the scraper:  
```sh  
python test_scrape.py  
```  

## Configuration  
- Modify `search_query` in `scrape.py` to scrape a different product.  
- Adjust `max_products` to limit the number of results.  

## Notes  
- The scraper scrolls dynamically to load additional products, but this depends on eBay’s page structure.  
- If no results are retrieved, ensure **Selenium** and **webdriver-manager** are up to date.  
- The scraper does **not** bypass CAPTCHAs, so excessive requests might lead to temporary blocks.  

## Future Improvements  
- Implement **proxy rotation** to avoid detection.  
- Improve **error handling** for network failures.  
- Add support for **multi-threading** to speed up scraping.  
- Extract additional product details like **seller ratings** and **shipping info**.  

## License  
This project is open-source and available under the **MIT License**.  

# abm_egypt
