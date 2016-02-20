
// importing 

import pymongo
import cgi

// reading htmlpage

form=cgi.FieldStorage()
// reading htmlpage constant
getname=form.getValue("fullname")
getnumber=form.getValue("number")
getemail=form.getValue("email")

// inserting in document
Client=pymongo.MongoClient()
db=Client.test
db.person.insert({'name':getname} ,{'phonenumber':getnumber},{'email':getemail})
