#!/bin/bash

baseUrl="http://localhost:8081"
user='user1'
echo "Let's generate a token"
curl -i -X POST $baseUrl/generate-token.exe -d "user=$user" 2>/dev/null
