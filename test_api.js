fetch("https://iris-fastapi-w3k7.onrender.com/predict", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        sepal_length: 5.1,
        sepal_width: 3.5,
        petal_length: 1.4,
        petal_width: 0.2
    })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error("Error:", error));