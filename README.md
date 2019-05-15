## flask-couchbase-DiaryApp   

This project shows how to build a flask-based application with a [Couchbase](https://www.couchbase.com/ server as the backend) 
server as the backend.     

## Getting Started   

Clone this repo in a virtualised environment. You can use the following commands to create virtualised environment

 `pip install virtualenv`    
 
 `mkidr directory_name`  
 
 `virtualenv projectname`    
 
 `git clone https://github.com/Rev0kz/flask-couchbase-demo.git`
 
 Install the following packages to run the app locally
 
 `pip install -r requirements.txt`  
 
 `python app.py`   
 
 
## How to Run a New Container for the Couchbase Server Image 
 
 `docker run -d --name db -p 8091-8094:8091-8094 -p 11210:11210 couchbase`
 
