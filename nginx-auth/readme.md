# What is this
A very basic example of **authentication** and **authorization** of nginx + customapp (python) + ldap

# Structure

$docker-compose up

Now you have the following containers running:
* **ldap** exposed on host network via **1389** port.
* **ldap manager** exposed on host network via **8080** port.
* **nginx** exposed on host network via **8888** port
* custom python application (internally it binds on port 8080 and is accessed by nginx for auth requests)

# How to use
TBD
