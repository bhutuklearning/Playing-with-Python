

### Just Some Info
Here I aim to build my own version of web framework{for backend} like FastAPI.

In the initial stage I would love to build the first get and post request server, then I will integrate (Put)Update and Delete method.
It will be a HTTP server. The API will be a rest API, as of now what I am thinking of.


## 1) Setup (Windows)
1. Create venv:
   ```powershell
   python -m venv venv
   ```
2. Activate venv:
   ```powershell
   venv\Scripts\activate
   ```

What is Happening in Backend?
    Browser sends HTTP request
    Server listens on port
    Server parses request
    Server finds matching route
    Executes function
    Sends HTTP response


## Lets build the version 1 
#### Version 1
In version GET and POST Request will be supported.
I will be learning and implementing decorators, route registration and JSON response.
After that proceeding towards basic request parsing and then running on localhost server.

### Technology used
Standard python library socket and json.
