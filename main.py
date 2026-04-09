
import requests
import pandas as pd
import sqlite3
import time

def load_data_api(url, database, table_name):
    page = 1
    limit = 500
    rows = 0
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
    
        while True:
            params = {'page': page, 'limit': limit}
            response = requests.get(url,params = params,timeout=10)
            data = response.json()
            df = pd.DataFrame(data['data'])
            if len(data['data']) == 0:
                print("Данные закочились")
                break
            
            rows += df.to_sql(table_name, conn,if_exists='append', index=False)
            print(f'Прочитана страница: {page} строк: {rows}')
            time.sleep(1.0)
            page = page + 1
    print(f'Загружено страниц: {page}, строк: {rows}')

url = 'https://superbank.tryapi.ru/clients/'
load_data_api(url, 'my_database.db', 'clients')

url = 'https://superbank.tryapi.ru/accounts/'
load_data_api(url,'my_database.db', 'accounts')

url = url = 'https://superbank.tryapi.ru/payments/'
load_data_api(url,'my_database.db', 'payments')
