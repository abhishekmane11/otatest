from ota import OTAUpdater

SSID = "Getparking"

PASSWORD = "playtmbiz"

firmware_url = "https://github.com/kevinmcaleer/ota_test/main/"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "test_ota.py")

ota_updater.download_and_install_update_if_available()
print("hello")
