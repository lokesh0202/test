// importing 

import pymongo
import cgi

// reading htmlpage

form=cgi.FieldStorage()

// reading htmlpage constant

getname=form.getValue("fullname")

// inserting in document
Client=pymongo.MongoClient()
db=Client.test
db.person.remove({'name':getname})
