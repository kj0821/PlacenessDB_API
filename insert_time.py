from src import dbhandler
from datetime import datetime
from src import placeontology
from src.jsonencoder import *
 
def unixtimestampToYMDHMS(timestamp):
    return datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d-%H-%M-%S')

def getWeekday (ymdhms):
    return datetime.strptime(ymdhms,'%Y-%m-%d-%H-%M-%S').strftime('%A')

def getIsWeekend(day):
    if day=="Saturday" or day=="Sunday":
        return "true"
    else:
        return "false"
    
db = dbhandler.firebase('https://placenessdb.firebaseio.com/yap')
ont = placeontology.ontology()
place_instances = db.get("")

for placeid in place_instances:
    place = place_instances[placeid]
    
    for key in place:
        instance = place[key]
        
        timestamp = instance['rawdata']['instagram']['created_time']
        ymdhms = unixtimestampToYMDHMS(timestamp)
        
        year = int(ymdhms.split('-')[0])
        month = int(ymdhms.split('-')[1])
        day = int(ymdhms.split('-')[2])
        hour = int(ymdhms.split('-')[3])
        minute = int(ymdhms.split('-')[4])
        second = int(ymdhms.split('-')[5])
        weekday = getWeekday(ymdhms)
        isWeekend = getIsWeekend(weekday)
        isHoliday = 'not sure'
        
        values_time = [timestamp, year, month, day, hour, minute, second, weekday, isWeekend, isHoliday]
        json_time = encodeJson(ont.time,values_time)
        
        db.put("/"+placeid+"/"+key+"/time", json_time) 
 