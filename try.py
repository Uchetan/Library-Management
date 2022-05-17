import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
colle=client['circket']
dm=colle['92712']
all_record = dm.find()
lis={}
for idx, record in enumerate(all_record):
    lis[idx]=  record
print(lis)
print(lis[0]['_id'])
for i in lis:
    print(lis[i])