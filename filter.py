import re
from urllib.parse import urlparse


class Filter:
    @staticmethod
    def filter_message(message_text):
        mentions = re.findall("(@[A-Za-z0-9_]+)", message_text)
        clean_text = message_text
        for mention in mentions:
            clean_text = clean_text.replace(mention, "")
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message_text)
        for url in urls:
            parsed = urlparse(url)
            if parsed.hostname == "telegram.me" or parsed.hostname == "t.me":
                clean_text = clean_text.replace(url, "")

        return clean_text




text = '''
[Forwarded from Shams_jewelry_mirzakhani]
[ Photo ]
@shams_jewelry
✨گالری شمس
بزرگترین کلکسیون حلقهای ازدواج در ایران 

ساخت ایده و رویای شما افتخار ماست 
 https://t.me/joinchat/AAAAAD6N4PVREVsXoHiLOw


0912 8397780
021 22258193. Shams
'''


