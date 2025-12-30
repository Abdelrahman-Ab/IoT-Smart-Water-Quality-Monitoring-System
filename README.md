# IoT-Smart-Water-Quality-Monitoring-System
This project monitors water quality parameters (TDS/ppm, turbidity, pH, temperature) using sensors connected to a Raspberry Pi. It integrates an AI model to classify water safety and publishes the data securely to HiveMQ Cloud via MQTT for real-time monitoring on dashboards or apps. The system also controls an LED based on temperature thresholds.

---

## Features

- Reads analog sensors via **MCP3008 (SPI)**: TDS/ppm, turbidity, pH  
- Reads temperature via **DS18B20 (1-Wire)**  
- AI classification of water quality (`SAFE`, `WARNING`, `DANGEROUS`)  
- Publishes data to **HiveMQ Cloud** using **MQTT over TLS**  
- JSON payload for dashboards / web / mobile apps  
- LED turns ON if temperature exceeds threshold  
- Fully **automated startup** on Raspberry Pi boot

---

## Project Modules

The code is divided into 5 modules for easy collaboration:

| Module | Responsibility |
|--------|----------------|
| `adc_reading.py` | MCP3008 sensor reading (TDS, turbidity, pH) |
| `temperature.py` | DS18B20 temperature reading + LED control |
| `ai_model.py` | AI model loading and classification |
| `mqtt_client.py` | MQTT connection, publishing, and AI integration |
| `main.py` | Thread orchestration and console output |

---

## Hardware

| Sensor / Device | Protocol | Description |
|-----------------|---------|------------|
| MCP3008 ADC | SPI | Reads analog sensors: TDS, turbidity, pH |
| DS18B20 | 1-Wire | Temperature measurement |
| LED | GPIO | Indicates temperature threshold exceeded |

---

## Communication Overview

- **SPI (MCP3008)**: Fast, reliable for analog sensor readings  
- **1-Wire (DS18B20)**: Simple, low-pin-count for temperature  
- **MQTT**: Lightweight publish/subscribe protocol for cloud communication  
  - **Publisher**: Raspberry Pi  
  - **Broker**: HiveMQ Cloud  
  - **Subscribers**: Dashboard / mobile / web apps  
  - **Security**: TLS + username/password authentication

---

## Setup

### Raspberry Pi Prerequisites

```bash
sudo apt update
sudo apt install python3-pip python3-venv python3-gpiozero python3-spidev python3-numpy
sudo raspi-config  # Enable SPI & 1-Wire
