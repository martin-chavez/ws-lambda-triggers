import requests
def lambda_handler(event, context):
  url="http://34.194.92.175:5000/changes/" + str(event["idParent"])
  response = requests.get(url)
  print(response.text)
  print(response.status_code, response.reason)
