import os
from typing import AsyncGenerator


async def file_generator(size: int | None = None) -> AsyncGenerator[bytes]:
    """
    Asynchronously generate random binary chunks.

    This coroutine yields 1024-byte chunks of cryptographically secure random
    data (via `os.urandom`). Generation continues until the requested size is
    exhausted, or indefinitely if no size is given.

    Args:
        size (int | None, optional): Total number of bytes to produce. If None,
            data is generated without limit. Defaults to None.

    Yields:
        bytes: A 1024-byte random chunk (the final chunk may be smaller if
        `size` is not a multiple of 1024).

    Notes:
        - Intended for streaming random data, e.g., for testing file uploads or
          consuming code that expects async generators of binary content.
        - Uses `os.urandom`, which is suitable for cryptographic use.

    """

    chunk_size: int | float = size if size is not None else float("inf")

    while chunk_size > 0:
        chunk = os.urandom(1024)
        yield chunk
        chunk_size -= 1024
