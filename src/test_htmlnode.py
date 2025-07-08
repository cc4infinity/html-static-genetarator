
import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", 'Cool Value')
        node2 = HTMLNode("div", 'Cool Value')
        self.assertEqual(node, node2)

    def test_not_eq_tag(self):
        node = HTMLNode("div", 'Cool Value', [], {})
        node2 = HTMLNode("p", 'Cool Value', [], {})
        self.assertNotEqual(node, node2)

    def test_not_eq_text(self):
        node = HTMLNode("div", 'Cool Value', [], {})
        node2 = HTMLNode("div", 'Other Value', [], {})
        self.assertNotEqual(node, node2)
    
if __name__ == "__main__":
    unittest.main()
