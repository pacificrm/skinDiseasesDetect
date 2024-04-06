from fastapi import APIRouter, UploadFile,HTTPException
from service.api.endpoints.detect import detect_router
from service.api.endpoints.test import test_router


main_router=APIRouter()

main_router.include_router(detect_router)
main_router.include_router(test_router)
