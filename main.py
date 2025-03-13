from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ CORS（クロスオリジン）対応：どこからでもアクセスOKにしておく
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ エンドポイント名を「/uppercase」に変更
@app.get("/uppercase")
def uppercase(text: str):
    return {"result": text.upper()}

# ✅ uvicornで起動するためのコード（Render上でも自動実行される）
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
