import pymongo

def openMongoDB():
    client = pymongo.MongoClient('localhost',27017)
    db = client['Sina']
    collect = db['domestic']
    return collect
if __name__ == '__main__':
    collect = openMongoDB()
    collect.insert_one({"tag":"news"})
    pass