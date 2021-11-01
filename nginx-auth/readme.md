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
access the nginx via: http://localhost:8888/

you'll see a POC interface with links to token generation.

Note: Ldap has 2 users: user1 (in administrators group) and user2 (simple user).

* generate a token for user1 or user2
* invoke some curl requests to /admin or /zuzu

user1 should have access to both /admin and /zuzu

user2 should have access to /zuzu only

# How can I login to ldap?
access http://localhost:8080/

Username: admin
password: 123

BTW: all users in ldap have the same passwords: 123
