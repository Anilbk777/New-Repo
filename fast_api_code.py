from fastapi import FastAPI
import uvicorn

app = FastAPI()
users = [
    {"name":"anil","roll no": 1,"address":"pkr"},
    {"name":"shyam","roll no":2,"address":"ktm"}
]

@app.get(" ")
def hello():
    return {"message":"Hello world"}

@app.get("/users")
def get_users():
    return users

@app.get("/user/{id}")
def get_user_by_id(ide:int):
    for user in users:
        if user['roll no'] == ide:
            return user
    return {"error":"404 User not found"}

@app.post("/user")
def create_user(user1:dict):
    try:
        users.append(user1)
        return {"message":"User added sucessfully","data":user1}

    except:
        return {"error":"Invalid user"}

if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)

