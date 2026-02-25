# You shouldn't change  name of function or their arguments
# ,but you can change content of the initial functions.
import json as js
import sys
from argparse import ArgumentParser
from typing import List, Optional, Sequence
import requests
import xml.etree.ElementTree as ET


class UnhandledException(Exception):
    pass

def get_text(parent, tag):
    element_primary = parent.find(tag)
    element = element_primary.text if element_primary is not None else None
    return element

def get_all_text(parent, tag):
    result = []
    elements_primary = parent.findall(tag)
    for element in elements_primary:
        if element.text is not None:
            result.append(element.text)
    return result

def remove_empty(data:dict) -> dict:
    result = {}
    for key, value in data.items():
        if value is not None and value != []:
            result[key] = value
    return result

def rss_parser(
    xml: str,
    limit: Optional[int] = None,
    json: bool = False,
) -> List[str]:
    """
    RSS parser.

    Args:
        xml: XML document as a string.
        limit: Number of the news to return. if None, returns all news.
        json: If True, format output as JSON.

    Returns:
        List of strings.
        Which then can be printed to stdout or written to file as a separate lines.

    Examples:
        >> xml = '<rss><channel><title>Some RSS Channel</title><link>https://some.rss.com</link><description>Some RSS Channel</description></channel></rss>'
        >> rss_parser(xml)
        ["Feed: Some RSS Channel",
        "Link: https://some.rss.com"]
        >> print("\\n".join(rss_parser(xmls)))
        Feed: Some RSS Channel
        Link: https://some.rss.com
    """
    # Your code goes here
    root = ET.fromstring(xml)

    channel = root.find("channel")
    if channel is None:
        return []

    channel_data = {}
    title_channel = get_text(channel, "title")
    link_channel = get_text(channel, "link")
    last_build_date_channel = get_text(channel, "lastBuildDate")
    pub_date_channel = get_text(channel, "pubDate")
    language_channel = get_text(channel, "language")
    managing_editor_channel = get_text(channel, "managingEditor")
    description_channel = get_text(channel, "description")
    categories_channel = get_all_text(channel, "category")

    channel_data = {
        "title": title_channel,
        "link": link_channel,
        "lastBuildDate": last_build_date_channel,
        "pubDate": pub_date_channel,
        "language": language_channel,
        "managingEditor": managing_editor_channel,
        "description": description_channel,
        "category": categories_channel,
    }

    ### return result preparation
    result = []
    if title_channel:
        result.append(f"Feed: {title_channel}")
    if link_channel:
        result.append(f"Link: {link_channel}")
    if last_build_date_channel:
        result.append(f"Last Build Date: {last_build_date_channel}")
    if pub_date_channel:
        result.append(f"Publish Date: {pub_date_channel}")
    if language_channel:
        result.append(f"Language: {language_channel}")
    if categories_channel:
        result.append(f"Categories: {', '.join(categories_channel)}")
    if managing_editor_channel:
        result.append(f"Editor: {managing_editor_channel}")
    if description_channel:
        result.append(f"Description: {description_channel}")


    #### Items Part ######

    items = channel.findall("item")

    if limit is not None:
        items = items[:limit]

    items_data = [] # list of all dictionaries of items details
    for item in items:
        item_data = {
            "title": get_text(item, "title"),
            "author": get_text(item, "author"),
            "pubDate": get_text(item, "pubDate"),
            "link": get_text(item, "link"),
            "category": get_all_text(item, "category"),
            "description": get_text(item, "description"),
        }
        items_data.append(item_data)

    # if items_data:
    #     result.append("")
    for item in items_data:
        result.append("")
        if item["title"]:
            result.append(f"Title: {item['title']}")
        if item["author"]:
            result.append(f"Author: {item['author']}")
        if item["pubDate"]:
            result.append(f"Publish Date: {item['pubDate']}")
        if item["link"]:
            result.append(f"Link: {item['link']}")
        if item["category"]:
            result.append(f"Categories: {', '.join(item['category'])}")
        if item["description"]:
            result.append("")
            result.append(item['description'])



    # Json output preparation
    # json_channel = {}
    # # only required fields when json type
    # if title_channel:
    #     json_channel['title'] = title_channel
    # if link_channel:
    #     json_channel['link'] = link_channel
    # if description_channel:
    #     json_channel['description'] = description_channel
    # if categories_channel:
    #     json_channel['category'] = categories_channel

    non_null_channel_data = remove_empty(channel_data)

    non_null_items_data = [remove_empty(item) for item in items_data]

    final_data = non_null_channel_data
    if non_null_items_data:
        final_data["items"] = non_null_items_data

    json_str = js.dumps(final_data, indent=2)

    if json:
        return [json_str]
    else:
        return result


def main(argv: Optional[Sequence] = None):
    """
    The main function of your task.
    """
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader.",
    )
    parser.add_argument("source", help="RSS URL", type=str, nargs="?")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true"
    )
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided", type=int
    )

    args = parser.parse_args(argv)
    xml = requests.get(args.source).text
    try:
        print("\n".join(rss_parser(xml, args.limit, args.json)))
        return 0
    except Exception as e:
        raise UnhandledException(e)


if __name__ == "__main__":
    main()
    # xml = """
    # <rss>
    #   <channel>
    #     <title>Test Feed</title>
    #     <link>https://example.com</link>
    #     <lastBuildDate>Mon, 01 Jan 2024</lastBuildDate>
    #     <pubDate>Sun, 31 Dec 2023</pubDate>
    #     <language>en</language>
    #     <category>Tech</category>
    #     <category>News</category>
    #     <managingEditor>editor@example.com</managingEditor>
    #     <description>Test description</description>
    #     <item>
    #         <title>Item 1</title>
    #         <description>A</description>
    #         <category>Tech</category>
    #         <category>News</category>
    #     </item>
    #   </channel>
    # </rss>
    # """

    # xml = """
    # <rss>
    #   <channel>
    #     <title>Feed</title>
    #     <link>https://example.com</link>
    #     <description>Desc</description>
    #     <item><title>Item 1</title><description>A</description></item>
    #     <item><title>Item 2</title><description>B</description></item>
    #     <item><title>Item 3</title><description>C</description></item>
    #   </channel>
    # </rss>
    # """
    # xml = """
    # <rss>
    #   <channel>
    #     <title>Tom &amp; Jerry</title>
    #     <link>https://example.com</link>
    #     <description>It&#39;s great</description>
    #   </channel>
    # </rss>
    # """
    out = rss_parser(xml, json=True)
    print("\n".join(out))