# AirBnB Clone Project Repository
##### The AirBnB clone project starts now until… the end of our first year. The goal of the project is to deploy on our server a simple copy of the AirBnB website. We won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.
## General
- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

`First step:` We Wrote a command interpreter to manage our AirBnB objects.

##### This was the first step towards building our first full web application: the AirBnB clone. This first step was very important because we used what we built during this project with all other projects projects that followed: HTML/CSS templating, database storage, API, front-end integration…

#### Each task is linked and has helped us to:
- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of our instances.
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine.

## Authors
|Isaac Phiri|
|Rency Ngina|
