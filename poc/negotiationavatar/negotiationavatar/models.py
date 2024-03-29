
from neomodel import StructuredNode, StringProperty, DateProperty

class Book(StructuredNode):
    title = StringProperty(unique_index=True)
    published = DateProperty()