from abc import ABC, abstractmethod
import os


class ConfigSource(ABC):
    @abstractmethod
    def load_value(self, key: str) -> str | None:
        pass


class FileConfigSource(ConfigSource):
    FILE_CONFIG = {"db.host": "localhost"}

    def load_value(self, key: str) -> str | None:
        return self.FILE_CONFIG.get(key, None)


class EnvConfigSource(ConfigSource):
    def load_value(self, key: str) -> str | None:
        key = key.replace(".", "_").upper()
        return os.environ.get(key, None)

class DefaultConfigSource(ConfigSource):
    DEFAULTS = {"db.host": "127.0.0.1", "db.port": "3306", "db.timeout": "30"}

    def load_value(self, key: str) -> str | None:
        return self.DEFAULTS.get(key, None)


class ConfigLoader:
    def __init__(self, sources: list[ConfigSource]):
        self._sources = sources

    def get(self, key: str) -> str | None:
        for source in self._sources:
            value = source.load_value(key)
            if value is not None and value != "":
                return value
            else:
                continue

        if value:
            return value
        else:
            raise ValueError(f"{key} doesnot exist")


if __name__ == "__main__":
    file_source = FileConfigSource()
    env_source = EnvConfigSource()
    default_source = DefaultConfigSource()
    loader = ConfigLoader([file_source, env_source, default_source])

    host = loader.get("db.host")
    port = loader.get("db.port")
    time_out = loader.get("db.timeout")
    print(f"db host = {host}")
    print(f"db port = {port}")
    print(f"db time out = {time_out}")
