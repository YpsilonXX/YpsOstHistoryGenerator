def safe_input(
    prompt: str = "→ ",
    expected_type: type = str,
    on_error=None,
    allow_empty: bool = False,
    strip: bool = True
):
    """
    Safe input with type checking

    Parameters:\n
        prompt (str): What to print before input (default: "→ ")
        expected_type (type): Expected type of the input — str, int, float, bool (default: str)
        on_error: Value to return when conversion fails.
                  If None — the function will ask again until correct input (default: None)
        allow_empty (bool): Can user input empty line (just press Enter)?
                            If False — empty input is rejected (default: False)
        strip (bool): Automatically remove leading and trailing whitespace?
                      If True — .strip() / .rstrip() is applied (default: True)

    Examples:\n
        age    = safe_input("Age: ", int, on_error=-1)\n
        height = safe_input("Height: ", float, on_error=0.0)\n
        name   = safe_input("Name: ", str, on_error="")\n
        agree  = safe_input("Continue? (yes/no): ", bool, on_error=False)\n

    Returns:
        Value of expected_type or on_error value (when applicable)\n
    """
    while True:
        user_input = input(prompt).rstrip() if strip else input(prompt)

        if not user_input and not allow_empty:
            print("Input cannot be empty")
            continue

        if expected_type is str:
            return user_input

        if expected_type is bool:
            lowered = user_input.lower().strip()
            if lowered in ("yes", "y", "true", "1", "да", "ok", "okay"):
                return True
            if lowered in ("no", "n", "false", "0", "нет", "-"):
                return False
            print("Expected yes/no, y/n, true/false, 1/0")
            continue

        # numeric types
        try:
            value = expected_type(user_input)
            return value
        except (ValueError, TypeError):
            if on_error is not None:
                return on_error

            type_name = expected_type.__name__
            print(f"Expected type {type_name}, got: {repr(user_input)}")
            # loop continues