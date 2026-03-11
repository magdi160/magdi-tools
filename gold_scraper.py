import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os

def scrape_gold():
    # رابط أسعار الذهب في اليمن كمثال لخدمة سحب البيانات
    url = "https://yemen.gold-price-today.com/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # استخراج السعر
        price_row = soup.find("td", {"class": "price"})
        price = price_row.text.strip() if price_row else "N/A"
        
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # حفظ البيانات في ملف CSV لفتحه ببرنامج Excel
        file_exists = os.path.isfile('gold_report.csv')
        with open('gold_report.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(['التاريخ والوقت', 'سعر الذهب'])
            writer.writerow([now, price])
            
        print(f"✅ تم سحب السعر بنجاح: {price}")
    except Exception as e:
        print(f"❌ حدث خطأ: {e}")

if __name__ == "__main__":
    scrape_gold()
