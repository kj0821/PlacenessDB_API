from src import dbhandler
from src import placeontology
from src.jsonencoder import *
import json

db = dbhandler.firebase('https://placenessdb.firebaseio.com/yap/')
place = placeontology.ontology()

def insertRawInput(filename):
    placename = filename.split(":")[0]
    f = open("./" + filename, "r")
        
        for line in f:
            _raw_string = line
            _raw_string_json_acceptable = _raw_string.replace("'", "\"")
            try:
                _raw_json = json.loads(_raw_string_json_acceptable)
                
                vals = ["","","","",""]
                data = encodeJson(place.root, vals)
                id = db.push(placename, data)
                try:
                    db.put(placename+"/"+id+"/rawdata", encodeJson(["instagram"],[_raw_json]))
                except:
                    print ("error:", encodeJson(["instagram"],[_raw_json]))
        
        except:
            print _raw_string_json_acceptable

insertRawInput("1024513679:2016-05-13 19:17:38.txt")