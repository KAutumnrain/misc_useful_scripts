# J2X-Shifter
Does what it says on the tin

---

This is specifically designed for a docker deployment, as flask by itself is specifically a production configuration.
If you decide to deploy this in production without it, gunicorn won't fire without some modification to the base script!

---
The total project requirements are as follows:

- Python 3.9+ (3.10 is preferred)
- Flask 2.2.2
- Gunicorn 20.1.0
- defusedxml 0.7.1
- json2xml 3.19.5

These version numbers should remain the same. Due to licensing I cannot provide
these wheels, but I highly recommend forking and compiling each to prevent
supply chain attacks. Also, please support the devs of each package if possible.

---

It's a fairly minimal flask-based JSON to XML format shifter. 
The idea was making it lightweight and somewhat secure. 


This version of the shifter is barebones to facilitate
building out middleware, intended to perform transfers of JSON info to legacy
endpoints that require XML-formatted documents.





Operation Flow
---
Operationally, the script takes in a request with the
```application/json``` content type and returns an XML translated
response. There are no file operations here, so the response should just end up being a 200 with the XML content attached.

Current Operation Flow:
![image](https://user-images.githubusercontent.com/101837956/193079003-b0c2b797-e4d0-4a46-826d-7350417efbf8.png)

Intended Operation Flow:
![image](https://user-images.githubusercontent.com/101837956/193079213-a7d9e0e1-8ad8-47bf-97c3-252436dcc7e5.png)

