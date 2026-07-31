
from cmqttd_addon.models import Config
from cmqttd_addon.generator import render

def test_render():
    text=render(Config())
    assert "mqtt:" in text
