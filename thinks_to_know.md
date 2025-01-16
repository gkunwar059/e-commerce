### Pydantic's `exclude_unset=True` Behavior

- **Without `exclude_unset=True`**: All fields, including unset ones (those with default values), are included in the dictionary.  
  Example: `{'name': 'John Doe', 'email': 'john.doe@example.com', 'phone_number': None}`  

- **With `exclude_unset=True`**: Only fields explicitly set or changed by the user are included in the dictionary.  
  Example: `{'name': 'John Doe', 'email': 'john.doe@example.com'}`



### CRUD `put and patch` Behavior
  -When to Use Which?:
    -Use PUT when the client has the complete data for the resource and wants to replace it entirely.
    -Use PATCH when updating specific fields without touching the rest of the resource.

  -The PUT method is designed to replace the entire resource

  --Use PATCH for partial updates,

  ***If improperly implemented: It may work like a PATCH (only updating the name field), which breaks RESTful principles.

##EXAMPLE:
  -Use PATCH for partial updates, where only specified fields are modified:
    PATCH /users/1
  {
    "name": "Jane Doe"
  }

  -Use PUT only when you're providing the entire resource.


##IMPORTANT --RESTAPI-RESFUL:
--MY QUESTION:
---RESTful
rest this all are the standard concept where the rules are set to perform this one is work will like this right ? yes or no ?

ANSWER:
Yes, 
- **RESTful concepts are a set of standards or guidelines designed to structure and organize how APIs interact with resources over # HTTP. - - **These -standards ensure consistency, scalability, and ease of understanding in API design.
-**REST (Representational State Transfer) defines rules and principles for:
-**REST (Representational State Transfer) defines rules and principles for:
-**REST (Representational State Transfer) defines rules and principles for:
-**How resources are represented (e.g., JSON, XML).
-**Which HTTP methods to use for specific operations:
-**GET: Retrieve data.
-**POST: Create resources.
-**PUT: Replace resources.
-**PATCH: Partially update resources.
-**DELETE: Remove resources.
-**Statelessness: Each request contains all the information needed to process it.
-**Resource Identification: Using URIs to identify resources.
-**In essence, RESTful APIs follow these rules to maintain clarity, predictability, and adherence to web standards