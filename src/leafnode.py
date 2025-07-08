from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, [], props)

    def to_html(self):
        if (self.value == None):
            raise ValueError('All leaf nodes must have a value')
        if (self.tag == None):
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def props_to_html(self):
        if self.props == None:
            return ''
        return ' ' + ' '.join(map(lambda key: f'{key}="{self.props[key]}"', self.props.keys()))

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.props})'

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value
