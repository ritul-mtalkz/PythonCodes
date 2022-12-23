from pymongo import MongoClient
def get_database():
    client = MongoClient()
    client = MongoClient("mongodb://localhost:27017/")
    db = client.userData
    collection_names = db.user
    return collection_names

def login(collection_names):
    name = input("Enter Name: ")
    phone = input("Enter mobile number: ")
    email = ""
    while(email == ""):
        email = input("Enter email: ")
        for i in collection_names.find():
            if(email == i["Email"] or phone == i['Phone']):
                print("Email Already Exist")
                email = ""            
    data = {
        "Name": name,
        "Email": email,
        "Phone": phone 
    }
    print(data)
    collection_names.insert_one(data)

def signUp(collection_names):
    email = input("Enter email: ")
    phone = input("Enter mobile number: ")
    for collection_name in collection_names.find():
        if(email == collection_name["Email"] and phone == collection_name["Phone"]):
            print("User Successful Login")
            print("User Name: ", collection_name["Name"])
            return
    print("User Not Found")

def choose():
    print("-------------Press 0 for Exit---------------------")
    print("-------------Press 1 for Registration-------------")
    print("-------------Press 2 for Login--------------------")
    choose = int(input())
    return choose

ch = choose()
while(ch!=0):
    colName = get_database()
    if(ch == 1):
        login(colName) 
        ch = choose()   
    if(ch == 2):
        signUp(colName)
        ch = choose()
