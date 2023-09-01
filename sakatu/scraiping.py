import requests
from bs4 import BeautifulSoup
import csv

# 初めのページのURL
base_url = 'https://sauna-ikitai.com/saunas/9134/posts'
page_number = 1

# CSVファイルを開く
with open('sauna_reviews.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['review']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    while True:
        # ページのURLを作成
        url = f"{base_url}?page={page_number}"
        
        # ウェブページを取得
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # <p class="p-postCard_text"> タグを検索
        reviews = soup.find_all('p', class_='p-postCard_text')

        # 口コミがない場合、ループを抜ける
        if not reviews:
            break

        # 口コミをCSVファイルに保存
        for review in reviews:
            writer.writerow({'review': review.text})
        
        # 次のページへ
        page_number += 1