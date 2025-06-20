def parse_boolean(value):
    """
    解析布尔值
    """
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        if value.lower() in ["true", "1", "yes", "y"]:
            return True
        if value.lower() in ["false", "0", "no", "n"]:
            return False
    raise ValueError(f"Invalid boolean value: {value}")
