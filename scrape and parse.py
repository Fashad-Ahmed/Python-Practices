from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/dionysus"
html_page = urlopen(url)
html_text = html_page.read().decode("utf-8")

for tag in ["Name: ", "Favorite animal: "]:
    tag_start = html_text.find(tag) + len(tag)
    tag_end = html_text[tag_start:].find("<")

    # Remove extra spaces and newline padding
    print(html_text[tag_start : tag_start + tag_end].strip(" \n"))

for tag in ["Name: .*?[\n<]", "Favourite Color: .*?[\n<]"]:
    match_results = re.search(tag, html_text)

    # remove label from first result
    result = re.sub(".*: ", "", match_results.group())

    print(result)
    print(result.strip(" \n<"))
