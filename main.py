from common.telemetry import init_telemetry

init_telemetry("api-gateway")

from fastapi import FastAPI

app = FastAPI(title="API Gateway")

@app.get("/health")
def health():
    return {"status": "ok"}
