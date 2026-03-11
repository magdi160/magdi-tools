# --------------------------------------------------
# Project: Magdi Tools Suite
# Developer: magdi160
# Description: Automated Gold Price Scraper (Yemen)
# Rights: Produced by magdi160 - 2026
# --------------------------------------------------

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os

def scrape_gold_yemen():
    print("--- Tool Produced by magdi160 ---")
    url = "https://yemen.gold-price-today.com/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find("table")
        rows = table.find_all("tr") if table else []
        
        gold_data = "No Data Found"
        if rows:
            for row in rows:
                cols = row.find_all("td")
                if len(cols) >= 2:
                    gold_data = f"{cols[0].text.strip()} : {cols[1].text.strip()}"
                    break

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # حفظ البيانات مع توقيع المبرمج
        file_name = 'gold_report.csv'
        file_exists = os.path.isfile(file_name)
        with open(file_name, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(['Developer: magdi160', 'Timestamp', 'Price Data'])
            writer.writerow(['magdi160', now, gold_data])
            
        print(f"✅ Success! Data captured by magdi160: {gold_data}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    scrape_gold_yemen()
