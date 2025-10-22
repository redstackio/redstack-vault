---
id: 41c8b396-87d8-413c-b7ce-10d98bc9a8dc
name: blueranger.sh
type: tool
verified: false
created_at: '2019-08-28T21:17:20.969163+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# blueranger.sh

## Overview

BlueRanger is a simple Bash script which uses Link Quality to locate Bluetooth device radios. It sends l2cap (Bluetooth) pings to create a connection between Bluetooth interfaces, since most devices allow pings without any authentication or authorization. The higher the link quality, the closer the

## Description

BlueRanger is a simple Bash script which uses Link Quality to locate Bluetooth device radios. It sends l2cap (Bluetooth) pings to create a connection between Bluetooth interfaces, since most devices allow pings without any authentication or authorization. The higher the link quality, the closer the device (in theory).Use a Bluetooth Class 1 adapter for long range location detection. Switch to a Class 3 adapter for more precise short range locating. The recision and accuracy depend on the build quality of the Bluetooth adapter, interference, and response from the remote device. Fluctuations may occur even when neither device is in motion.BlueRanger Homepage | Kali BlueRanger Repo
