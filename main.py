from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ CORS設定（外部アクセスを許可）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ /uppercase エンドポイント
@app.get("/uppercase")
def uppercase(text: str):
    return {"result": text.upper()}

# ✅ サーバー起動（ローカル用）
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
