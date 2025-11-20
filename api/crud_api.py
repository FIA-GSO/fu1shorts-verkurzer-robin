from .api import app
from .database import * 
from .crud import ShortDBClient as db_client
db = db_client()

@app.post("/api/create_short")
def create_short_api(url: str) -> int:
    return db.create_short(url)

@app.put("/api/update_short/<int:id>")
def update_short_api(id: int, url: str) -> bool:
    return db.update_short(id, url)

@app.get("/api/read_short/<int:id>")
def read_short_api(id: int) -> str:
    return db.read_short(id)

@app.get("/api/read_all")
def read_all() -> list[str]:

    return db.read_all()

@app.get("/api/read_short_random")
def read_short_random() -> str:
    return db.read_short_random()

@app.delete("/api/delete_short/<int:id>")
def delete_short(id: int) -> bool:
    return db.delete_short(id)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)