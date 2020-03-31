import json
import random

#Brand name with just SmartPhone and not accessory
smartphoneBrand = ['Samsung', 'Mi', 'Coolpad', 'Nokia', 'Xifo', 'Honor', 'Redmi', 'realme', 'Vivo', 'OnePlus',
                   'Lava', 'Moto', 'Oppo','Binatone',
                   'GIGASMART', 'Huawei', 'SENIOR WORLD',
                   'XOLO', 'FORME', '10.or',
                   'iVOOMi', 'Motorola', 'Micromax', 'LG', 'MTR', 'Beetel',
                    'InFocus', 'Alcatel','Poco',
                   'Orientel', 'Lenovo', 'Ichiban', 'Apple','Xiaomi','HTC', 'Karbonn', 'Gionee', 'LYF', 'Intex']
data=[]

#To get total brand Names
def addBrand(obj):
    if not obj["Brand_name"] in smartphoneBrand:
        smartphoneBrand.append(obj["Brand_name"])


def fillRandomReview(obj):
    if obj["rating"]=="":
       obj["rating"] = float("{0:.1f}".format(random.uniform(1.0,5.0)))
    else:
        rating=obj["rating"][0:3]    #sliced through starting three digits of the rating string
        obj["rating"]= float(rating)

    #print(obj)
    return obj

#this function remove the formatting in price record and fill some price for the document with no price.
def fillRandomPrice(obj):
    price = obj["Product_price"]
    #print(obj)
    if price.find(',') == -1:
        price = str(random.randrange(3000, 20000))
    if price.find(',') != -1:
        price = price.replace(',', '')
        price = price.split(".", 1)[0]
    obj["Product_price"] = int(price)
    return obj

def addNewIdData(obj,id):
    obj['_id'] = id
    return obj

#opening json dataset
with open('amazon_phone_dataset.json', encoding="utf8") as infile:
    #parsing json data into list of dictionaries
    data = json.load(infile)  # total documents 9570
    i = 0
    currentIndex = -1
    k = 0
    j = 0
    dataCopy = data.copy()     #creating copy so that i can iterate and modify data at the same time


    for obj in dataCopy:
        currentIndex += 1
        #deleting documents with no Product Name
        if obj["Product_name"] == "":
            data.remove(obj)
            i += 1
            continue
        # deleting documents with no img_URL
        if obj["Product_img"] == "":
            data.remove(obj)
            continue
        #deleting documents with no BrandName
        if obj["Brand_name"] == "":
            data.remove(obj)
            continue
        #deleting documents with no mobile brand i.e. product is not a mobile
        if not obj["Brand_name"] in smartphoneBrand:
            data.remove(obj)
            continue

    id=0
    for obj in data:
        j+=1                      #total number of filtered records
        # updating price in required format and filling price for the documents with no price
        obj = fillRandomPrice(obj)
        # change price data type string to int
        #filling random reviews for documents with no reviews
        obj = fillRandomReview(obj)

        #adding an id to the dataset
        obj = addNewIdData(obj,id)
        id+=1
        print(obj)

    print(len(data), j,currentIndex, k)

#open file with write permission
with open('dataset.json',  'w') as outfile:
    #write json data into dataset.json file(it creates new json file)
    json.dump(data,outfile,indent=1)

print(smartphoneBrand)
