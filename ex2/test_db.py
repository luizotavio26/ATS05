def test_db_1(db_connection):
    assert "Conexão Global Estabelecida" in db_connection

def test_db_2(db_connection):
    assert "Conexão Global Estabelecida" in db_connection