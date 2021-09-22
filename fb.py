from facebook_scraper import get_posts

page_name = input("Please enter page name: ")

page_number = int(input("How many pages would you like to scrape: "))

for post in get_posts(page_name, pages=page_number):
    print(post['text'])
    print("------")
