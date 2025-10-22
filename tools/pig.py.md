---
id: 44137bae-effa-43a6-a55d-6e9488d54738
name: pig.py
type: tool
verified: false
created_at: '2019-08-28T21:17:29.098804+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# pig.py

## Overview

DHCPig initiates an advanced DHCP exhaustion attack. It will consume all IPs on the LAN, stop new users from obtaining IPs, release any IPs in use, then for good measure send gratuitous ARP and knock all windows hosts offline. It requires scapy >=2.1 library and admin privileges to execute. No conf

## Description

DHCPig initiates an advanced DHCP exhaustion attack. It will consume all IPs on the LAN, stop new users from obtaining IPs, release any IPs in use, then for good measure send gratuitous ARP and knock all windows hosts offline. It requires scapy >=2.1 library and admin privileges to execute. No configuration necessary, just pass the interface as a parameter. It has been tested on multiple Linux distributions and multiple DHCP servers (ISC, Windows 2k3/2k8).
