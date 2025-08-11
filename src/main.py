from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi.responses import StreamingResponse
from src.utils.files import file_generator
from src.utils.parser import parse_size_to_byte
from starlette.responses import FileResponse


app = FastAPI(debug=True)


@app.get("/")
async def read_index():
    return FileResponse("./src/templates/index.html")


@app.get("/eat")
async def eat(
    filename: str, size: Annotated["int | None", Depends(parse_size_to_byte)]
) -> StreamingResponse:
    file_iter = file_generator(size=size)

    return StreamingResponse(
        file_iter, headers={"Content-Disposition": f'attachment; filename="{filename}"'}
    )
