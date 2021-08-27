from starlette.responses import FileResponse, RedirectResponse
from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["Home"])
def index():
    return RedirectResponse(url="/app")


@router.get("/app", tags=["Home"])
def application():
    return FileResponse("app/public/index.html")


@router.get("/hello", tags=["Home"])
def hello_world():
    return "hello world"
