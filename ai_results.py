import threading
from adc_reading import adc_thread
from temperature import temp_thread
from mqtt_client import mqtt_thread, mqtt_connect, temperature_data, adc_data, lock
from ai_model import ai_classify_with_confidence
import time

if not mqtt_connect():
    print("❌ Fix MQTT connection before running")
    exit(1)

# Start threads
t1 = threading.Thread(target=adc_thread, daemon=True)
t2 = threading.Thread(target=temp_thread, daemon=True)
t3 = threading.Thread(target=mqtt_thread, daemon=True)

t1.start()
t2.start()
t3.start()

try:
    while True:
        with lock:
            ppm = adc_data["ppm"]
            turb = adc_data["turbidity"]
            ph = adc_data["ph"]
            temp = temperature_data["temp"]

            print(f"CH0 | ppm={ppm:.1f}")
            print(f"CH1 | turbidity={turb:.1f}")
            print(f"CH2 | pH={ph:.2f}")

            if temp is None:
                print("Temperature: Sensor not ready...")
                print("AI Classification: NO_TEMP")
            else:
                print(f"Temperature: {temp:.2f} °C")
                ai_result, ai_conf = ai_classify_with_confidence(ppm, turb, ph, temp)
                print(f"AI Classification: {ai_result} (Confidence {ai_conf:.2f})")

        print("-----")
        time.sleep(1)

except KeyboardInterrupt:
    print("Program stopped. LED turned OFF.")
