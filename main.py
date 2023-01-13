from fastapi import FastAPI
from chat import chatgpt_clone
from pydantic import BaseModel
import uvicorn 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    chat: str
@app.get("/")
def read_root():
    return {"Hello": "Ssebowa Chatbot"}

@app.get('/{input}')
async def read_chat(input:str):
    return chatgpt_clone(input)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)