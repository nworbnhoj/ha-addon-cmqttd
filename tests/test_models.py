from cmqttd_addon.models import AddonConfig

def test_defaults():
 assert AddonConfig().connection=='usb'
