from mongoengine import StringField, IntField, Document, EmbeddedDocument, ListField, EmbeddedDocumentField, FloatField,DictField
'''
class Rent_Details(EmbeddedDocument):
    quarter1_2005 = IntField(required=False)
    quarter2_2005 = IntField(required=False)
    quarter3_2005 = IntField(required=False)
    quarter4_2005 = IntField(required=False)

    quarter1_2006 = IntField(required=False)
    quarter2_2006 = IntField(required=False)
    quarter3_2006 = IntField(required=False)
    quarter4_2006 = IntField(required=False)

    quarter1_2007 = IntField(required=False)
    quarter2_2007 = IntField(required=False)
    quarter3_2007 = IntField(required=False)
    quarter4_2007 = IntField(required=False)

    quarter1_2008 = IntField(required=False)
    quarter2_2008 = IntField(required=False)
    quarter3_2008 = IntField(required=False)
    quarter4_2008 = IntField(required=False)

    quarter1_2009 = IntField(required=False)
    quarter2_2009 = IntField(required=False)
    quarter3_2009 = IntField(required=False)
    quarter4_2009 = IntField(required=False)

    quarter1_2010 = IntField(required=False)
    quarter2_2010 = IntField(required=False)
    quarter3_2010 = IntField(required=False)
    quarter4_2010 = IntField(required=False)

    quarter1_2011 = IntField(required=False)
    quarter2_2011 = IntField(required=False)
    quarter3_2011 = IntField(required=False)
    quarter4_2011 = IntField(required=False)

    quarter1_2012 = IntField(required=False)
    quarter2_2012 = IntField(required=False)
    quarter3_2012 = IntField(required=False)
    quarter4_2012 = IntField(required=False)

    quarter1_2013 = IntField(required=False)
    quarter2_2013 = IntField(required=False)
    quarter3_2013 = IntField(required=False)
    quarter4_2013 = IntField(required=False)

    quarter1_2014 = IntField(required=False)
    quarter2_2014 = IntField(required=False)
    quarter3_2014 = IntField(required=False)
    quarter4_2014 = IntField(required=False)

    quarter1_2015 = IntField(required=False)
    quarter2_2015 = IntField(required=False)
    quarter3_2015 = IntField(required=False)
    quarter4_2015 = IntField(required=False)

    quarter1_2016 = IntField(required=False)
    quarter2_2016 = IntField(required=False)
    quarter3_2016 = IntField(required=False)
    quarter4_2016 = IntField(required=False)
    def __init__(self,quarter1_2005,quarter2_2005,quarter3_2005,quarter4_2005,quarter1_2006,quarter2_2006,quarter3_2006,quarter4_2006,
                 quarter1_2007,quarter2_2007,quarter3_2007,quarter4_2007,quarter1_2008,quarter2_2008,quarter3_2008,quarter4_2008,
                 quarter1_2009,quarter2_2009,quarter3_2009,quarter4_2009,quarter1_2010,quarter2_2010,quarter3_2010,quarter4_2010,
                 quarter1_2011,quarter2_2011,quarter3_2011,quarter4_2011,quarter1_2012,quarter2_2012,quarter3_2012,quarter4_2012,
                 quarter1_2013,quarter2_2013,quarter3_2013,quarter4_2013,quarter1_2014,quarter2_2014,quarter3_2014,quarter4_2014,
                 quarter1_2015,quarter2_2015,quarter3_2015,quarter4_2015,quarter1_2016,quarter2_2016,quarter3_2016,quarter4_2016,*args,**kwargs):

        super().__init__(*args, **kwargs)

        self.quarter1_2005 = quarter1_2005
        self.quarter2_2005 = quarter2_2005
        self.quarter3_2005 = quarter3_2005
        self.quarter4_2005 = quarter4_2005

        self.quarter1_2006 = quarter1_2006
        self.quarter2_2006 = quarter2_2006
        self.quarter3_2006 = quarter3_2006
        self.quarter4_2006 = quarter4_2006

        self.quarter1_2007 = quarter1_2007
        self.quarter2_2007 = quarter2_2007
        self.quarter3_2007 = quarter3_2007
        self.quarter4_2007 = quarter4_2007

        self.quarter1_2008 = quarter1_2008
        self.quarter2_2008 = quarter2_2008
        self.quarter3_2008 = quarter3_2008
        self.quarter4_2008 = quarter4_2008

        self.quarter1_2009 = quarter1_2009
        self.quarter2_2009 = quarter2_2009
        self.quarter3_2009 = quarter3_2009
        self.quarter4_2009 = quarter4_2009

        self.quarter1_2010 = quarter1_2010
        self.quarter2_2010 = quarter2_2010
        self.quarter3_2010 = quarter3_2010
        self.quarter4_2010 = quarter4_2010

        self.quarter1_2011 = quarter1_2011
        self.quarter2_2011 = quarter2_2011
        self.quarter3_2011 = quarter3_2011
        self.quarter4_2011 = quarter4_2011

        self.quarter1_2012 = quarter1_2012
        self.quarter2_2012 = quarter2_2012
        self.quarter3_2012 = quarter3_2012
        self.quarter4_2012 = quarter4_2012

        self.quarter1_2013 = quarter1_2013
        self.quarter2_2013 = quarter2_2013
        self.quarter3_2013 = quarter3_2013
        self.quarter4_2013 = quarter4_2013

        self.quarter1_2014 = quarter1_2014
        self.quarter2_2014 = quarter2_2014
        self.quarter3_2014 = quarter3_2014
        self.quarter4_2014 = quarter4_2014

        self.quarter1_2015 = quarter1_2015
        self.quarter2_2015 = quarter2_2015
        self.quarter3_2015 = quarter3_2015
        self.quarter4_2015 = quarter4_2015

        self.quarter1_2016 = quarter1_2016
        self.quarter2_2016 = quarter2_2016
        self.quarter3_2016 = quarter3_2016
        self.quarter4_2016 = quarter4_2016
class Sale_Details(EmbeddedDocument):
    year_2005 = IntField(required=False)
    year_2006 = IntField(required=False)
    year_2007 = IntField(required=False)
    year_2008 = IntField(required=False)
    year_2009 = IntField(required=False)
    year_2010 = IntField(required=False)
    year_2011 = IntField(required=False)
    year_2012 = IntField(required=False)
    year_2013 = IntField(required=False)
    year_2014 = IntField(required=False)
    year_2015 = IntField(required=False)
    year_2016 = IntField(required=False)
    def __init__(self,year_2005,year_2006,year_2007,year_2008,year_2009,year_2010,year_2011,year_2012,year_2013,year_2014,year_2015,year_2016,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.year_2005 = year_2005
        self.year_2006 = year_2006
        self.year_2007 = year_2007
        self.year_2008 = year_2008
        self.year_2009 = year_2009
        self.year_2010 = year_2010
        self.year_2011 = year_2011
        self.year_2012 = year_2012
        self.year_2013 = year_2013
        self.year_2014 = year_2014
        self.year_2015 = year_2015
        self.year_2016 = year_2016
class Return_Rate(EmbeddedDocument):
    year_2006 = FloatField(required=False)
    year_2007 = FloatField(required=False)
    year_2008 = FloatField(required=False)
    year_2009 = FloatField(required=False)
    year_2010 = FloatField(required=False)
    year_2011 = FloatField(required=False)
    year_2012 = FloatField(required=False)
    year_2013 = FloatField(required=False)
    year_2014 = FloatField(required=False)
    year_2015 = FloatField(required=False)
    year_2016 = FloatField(required=False)
    def __init__(self,year_2006,year_2007,year_2008,year_2009,year_2010,year_2011,year_2012,year_2013,year_2014,year_2015,year_2016,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.year_2006 = year_2006
        self.year_2007 = year_2007
        self.year_2008 = year_2008
        self.year_2009 = year_2009
        self.year_2010 = year_2010
        self.year_2011 = year_2011
        self.year_2012 = year_2012
        self.year_2013 = year_2013
        self.year_2014 = year_2014
        self.year_2015 = year_2015
        self.year_2016 = year_2016
class Details(EmbeddedDocument):
    one_rent=DictField(EmbeddedDocumentField(Rent_Details))
    two_rent=DictField(EmbeddedDocumentField(Rent_Details))
    three_rent=DictField(EmbeddedDocumentField(Rent_Details))
    four_rent=DictField(EmbeddedDocumentField(Rent_Details))
    all_rent=DictField(EmbeddedDocumentField(Rent_Details))
    sales=DictField(EmbeddedDocumentField(Sale_Details))
    return_rate=DictField(EmbeddedDocumentField(Return_Rate))
    def __init__(self,one_rent={},two_rent={},three_rent={},four_rent={},all_rent={},sales={},return_rate={},*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.one_rent = one_rent
        self.two_rent = two_rent
        self.three_rent = three_rent
        self.four_rent = four_rent
        self.all_rent = all_rent
        self.sales = sales
        self.return_rate = return_rate
'''
class Dwellings(Document):
    # lga=StringField(required=True,primary_key=True)
    # unit=DictField(EmbeddedDocumentField(Details))
    # house=DictField(EmbeddedDocumentField(Details))
    # all=DictField(EmbeddedDocumentField(Details))

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
