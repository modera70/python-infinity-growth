import enum


class Driver(enum.Enum):
    FIREFOX = "firefox-browser-config.json"
    CHROME = "chrome-browser-config.json"

    @staticmethod
    def values():
        return [pair.value for pair in Driver]

    def __str__(self) -> str:
        return self.name

