#!/bin/bash

baseUrl="http://localhost:8081"

echo "-- /auth without headers"
curl -I $baseUrl/auth 2>/dev/null|head -n1

echo "-- /auth with unknown authorization method"
curl -I -H 'Authorization: zuzu' $baseUrl/auth 2>/dev/null|head -n1

echo "-- /auth with invalid jwt"
curl -I -H 'Authorization: Bearer zuzu' $baseUrl/auth 2>/dev/null|head -n1

declare -a users=(user1 user2 unknown)

for user in "${users[@]}"
do
  echo "-- Let's get a token for '${user}'"
  res=$(curl -i -X POST $baseUrl/generate-token.exe -d "user=$user" 2>/dev/null)
  token=$(echo "$res"|grep 'Please find your token'|awk '{ print $5}')

  if [ -z "$token" ]; then
    echo "cannot get token for '${user}'"
  else
    echo "--- verify access to /admin/"
    curl -I -H "Authorization: Bearer $token" -H "X-Original-URI: /admin/" $baseUrl/auth 2>/dev/null|head -n1
  fi
done


