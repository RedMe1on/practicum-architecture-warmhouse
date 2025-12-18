import datetime
from fastapi import FastAPI, Query
import random

from pydantic import BaseModel

app = FastAPI(
    title="Temerature API",
    description="API для имитации работы удаленного датчика",
    version="1.0.0",
)


@app.get("/temperature")
def sensor_temperature(location: str | None = Query()) -> dict:
    return {
        "location": location,
        "value": random.randint(-30, 30),
        "unit": "°C",
        "status": "active",
        "timestamp": datetime.datetime.now(tz=datetime.timezone.utc),
        "description": "Good Day",
    }


@app.get("/temperature/{id}")
def sensor_temperature_by_id(id: int) -> dict:
    return {
        "id": id,
        "value": random.randint(-30, 30),
        "unit": "°C",
        "status": "active",
        "timestamp": datetime.datetime.now(tz=datetime.timezone.utc),
        "description": "Good Day",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8081, reload=True)
