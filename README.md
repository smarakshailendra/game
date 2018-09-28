# game
server game application

A web server application with two endpoints:
  Endpoint 1 (/process/*)
  
    This endpoint accepts HTTP request sent using any of the methods (GET, POST,
    PUT, DELETE) and responds back with a JSON describing the request. 
    {
        time:
        method: 
        headers: 
        path: 
        query: 
        body: 
        duration: 
    }
  
  Endpoint 2 (/stats)
  
    This endpoint responds with the following real-time statistics:
    • Total number of requests made since server startup and the average
    response time, classified by HTTP method.
    • Number of requests and average response times, in the past hour,
    classified by HTTP method
    • Number of requests and average response times, in the past minute,
    classified by HTTP method

The project is developed using python 2.7, django 1.11.x.
The third party modules are saved in requirement.txt file for pip installation.

Sqlite db is used to retain each and every requests made.

The project is hosted in an aws based vm.
The apis can be accessed with 
      host: ec2-18-222-79-220.us-east-2.compute.amazonaws.com
      port: 9061
      
Note: In case the vm is not reachable, drop me a message.
