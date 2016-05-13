import src

############# 0. initialization ############
db = dbhandler.firebase('https://placenessdb.firebaseio.com/yap/')

############# 1. fetching data on "place_1" ############
place_instances = db.get("place_1")

############# 2. accessing values of each posts ############
for key in place_instances:
    instance = place_instances[key]
    activity = instance['activity']
    dweller = instance['dweller']
    opinion = instance['opinion']
    rawdata = instance['rawdata']
    space = instance['space']
    time = instance['time']
    
    print "time:", time
    print "activity:", activity
    print "dweller:", dweller
    print "opinion:", opinion
    print "space:", space
    #print "rawdata:", rawdata
    
