import os
import tempfile

import pytest

from app import app

def test_dummy():
    assert True

@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            flaskr.init_db()
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])