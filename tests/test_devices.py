
from cmqttd_addon.devices import validate_cni

def test_validate_cni():
    assert validate_cni("192.168.1.10",10001)
    assert not validate_cni("",10001)
