
import re






class Filter:
    @staticmethod
    def filter_message(message_text):
        urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', message_text)
        mentions = re.findall("(@[A-Za-z0-9_]+)", message_text)
        clean_text = message_text
        for mention in mentions:
            clean_text = clean_text.replace(mention, "")
        for url in urls:
            clean_text = clean_text.replace(url, "")

        return clean_text




text = '''[Forwarded from کوی‌ستان]
[ Photo ]
نقییییییییی!

نهار #رزرو نکردمههههههههه!

http://dining.ut.ac.ir/

@Kooyestan | #دانشگاه_تهران'''


#print(Filter.filter_message(text))
