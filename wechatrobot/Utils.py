from typing import Any, Callable, Awaitable, Iterable, List

def run_funcs(funcs: Iterable[Callable[..., Awaitable[Any]]], *args,
                          **kwargs) -> List[Any]:
    results = []
    for f in funcs:
        results.append(f(*args, **kwargs))
    return results