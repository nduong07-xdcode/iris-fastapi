
import requests
url = "https://iris-fastapi-w3k7.onrender.com/predict"
data = {
"sepal_length": 5.1,
"sepal_width": 3.5,
"petal_length": 1.4,
"petal_width": 0.2,
}
response = requests.post(url, json=data, timeout=30)
response.raise_for_status()
print(response.json())