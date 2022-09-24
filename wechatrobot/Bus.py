from typing import Callable, List, Any
from collections import defaultdict

class EventBus:
    def __init__(self):
        self._subscribers = defaultdict(set)

    def subscribe(self, event: str, func: Callable) -> None:
        self._subscribers[event].add(func)

    def emit(self, event: str, *args, **kwargs) -> List[Any]:
        results = []
        for f in self._subscribers[event]:
            results.append(f(*args, **kwargs))
        return results