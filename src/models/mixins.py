class InitLoggerMixin:
    def __init__(self, *args, **kwargs) -> None:
        print(repr(self))
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        args = ", ".join(repr(v) for v in self.__dict__.values())
        return f"{self.__class__.__name__}({args})"