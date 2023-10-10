from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
from clf_helper import PlantDiseaseClassifier

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/upload/")
async def upload_image(file: UploadFile):
    try:

        uploaded_image = Image.open(file.file)
        classifier = PlantDiseaseClassifier()
        predicted_class, confidence = classifier.predict_img(uploaded_image)

        return JSONResponse(content={'predicted_class': predicted_class, 'confidence': confidence}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"message": str(e)}, status_code=500)
