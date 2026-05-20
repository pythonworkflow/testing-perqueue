def fix(f):
    def fm(*args, **kwargs):
        result = f(*args, **kwargs)
        if isinstance(result, dict):
            return True, result
        else:
            return True, {"data": result}

    return fm


@fix
def get_prod_and_div(x, y):
    return {"prod": x * y, "div": x / y}


@fix
def get_sum(x, y):
    return x + y


@fix
def get_square(x):
    return x ** 2
