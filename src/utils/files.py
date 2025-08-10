import os
from typing import AsyncGenerator


async def file_generator(size: int | None = None) -> AsyncGenerator[bytes]:
    size = size if size is not None else float("inf")

    while size > 0:
        chunk = os.urandom(1024)
        yield chunk
        size -= 1024
