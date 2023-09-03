import requests as r


# The decorator should accept a channel name as an argument.
def ntfy_on_exception(func, channel_name):
    # The decorator should return a function that wraps the original function.
    def wrapper(*args, **kwargs):
        # The wrapper should call the original function and return its result.
        try:
            return func(*args, **kwargs)
        # If the original function raises an exception, the wrapper should send a message to the specified channel.
        except Exception as e:
            r.post(
                f"https://ntfy.sh/{channel_name}",
                data="Test123".encode(encoding="utf-8"),
            )

    return wrapper
