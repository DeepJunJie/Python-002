# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Homework2Pipeline:
    def process_item(self, item, spider):
        title = item['title']
        type = item['type']
        date = item['date']
        output = f'|{title}|\t|{type}|\t|{date}|\n'
        with open('./movies.csv', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item
