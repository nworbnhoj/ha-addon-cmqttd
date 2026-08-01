
from pathlib import Path

def test_reference_exists():
    assert Path('cmqttd/config.schema.reference.yaml').exists()
