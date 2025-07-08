import unittest

from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p_complex(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_not_eq_text(self):
        node = LeafNode("div", 'no more pythonian')
        node2 = LeafNode("div", 'no more pythonian')
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
