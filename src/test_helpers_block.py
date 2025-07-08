from helpers_block import markdown_to_blocks, BlockType, block_to_block_type
import unittest

class TestTextNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


    def test_markdown_to_blocks_empty(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [],
        )

    def test_block_to_block_type(self):
        heading_block = """# some cool txt
        asd
        asd"""
        code_block = """```
        some()
        coool()
        codeeee()```"""
        quote_block = """>something
>not cool"""
        non_ordered_list_block = """- one thing
- two thingsjjkkjkjkjkj"""
        ordered_list_block = """1. somethind nooo
2. some other thinhggg"""
        self.assertEqual(block_to_block_type(heading_block), BlockType.HEADING)
        self.assertEqual(block_to_block_type(code_block), BlockType.CODE)
        self.assertEqual(block_to_block_type(quote_block), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(non_ordered_list_block), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(ordered_list_block), BlockType.ORDERED_LIST)


    def test_bad_block_to_block_type(self):
        heading_block = """#some cool txt
        asd
        asd"""
        code_block = """```
        some()
        coool()
        codeeee()``"""
        quote_block = """>something
>not cool
nope"""
        non_ordered_list_block = """- one thing
- two thingsjjkkjkjkjkj
a"""
        ordered_list_block = """1. somethind nooo
3. some other thinhggg"""
        self.assertEqual(block_to_block_type(heading_block), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(code_block), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(quote_block), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(non_ordered_list_block), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(ordered_list_block), BlockType.PARAGRAPH)
