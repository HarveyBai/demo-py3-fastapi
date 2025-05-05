#!/bin/sh
source .venv/bin/activate 
uvicorn src.demo_py3_fastapi.main:app --host 0.0.0.0 --port $PORT --reload