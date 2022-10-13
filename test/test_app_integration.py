import os
import json
import pathlib
from typing import Dict, Any

import pytest
from fastapi.testclient import TestClient

from app.app import app

client = TestClient(app)

# this will soon be `from tklauthtools.testing import FlagFile`
class FlagFile:
    def __init__(self):
        self.flag_values: Dict[str, Any] = {}

    def set_flag(self, flag: str, value: Any):
        self.flag_values[flag] = value

    def write(self, path: str):
        with open(path, "w") as file:
            json.dump({"flagValues": self.flag_values}, file)


@pytest.fixture
def temp_flag_file(tmp_path: pathlib.Path):
    path = str((tmp_path / "flags.json").resolve())
    os.environ["LAUNCHDARKLY_LOCAL_FLAG_FILE"] = path
    return path


def test_default_flag(temp_flag_file):
    flags = FlagFile()
    flags.set_flag("ab-vendor-awesome-new-feature", "default")
    flags.write(temp_flag_file)

    response = client.get("/")
    assert response.text == "Nothing Special Happened"


def test_version1_flag(temp_flag_file):
    flags = FlagFile()
    flags.set_flag("ab-vendor-awesome-new-feature", "version1")
    flags.write(temp_flag_file)

    response = client.get("/")
    assert response.text.startswith("<pre>")


def test_version2_flag(temp_flag_file):
    flags = FlagFile()
    flags.set_flag("ab-vendor-awesome-new-feature", "version2")
    flags.write(temp_flag_file)

    response = client.get("/")
    assert response.text == "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
