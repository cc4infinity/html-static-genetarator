from parentnode import ParentNode
from enum import Enum
from leafnode import LeafNode

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordersd_list"

def markdown_to_blocks(markdown):
    lines = markdown.split('\n\n')
    stripped_lines = map(lambda line: line.strip(), lines)
    result = filter(lambda line: len(line) > 0, stripped_lines)
    return list(result)

def block_to_block_type(block):
    if block.startswith("# "):
        return BlockType.HEADING
    if block.startswith("```") and block[-3:] == "```":
        return BlockType.CODE
    lines = block.split('\n')
    non_quotes = list(filter(lambda line: not line.startswith(">"), lines))
    if len(non_quotes) == 0:
        return BlockType.QUOTE

    non_ordered_list_item = list(filter(lambda line: not line.startswith("- "), lines))
    if len(non_ordered_list_item) == 0:
        return BlockType.UNORDERED_LIST

    is_ordered_list = True
    for i in range(len(lines)):
        if not lines[i].startswith(f"{i + 1}. "):
            is_ordered_list = False
            break
    if (is_ordered_list):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

def block_to_text(block, block_type):
    if block_type == BlockType.HEADING:
        return block[2:]
    if block_type == BlockType.CODE:
        return block[4:-3]
    if block_type == BlockType.QUOTE:
        return '\n'.join(list(map(lambda line: line[2:], block.split('\n'))))
    if block_type == BlockType.UNORDERED_LIST:
        return '\n'.join(list(map(lambda line: line[2:], block.split('\n'))))
    if block_type == BlockType.ORDERED_LIST:
        return '\n'.join(list(map(lambda line: line[3:], block.split('\n'))))
    return block
    
