from fastapi import FastAPI
import random
from faker import Faker

app = FastAPI()
fake = Faker()

@app.get("/generate_users")
def generate_users(count: int = 1100):
    users = []
    for _ in range(count):
        user = {
            "name": fake.name(),
            "age": random.randint(18, 65),
            "location": fake.city()
        }
        users.append(user)
    return users

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)