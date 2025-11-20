from .api import app
from .database import * 
from .crud import ShortDBClient as db_client
db = db_client()

@app.get("/v1/shorts/{id}", tags=["GET"])
def read_short_api(id: int) -> str:
    return db.read_short(id)

@app.post("/v1/shorts/create", tags=["POST"])
def create_short_api(url: str) -> int:
    return db.create_short(url)

@app.put("/v1/shorts/update/{id}", tags=["PUT"])
def update_short_api(id: int, url: str) -> bool:
    return db.update_short(id, url)

@app.get("/v1/shorts", tags=["GET"])
def read_all() -> list[str]:
    return db.read_all()

@app.get("/v1/shorts/random", tags=["GET"])
def read_short_random() -> str:
    return db.read_short_random()

@app.delete("/v1/shorts/delete/{id}", tags=["Delete"])
def delete_short(id: int) -> bool:
    return db.delete_short(id)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)