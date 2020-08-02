# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class TestUseproxyPipeline:
    def process_item(self, item, spider):
        conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='user1',
            passwd='12345678',
            db='testdb',
            charset='utf8'
        )
        cursor = conn.cursor()  
        title = item['title']
        myip = item['myip']
        insert_sql = 'INSERT INTO crawl_myip(title_name, ip_addr) VALUES (%s, %s)'
        cursor.execute(insert_sql, (title, myip))
        conn.commit()	
        cursor.close()	
        conn.close()

        return item
