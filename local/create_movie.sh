#!/bin/bash

requestData="{\"movie_id\":\"$(uuidgen)\",\"title\":\"Tanner sucks\",\"director\":\"Mr. Director\"}"
echo $requestData

curl --header "Content-Type: application/json" \
  --request POST \
  --data "$requestData" \
  https://efhveup792.execute-api.us-east-2.amazonaws.com/default/movie

# Without this empty print, the terminal doesn't go to a new line
echo ""
