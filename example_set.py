from src import dbhandler
from src import placeontology
from src.jsonencoder import *
import json

############# 0. initialization ############
db = dbhandler.firebase('https://placenessdb.firebaseio.com/yap/')
place = placeontology.ontology()

############# 1. assigning place name ############
placename = "place_x"

############# 2. assigning values according to ontology ############
values_dweller = ['user1', 'girlfriend']
values_time = [1461737135, 2016, 4, 27, 15, 5, 35, "Wednesday", "false", "not sure"]
values_space = ['high traffic', 'sunny', 28]
values_activity = ['action movies', 'watch movies']
values_opinion = ['excited to watch movies']

############# 3. encoding values as json ############
json_dweller = encodeJson(place.dweller,values_dweller)
json_time = encodeJson(place.time,values_time)
json_space = encodeJson(place.space,values_space)
json_activity = encodeJson(place.activity,values_activity)
json_opinion = encodeJson(place.opinion,values_opinion)

############# 4. encoding json within json ############
json_key_values = encodeJson(place.root, [json.loads(json_dweller), json.loads(json_time), json.loads(json_space), json.loads(json_activity), json.loads(json_opinion)])
id = db.push(placename, json_key_values)

############# 5. pushing raw data ############
_raw_string = '{"user_has_liked": false, "attribution": null, "tags": [], "user": {"username": "sweetqueencaroline", "profile_picture": "https://scontent.cdninstagram.com/t51.2885-19/s150x150/12446060_974065959338535_969160479_a.jpg", "id": "328018583", "full_name": "Beth Sweet"}, "comments": {"count": 0, "data": []}, "filter": "Normal", "images": {"low_resolution": {"url": "https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12930858_1067729273287430_28234806_n.jpg?ig_cache_key=MTIxNzg5NTU1NTk1NDkwMTA4OQ%3D%3D.2.l", "width": 320, "height": 320}, "thumbnail": {"url": "https://scontent.cdninstagram.com/t51.2885-15/s150x150/e35/c135.0.809.809/12724699_581850808656892_874956096_n.jpg?ig_cache_key=MTIxNzg5NTU1NTk1NDkwMTA4OQ%3D%3D.2.c", "width": 150, "height": 150}, "standard_resolution": {"url": "https://scontent.cdninstagram.com/t51.2885-15/s640x640/sh0.08/e35/12930858_1067729273287430_28234806_n.jpg?ig_cache_key=MTIxNzg5NTU1NTk1NDkwMTA4OQ%3D%3D.2.l", "width": 640, "height": 640}}, "link": "https://www.instagram.com/p/BDm1Y4yOABh/", "location": {"latitude": 40.7142, "name": "New York, New York", "longitude": -74.0064, "id": 212988663}, "created_time": "1459404485", "users_in_photo": [], "caption": {"created_time": "1459404485", "text": "Bright lights", "from": {"username": "sweetqueencaroline", "profile_picture": "https://scontent.cdninstagram.com/t51.2885-19/s150x150/12446060_974065959338535_969160479_a.jpg", "id": "328018583", "full_name": "Beth Sweet"}, "id": "1217895560316978109"}, "type": "image", "id": "1217895555954901089_328018583", "likes": {"count": 0, "data": []}}'
#.replace(' false,',' False,').replace(' null,', 'None')
_raw_string_json_acceptable = _raw_string.replace("'", "\"")
_raw_json = json.loads(_raw_string_json_acceptable)
db.put(placename+"/"+id+"/rawdata", encodeJson(["instagram"],[_raw_json]))