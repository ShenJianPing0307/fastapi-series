from typing import List
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/multi/uploaadfile/")
async def create_multi_upload_file(files: List[UploadFile] = File(...)):
    results = []
    for file in files:
        content = await file.read()
        print(content)
        results.append({"filename": file.filename, "content_type": file.content_type})
    return results


@app.post("/uploaadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}


@app.post("/file/")
async def create_file(file: bytes = File(...)):
    print(file)
    return {"file_size": len(file)}


@app.post("/multi/file/")
async def create_multi_file(file: List[bytes] = File(...)):
    return {"file_size": len(file)}
