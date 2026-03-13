import pytest
import os

@pytest.fixture
def log_file():
    f = open("text_log.txt", "w")
    yield f
    f.close()
    os.remove("text_log.txt")

def test_escrita_log(log_file):
    log_file.write("Teste de log")
    assert not log_file.closed