# A simple UI using fast API
# Need fast API package, a server, Transformer package
# What do we need to request from the server?
# Root url for some documentations
# Training

# What do we need to post to the server?
# Our Dialouge to get the summary

from fastapi import FastAPI
import uvicorn
from TextSummarizer.pipeline.prediction import PredictionPipeline
import os
import sys
from fastapi.responses import Response
from starlette.responses import RedirectResponse


# Place holder text and api object
text: str = "What is Text Summarization ?"
app = FastAPI()


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training Successful !!")

    except Exception as e:
        return Response(f"Error Occured! {e}")


@app.post("/predict")
async def predict_route(text):
    try:
        pred_pipe = PredictionPipeline()
        pred = pred_pipe.predict(text=text)
        return pred
    except Exception as e:
        raise e

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
