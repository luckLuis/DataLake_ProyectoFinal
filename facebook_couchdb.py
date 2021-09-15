#!/usr/bin/env python
# coding: utf-8

# In[2]:

#librerias
from facebook_scraper import get_posts
import couchdb
import json
import time


# In[3]:

#creacion de base de datos y conexion con couchdb
couch=couchdb.Server('http://sebas:18102412@127.0.0.1:5984')
db=couch.create('steam')
nombredb='steam'
db=couch[nombredb]


# In[4]:

#recopilacion de datos
i=1
for post in get_posts('Steam', pages=1000, extra_info=True):
    print(i)
    i=i+1
    time.sleep(5)
    
    id=post['post_id']
    doc={}
     
    doc['id']=id
    
    mydate=post['time']
    
    try:
        doc['texto']=post['text']
        doc['date']=mydate.timestamp()
        doc['likes']=post['likes']
        doc['comments']=post['comments']
        doc['shares']=post['shares']
        try:
            doc['reactions']=post['reactions']
        except:
            doc['reactions']={}

        doc['post_url']=post['post_url']
        db.save(doc)

    
        print("guardado")

    except Exception as e:    
        print("no se pudo grabar:" + str(e))





