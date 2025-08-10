import os
from typing import Generator


def file_generator(size: int | None = None) -> Generator[bytes]:
    reminding = size

    while True:
        chunk = os.urandom(1024)
        yield chunk

        if reminding:
            reminding -= 1024

            if reminding <= 0:
                break
