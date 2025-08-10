import os
from typing import AsyncGenerator


async def file_generator(size: int | None = None) -> AsyncGenerator[bytes]:
    reminding = size

    while True:
        chunk = os.urandom(1024)
        yield chunk

        if reminding:
            reminding -= 1024

            if reminding <= 0:
                break
