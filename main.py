```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class WeatherData(BaseModel):
    location: str
    date: str
    temperature: float
    description: str
    humidity: int
    wind_speed: int
    precipitation: float

class ForecastData(BaseModel):
    location: str
    forecast: List[WeatherData]

class HistoricalData(BaseModel):
    location: str
    date: str
    temperature_high: float
    temperature_low: float
    description: str
    precipitation: float

# Dummy data to simulate API responses
weather_data = {
    "New York City": WeatherData(location="New York City", date="2022-10-15", temperature=72, description="Partly cloudy", humidity=65, wind_speed=10, precipitation=0.1),
    # Add more dummy data as needed
}

forecast_data = {
    "San Francisco": ForecastData(
        location="San Francisco",
        forecast=[
            WeatherData(date="2022-10-16", description="Sunny", temperature=75, temperature_low=60),
            WeatherData(date="2022-10-17", description="Rainy", temperature=65, temperature_low=55),
            # Add more forecast data as needed
        ]
    ),
    # Add more forecast data as needed
}

historical_data = {
    "London": HistoricalData(location="London", date="2022-09-01", temperature_high=70, temperature_low=55, description="Cloudy", precipitation=0.2),
    # Add more historical data as needed
}

@app.get("/current-weather/{location}")
async def get_current_weather(location: str):
    if location not in weather_data:
        raise HTTPException(status_code=404, detail="Location not found")
    return weather_data[location]

@app.get("/forecast/{location}")
async def get_forecast(location: str):
    if location not in forecast_data:
        raise HTTPException(status_code=404, detail="Location not found")
    return forecast_data[location]

@app.get("/historical-data/{location}")
async def get_historical_data(location: str, date: str):
    if location not in historical_data:
        raise HTTPException(status_code=404, detail="Location not found")
    if historical_data[location].date != date:
        raise HTTPException(status_code=404, detail="Historical data not available for the specified date")
    return historical_data[location]
```