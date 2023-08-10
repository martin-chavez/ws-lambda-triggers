import requests
def lambda_handler(event, context):
  try:
    url="http://44.194.243.124:5000/changes/" + str(event["idParent"])
    response = requests.get(url)
    print(response.text) #TEXT/HTML
    print(response.status_code, response.reason) #HTTP
  except Exception as e:
    print("Error occurred while hitting WS API")
    print(e)
