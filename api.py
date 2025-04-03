from fastapi import FastAPI
from fastapi.responses import FileResponse  
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os
from IA.app import chat_bot
from procuraBase import procuraBase
from utils import apresenta_lista

app = FastAPI()

# Servir arquivos estáticos (frontend)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Servir o arquivo index.html na raiz
@app.get("/")
def read_root():
    return FileResponse(os.path.join("static", "index.html"))

# Modelo para definir o input esperado do frontend
class InputData(BaseModel):
    text: str

# Função que processa a string e devolve um JSON
def processar_string(texto: str):
    chat_bot_response = chat_bot(texto)
    print(f"Resposta do chat_bot: {chat_bot_response}")
    return chat_bot_response

# Função que transforma o JSON numa string
def json_para_string(dados: dict):
    lista_produtos = dados["detalhes"]["produtos_sugeridos"]
    lista_resultado = procuraBase(lista_produtos)
    resposta_normal = dados["resposta"]
    return f"{resposta_normal}\n{apresenta_lista(lista_resultado)}"

# Endpoint da API
@app.post("/process")
def processar(input_data: InputData):
    json_resultado = processar_string(input_data.text)
    resposta = json_para_string(json_resultado)
    return {"response": resposta}