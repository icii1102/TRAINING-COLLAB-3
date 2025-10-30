import time
import board
import adafruit_dht
import paho.mqtt.client as mqtt

# ---- Konfigurasi MQTT ----
MQTT_BROKER = "192.168.0.123"   # Ganti dengan IP laptop kamu (tempat broker MQTT)
MQTT_PORT = 1883
MQTT_TOPIC = "sensor/dht11"

# ---- Setup DHT11 ----
dht_device = adafruit_dht.DHT11(board.D4)  # Pin data DHT11 ke GPIO4

# ---- Setup MQTT ----
client = mqtt.Client("RaspberryPi_DHT11")
client.connect(MQTT_BROKER, MQTT_PORT, 60)

print("Mulai membaca DHT11 dan mengirim ke MQTT...")

try:
    while True:
        try:
            temperature = dht_device.temperature
            humidity = dht_device.humidity

            if temperature is not None and humidity is not None:
                data = f"{temperature},{humidity}"
                print(f"Publish → {MQTT_TOPIC}: {data}")
                client.publish(MQTT_TOPIC, data)
            else:
                print("Gagal membaca data sensor!")

        except RuntimeError as e:
            print("Error pembacaan sensor:", e.args[0])

        time.sleep(2)

except KeyboardInterrupt:
    print("\nProgram dihentikan oleh user.")
    dht_device.exit()
