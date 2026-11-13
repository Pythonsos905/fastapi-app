from fastapi import FastAPI

# Создаем приложение FastAPI
app = FastAPI(title="Мой первый сервис на FastAPI")

# Главная страница (отдает чистый JSON, как в реальных микросервисах)
@app.get("/")
def read_root():
    return {"status": "ok", "developer": "Андрей", "level": "Junior+"}

# Динамический маршрут с параметром (например, /items/5?q=телефон)
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = "Без описания"):
    return {"item_id": item_id, "query": q}