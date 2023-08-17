import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.endpoints import (
    destinations,
    users,
    authentication,
    registration,
    initialise,
    availabilities,
    notification_of_interest,
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(destinations.router)
app.include_router(users.router)
app.include_router(authentication.router)
app.include_router(registration.router)
app.include_router(initialise.router)
app.include_router(availabilities.router)
app.include_router(notification_of_interest.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
