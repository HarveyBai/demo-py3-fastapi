from demo_py3_fastapi.config.my_config import my_config
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    my_config.reload_config()
    # ("my_config: ", my_config.get_app_config())
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
