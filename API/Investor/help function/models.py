from mongoengine import StringField, IntField, Document, EmbeddedDocument, ListField, EmbeddedDocumentField, FloatField,DictField

class Dwellings(Document):
    lga = StringField(required=True)
    unit = DictField()
    house = DictField()
    all = DictField()
    def __init__(self,lga,unit={},house={},all={},*args,**values):
        super().__init__(*args,**values)
        self.lga = lga
        self.unit = unit
        self.house = house
        self.all = all
