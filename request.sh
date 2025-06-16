curl --header "Content-Type: application/json" \
  --request GET \
  --data '{"id":"123","title":"New Movie","director":"Mr. Director"}' \
  https://efhveup792.execute-api.us-east-2.amazonaws.com/default

# Without this empty print, the terminal doesn't go to a new line
echo ""
