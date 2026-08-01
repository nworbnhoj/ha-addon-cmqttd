from cmqttd_addon.topics import light_topic

def test_topic():
 assert light_topic('homeassistant','kitchen')=='homeassistant/light/kitchen'
