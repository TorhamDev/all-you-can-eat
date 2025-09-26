def parse_size_to_byte(size: str) -> int:
    """
    Convert a human-readable size string into bytes.

    Supported formats:
        - "<number>kb" → kilobytes (1024 bytes each)
        - "<number>mb" → megabytes (1024^2 bytes each)
        - "<number>gb" → gigabytes (1024^3 bytes each)
        - "<number>"   → plain integer (interpreted as bytes)

    Behavior:
        - The input is case-insensitive.
        - If the string is not in a recognized format and not a plain integer,
          returns 1024 as a default fallback.

    Args:
        size (str): Size string to parse.

    Returns:
        int: The size in bytes, or 1024 if the input is unrecognized.

    Examples:
        >>> parse_size_to_byte("10kb")
        10240
        >>> parse_size_to_byte("2MB")
        2097152
        >>> parse_size_to_byte("500")
        500
        >>> parse_size_to_byte("invalid")
        1024   # fallback default
    """

    size = size.lower()
    size_map = {"kb": 1024, "mb": 1024**2, "gb": 1024**3}

    if "gb" in size:
        return int(size[:-2]) * size_map["gb"]

    if "kb" in size:
        return int(size[:-2]) * size_map["kb"]

    if "mb" in size:
        return int(size[:-2]) * size_map["mb"]

    if size.isdigit():
        return int(size)

    return 1024
