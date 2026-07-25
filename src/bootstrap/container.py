from dependency_injector import containers


class ApplicationContainer(containers.DeclarativeContainer):
    """
    Dependency Injection Container.

    All application dependencies will be registered here.
    """

    wiring_config = containers.WiringConfiguration(
        packages=[
            "src.modules",
        ]
    )