
from cmqttd_addon.health import check

def test_health_returns_dict():
    assert isinstance(check(), dict)
