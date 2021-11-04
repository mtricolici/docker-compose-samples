#!/bin/bash

baseUrl="http://localhost:8081"
user='user1'
echo "Let's generate a token"
res=$(curl -i -X POST $baseUrl/generate-token.exe -d "user=$user" 2>/dev/null)

token=$(echo "$res"|grep 'Please find your token:'|awk '{ print $5}')
refresh_token=$(echo "$res"|grep 'Your refresh token is:'|awk '{ print $5}')

echo "Token is: '$token'"
echo "Refresh token: '$refresh_token'"

echo "Let's ask for a new token"
res=$(curl -i -G \
  --data-urlencode "refresh_token=$refresh_token" \
  --data-urlencode "jwt_token=${token}" \
  $baseUrl/refresh 2>/dev/null)

echo "$res"

new_token=$(echo "$res"|grep 'Your new token'|awk '{ print $4}')
echo "new token: '$new_token'"

echo "Let's validate new token"
curl -i -H "Authorization: Bearer ${new_token}" \
  -H "X-Original-URI: /something" \
  $baseUrl/auth
