from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() #create an instance of fastAPI

# The app instance is the main component of our fastAPI application. It is used to configure the application.

class Custom(BaseModel):
    name: str
    age:int

@app.get("/ping")  # /ping is the path of endpoint.   " @app IS A DECORATOR used to define an endpoint."
async def root():
    return {"message": "Hello World"}


@app.get("/")
async def root():
    return{"message": "welcome"}


# @app.get("/blogs/{blog_id}")
# async def read_blog(blog_id : int):
#     return {"blog_id": blog_id}     # ouput => {"blog_id":"2"}   , after add int output => {"blog_id":2}


@app.get("/blogs/comments")
async def read_blog_comments():
    return {"comments" : "no comment yet!"}    # here this gives error because we write it below above api in above /blogs/id here we take id and when we go to /blogs/comments it take comments as a id and give error to solve this we write this api before the above api.



@app.post("/blogs/{blog_id}")
async def read_blog(blog_id : int , request_body: Custom, q : str = None , name : str = " "):
    print(request_body) # output in terminal => name='simar' age=23  , because we send name and age in request thought postman in json format.
    print(q , name)   #output in terminal =>
                      # INFO: 127.0.0.1:49441 - "GET /blogs/123?q=simar HTTP/1.1" 200 OK
                      # simar singh
                      #INFO: 127.0.0.1:55533 - "GET /blogs/123?q=simar&name=singh HTTP/1.1" 200 OK

    return {"blog_id": blog_id}                  # now above problem solve ..