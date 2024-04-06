from fastapi import FastAPI
from service.api.api import main_router
import uvicorn
import onnxruntime as rt

app=FastAPI(project_name="SkinDisease Detction")

app.include_router(main_router)

providers=['CPUExecutionProvider']
m_q=rt.InferenceSession("service/VIT23n_quantmodel.onnx", 
                            providers=providers)

@app.get("/")
async def root():
    return {"hello":"world"}

 # at last, the bottom of the file/module
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=5049)