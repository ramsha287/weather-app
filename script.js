document.getElementById("weatherForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const city = document.getElementById("city").value;

    const response = await fetch("http://127.0.0.1:8000/get_weather", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ city: city }),
    });

    const data = await response.json();

    if (data.error) {
        alert(data.error);
        return;
    }

    // Display the weather information
    document.getElementById("temp").textContent = `Temperature: ${data.temperature}°C`;
    document.getElementById("humidity").textContent = `Humidity: ${data.humidity}%`;
    document.getElementById("feelsLike").textContent = `Feels Like: ${data.feels_like}°C`;
});
