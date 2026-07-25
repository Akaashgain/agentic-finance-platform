from dataclasses import dataclass


@dataclass(slots=True)
class AppContainer:
    """Container for shared application services."""