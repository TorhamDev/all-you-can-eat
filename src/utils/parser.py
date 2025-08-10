def parse_size_to_byte(size: str | None) -> int | None:
    if not size:
        return None

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
