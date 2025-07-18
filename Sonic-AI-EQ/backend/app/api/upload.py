from fastapi import APIRouter, File, UploadFile
from ..services.file_service import save_upload_file

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    filename = await save_upload_file(file)
    return {"filename": filename}