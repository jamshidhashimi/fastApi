# What is an API

API stands for Application Programming Interface and it is a way for one program to talk to another program.

# HTTP APIs

HTTP APIs (Application Programming Interfaces) are interfaces that allow communication and interaction between different software systems over the HTTP (Hypertext Transfer Protocol) protocol. They enable applications to send requests and receive responses to perform various operations, exchange data, and access resources over the internet.

```python
import urllib3

resp = urllib3.request('GET', 'https://openlibrary.org/search/authors.json?q=adam grant')
result = resp.json()
print(result)
```

Make sure you have urllib3 installed. You can install it by running the following command:
`python -m pip install urllib3`

**Formatting CLI output**

```python
import urllib3
import rich

resp = urllib3.request('GET', 'https://openlibrary.org/search/authors.json?q=adam grant')
result = resp.json()
rich.print(result)
```

Make sure you have urllib3 installed. You can install it by running the following command:
`python -m pip install rich`

# What is FastApi

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

FastAPI is designed to be a high-performance web framework for building APIs in Python. It achieves its performance through the use of two main libraries: Starlette and Pydantic.

1. Starlette: Starlette is an asynchronous web framework that provides excellent performance. It is built on top of the ASGI (Asynchronous Server Gateway Interface) specification, which allows for efficient handling of multiple requests concurrently. Starlette's design and architecture contribute to FastAPI's fast request/response cycle, making it comparable in performance to popular frameworks like Node.js and Go.

2. Pydantic: Pydantic is a data validation and serialization library. It allows you to define the structure and types of your data through Python classes with type hints. Pydantic performs data validation and conversion, ensuring that incoming requests are well-formed and conform to the specified data models. This process is highly optimized and contributes to the overall performance of FastAPI.

By leveraging the performance benefits of Starlette and Pydantic, FastAPI is considered one of the fastest Python frameworks available for building web APIs. It offers a balance of speed, developer productivity, and ease of use, making it a popular choice for high-performance Python applications.

Key features in summary:

- Fast: Very high performance. One of the fastest Python frameworks available.
- Fast to code: Increase the speed to develop features by about 200% to 300%.
- Fewer bugs: Reduce about 40% of human (developer) induced errors.
- Intuitive: Great editor support. Completion everywhere. Less time debugging.
- Easy: Designed to be easy to use and learn. Less time reading docs.
- Short: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
- Robust: Get production-ready code. With automatic interactive documentation.
- Standards-based: Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.

# Setup

`pip install "fastapi[all]"`

or, alternatively, you can do it one by one:

`pip install fastapi`

and then:

`pip install "uvicorn[standard]"`

## Why we need uvicorn?

Uvicorn is a high-performance ASGI server that is commonly used to run FastAPI applications. Here's why we need Uvicorn to run FastAPI:

- ASGI Compatibility: FastAPI is built on top of the ASGI (Asynchronous Server Gateway Interface) specification, which is an emerging standard for building Python web applications. Uvicorn is designed specifically to support ASGI, making it a suitable server for running FastAPI.

- Concurrency and Performance: Uvicorn is built using the powerful asyncio library in Python, which allows it to handle high levels of concurrency and provide excellent performance. FastAPI, being an asynchronous web framework, can take full advantage of Uvicorn's concurrency capabilities to handle multiple requests simultaneously.

- WebSocket Support: Uvicorn has built-in support for WebSockets, which are a key feature in many modern web applications. FastAPI provides WebSocket functionality, and Uvicorn allows you to seamlessly integrate and run WebSocket-enabled endpoints alongside your regular HTTP endpoints.

- Development and Production Environment: Uvicorn provides useful features for both development and production environments. It supports automatic code reloading during development, allowing you to see instant changes without restarting the server. In production, Uvicorn can be configured to handle multiple workers, enabling your FastAPI application to scale and handle a high volume of concurrent requests.

## First Example

Create a file `main.py` and write the following:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

Then run it live server:
`uvicorn main:app --reload`

The command `uvicorn main:app` refers to:

- main: the file main.py (the Python "module").
- app: the object created inside of main.py with the line app = FastAPI().
- --reload: make the server restart after code changes. Only use for development.

**See it live**
Open your browser at `http://127.0.0.1:8000` and you should see:
`{"message": "Hello World"}`

Let's see in detail on what's happening here:

1. from fastapi import FastAPI: This line imports the FastAPI class from the fastapi module. FastAPI is a framework for building APIs with Python.

2. app = FastAPI(): This line creates an instance of the FastAPI class and assigns it to the variable app. This app object will be used to define the routes and handlers for our API.

3. @app.get("/"): This is a decorator that associates the following function with the root URL ("/") of the API. In this case, it is used for handling HTTP GET requests to the root URL.

4. async def root():: This line defines an asynchronous function named root, which will handle requests to the root URL ("/").

5. return {"message": "Hello World"}: This line is the body of the root function. It returns a dictionary containing a single key-value pair: "message" as the key and "Hello World" as the value. This dictionary will be converted to JSON format and sent as the response to the client when the root URL is accessed.

**Interactive API docs**
Now go to `http://127.0.0.1:8000/docs`.

You will see the automatic interactive API documentation (provided by Swagger UI)

**Alternative API docs**
And now, go to `http://127.0.0.1:8000/redoc`.

You will see the alternative automatic documentation (provided by ReDoc)

**OpenAPI**

FastAPI generates a "schema" with all your API using the OpenAPI standard for defining APIs. OpenAPI is a specification that dictates how to define a schema of your API.

This schema definition includes your API paths, the possible parameters they take, etc. If you are curious about how the raw OpenAPI schema looks like, FastAPI automatically generates a JSON (schema) with the descriptions of all your API.

You can see it directly at: `http://127.0.0.1:8000/openapi.json`

**Path or Endpoint Operation**
"Path" here refers to the last part of the URL starting from the first `/`.

So, in a URL like:

`https://example.com/items/foo`
...the path would be:

`/items/foo`

While building an API, the "path" is the main way to separate "concerns" and "resources".

**Operation**

"Operation" here refers to one of the HTTP "methods".

When building APIs, you normally use these specific HTTP methods to perform a specific action.

Normally you use:

```
POST: to create data.
GET: to read data.
PUT: to update data.
DELETE: to delete data.
```

So, in OpenAPI, each of the HTTP methods is called an "operation".

We are going to call them "operations" too.

The `@app.get("/")` tells FastAPI that the function right below is in charge of handling requests that go to:

- the path /
- using a get operation

You can also use the other operations:

```
@app.post()
@app.put()
@app.delete()
```

## Path Parameters

You can declare path "parameters" or "variables" with the same syntax used by Python format strings:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
```

The value of the path parameter item_id will be passed to your function as the argument item_id.

**Path parameters with types**

You can declare the type of a path parameter in the function, using standard Python type annotations:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

In this case, item_id is declared to be an int.

**Data validation**
But if you go to the browser at http://127.0.0.1:8000/items/foo, you will see a nice HTTP error of:

```
{
    "detail": [
        {
            "loc": [
                "path",
                "item_id"
            ],
            "msg": "value is not a valid integer",
            "type": "type_error.integer"
        }
    ]
}
```

because the path parameter item_id had a value of "foo", which is not an int.

## Query Parameters

When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.

```python
from typing import Union
from fastapi import FastAPI

app = FastAPI()

student = {'id': 1, 'name': 'Jean', 'age': 25, 'year': '3'}


@app.get("/students/")
async def get_students(id: int, name: Union[str, None] = None):

    if id and name and student.get('id') == id and student.get('name') == name:
        return student

    if student.get('id') == id:
        return student

    if student.get('name') == name:
        return student

    return {"message": "Data not found"}
```

**Optional parameters**

The same way, you can declare optional query parameters, by setting their default to `None`.

**Required query parameters**

When you declare a default value for non-path parameters (for now, we have only seen query parameters), then it is not required.

If you don't want to add a specific value but just make it optional, set the default as None.

But when you want to make a query parameter required, you can just not declare any default value

# Resources

https://fastapi.tiangolo.com
