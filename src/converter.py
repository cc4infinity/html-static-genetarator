import re
from helpers_block import BlockType, markdown_to_blocks, block_to_block_type, block_to_text
from parentnode import ParentNode
from leafnode import LeafNode
from leafnode import LeafNode
from helpers import text_to_textnodes
from textnode import TextNode

def text_to_list(text, block_type):
    child_html_nodes = []
    for line in text.split('\n'):
        line_text_nodes = text_to_textnodes(line)
        line_html_nodes = list(map(lambda text_node: text_node.to_html_node(), line_text_nodes))
        child_html_nodes.append(ParentNode('li', line_html_nodes, None))
    list_tag = 'ul' if BlockType == BlockType.UNORDERED_LIST else 'ol'
    return ParentNode(list_tag, child_html_nodes)

def text_to_text_node(text, block_type):
    leaf_nodes = []
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
        html_node = node.to_html_node()
        leaf_nodes.append(html_node)
    if block_type == BlockType.PARAGRAPH:
        return ParentNode('p', leaf_nodes, None)
    if block_type == BlockType.HEADING:
        return ParentNode('h1', leaf_nodes, None)
    if block_type == BlockType.CODE:
        return ParentNode('pre', [LeafNode('code', text, None)], None)
    if block_type == BlockType.QUOTE:
        return ParentNode('blockquote', leaf_nodes, None)
    raise Exception('Bad block type in text to text node frunciton')

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    HTMLNodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        block_text = block_to_text(block, block_type)
        nodes = text_to_list(block_text, block_type) if block_type == BlockType.ORDERED_LIST or block_type == BlockType.UNORDERED_LIST else text_to_text_node(block_text, block_type)
        HTMLNodes.append(nodes)
    result = ParentNode('div', HTMLNodes)
    return result.to_html()

def extract_title(markdown):
    title_regex = r'^\# (.+)'
    result = re.findall(title_regex, markdown, flags=re.MULTILINE)
    if len(result) == 0:
        raise Exception("Ther is no title")
    return result[0]


match = """
# heh title"""
print(extract_title(match))
