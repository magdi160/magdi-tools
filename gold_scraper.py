import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os

def scrape_gold_yemen():
    url = "https://yemen.gold-price-today.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        print("🔍 جاري قنص أسعار الذهب من جدول الموقع...")
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # البحث عن أول جدول في الصفحة (جدول الأسعار)
        table = soup.find("table")
        rows = table.find_all("tr") if table else []
        
        # سنأخذ أول صف يحتوي على سعر (عادة يكون عيار 24)
        gold_data = "لم يتم العثور على بيانات"
        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 2:
                # نأخذ اسم العيار + السعر بالريال اليمني
                gold_data = f"{cols[0].text.strip()} : {cols[1].text.strip()}"
                break # نكتفي بأول عيار (الأكثر طلباً)

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # حفظ النتيجة
        file_name = 'gold_report.csv'
        file_exists = os.path.isfile(file_name)
        with open(file_name, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(['التاريخ', 'العيار والسعر'])
            writer.writerow([now, gold_data])
            
        print(f"✅ تم السحب بنجاح!")
        print(f"💰 البيانات: {gold_data}")
        print(f"📁 تم التحديث في ملف: {file_name}")
        
    except Exception as e:
        print(f"❌ حدث خطأ: {e}")

if __name__ == "__main__":
    scrape_gold_yemen()
