from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError('Parent node should have a tag')
        if self.children == None:
            raise ValueError('Children of a parent node should not be null')
        children = ''.join(map(lambda child: child.to_html(), self.children))
        return f'<{self.tag}{self.props_to_html()}>{children}</{self.tag}>'


    def props_to_html(self):
        if self.props == None:
            return ''
        return ' ' + map(lambda key: f'{key}="{self.prop[key]}"', self.props.keys()).join(' ')
