from src import dbhandler
from src import placeontology
from src.jsonencoder import *
import json

db_data = dbhandler.firebase('https://placenessdb.firebaseio.com/data/starbucks/')
db_ont = dbhandler.firebase('https://placenessdb.firebaseio.com/ontology/starbucks/')
place = placeontology.ontology()
  
  
def insertRawInput(filename):
    placeid  = filename.split("/")[3].split(":")[0]
    f = open("./" + filename, "r")
        
    for line in f:
        _raw_string = line
        _raw_string_json_acceptable = _raw_string.replace("'", "\"")
        try:
            _raw_json = json.loads(_raw_string_json_acceptable)
            try:
                db_data.put(placeid +"/instagram/"+ _raw_json['id'], json.dumps(_raw_json))
                
                vals = ["","","","",""]
                data = encodeJson(place.root, vals)
                db_ont.put(placeid +"/instagram/"+ _raw_json['id'], data)
            except:
                print ("error:", json.dumps(_raw_json))
    
        except:
            print _raw_string_json_acceptable
