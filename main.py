from fastapi import FastAPI, status, Request
from app.chat import chat
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

import uvicorn 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    input: str
@app.get("/")
def read_root():
    return {"Hello": "Ssebowa Chatbot"}

@app.exception_handler(ValueError)
async def value_error_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=500,
        content={"message": str(exc)},
    )
@app.get('/chat/{input}')
async def read_chat(input:str):
    value = chat(input)
    print(value)
    # return value
    return JSONResponse(content=value,status_code=status.HTTP_200_OK)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)