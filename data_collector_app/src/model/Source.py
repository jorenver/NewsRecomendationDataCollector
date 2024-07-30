import mongoengine as me

class Source(me.Document):
    name = me.StringField(required=True)
    description = me.StringField(required=True)
    url = me.StringField(required=True)
    category = me.StringField(required=False)


    meta = {
        'collection': 'sources'
    }