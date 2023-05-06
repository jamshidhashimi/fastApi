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

## First Example

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```
