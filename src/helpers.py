import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            split_text = node.text.split(delimiter)
            index = 0
            for text in split_text:
                if index % 2 == 0:
                    result.append(TextNode(text, TextType.TEXT))
                else:
                    result.append(TextNode(text, text_type))
                index += 1
        else:
            result.append(node)
    return result


def extract_markdown_images(text):
    image_regex = r'!\[(.*?)\]\((.*?)\)'
    return re.findall(image_regex, text)

def extract_markdown_links(text):
    link_regex = r'\[(.*?)\]\((.*?)\)'
    return re.findall(link_regex, text)

def split_nodes_image(texts):
    result = []
    for text in texts:
        if text.text_type != TextType.TEXT:
            result.append(text)
            continue
        image_regex = r'!\[(.*?)\]\((.*?)\)'
        clear_image_regex = r'!\[.*?\]\(.*?\)'
        images = extract_markdown_images(text.text)
        texts = re.split(clear_image_regex, text.text)
        for i in range(len(images) + len(texts)):
            if i % 2 == 0:
                if texts[i // 2] != '':
                    result.append(TextNode(texts[i // 2], TextType.TEXT))
            else:
                result.append(TextNode(images[i // 2][0], TextType.IMAGE, images[i // 2][1]))
    return result
            
def split_nodes_link(texts):
    result = []
    for text in texts:
        if text.text_type != TextType.TEXT:
            result.append(text)
            continue
        link_regex = r'\[(.*?)\]\((.*?)\)'
        clear_link_regex = r'\[.*?\]\(.*?\)'
        links = extract_markdown_links(text.text)
        texts = re.split(clear_link_regex, text.text)
        for i in range(len(links) + len(texts)):
            if i % 2 == 0:
                if texts[i // 2] != '':
                    result.append(TextNode(texts[i // 2], TextType.TEXT))
            else:
                result.append(TextNode(links[i // 2][0], TextType.LINK, links[i // 2][1]))
    return result

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    result = split_nodes_delimiter([node], "**", TextType.BOLD)
    result = split_nodes_delimiter(result, "_", TextType.ITALIC)
    result = split_nodes_delimiter(result, "`", TextType.CODE)
    result = split_nodes_image(result)
    result = split_nodes_link(result)
    return result
