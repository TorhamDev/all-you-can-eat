from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from src.utils import file_generator


app = FastAPI(debug=True)


@app.get("/")
def root(filename: str, size: int | None = None) -> StreamingResponse:
    file_iter = file_generator(size=size)

    return StreamingResponse(
        file_iter, headers={"Content-Disposition": f'attachment; filename="{filename}"'}
    )
