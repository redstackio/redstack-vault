---
id: proc-rogue-wifi-ap-001
tags:
  - rogue-ap
  - wifi
  - mitm
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:24:44.850Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Configure-Rogue-WiFi-Access-Point

## Summary

This procedure sets up a rogue WiFi access point on a Linux machine to attract target devices, routing their traffic through a local transparent proxy for MITM attacks on vulnerable apps like Twitter iOS.

## Description

The rogue AP simulates a legitimate network, luring users without authentication. On the same machine as the proxy, it ensures all traffic passes through the attacker's controls. Target: iOS devices on stock firmware. Outcomes: Device connectivity hijacked, enabling downstream interception without physical access beyond WiFi range.

## Requirements

1. Linux machine with WiFi adapter supporting AP mode (e.g., wlan0)
2. hostapd and dnsmasq installed for AP and DHCP
3. Proxy running on localhost

## Defense

Defensive measures and detection strategies:

- Educate users on verifying WiFi networks
- Use WPA3-Enterprise for corporate networks
- Monitor for deauth attacks or rogue SSIDs via wireless scanners

## Objectives

1. Create fake WiFi network
2. Route client traffic locally
3. Position for traffic redirection

## Instructions

### Step 1: Install and Configure hostapd

**Context**: Set up the AP software to broadcast the rogue SSID.

```bash
apt install hostapd dnsmasq
```

Create /etc/hostapd/hostapd.conf:
```
interface=wlan0
ssid=RogueTwitterNet
hw_mode=g
channel=6
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
```

Then run:
```bash
hostapd /etc/hostapd/hostapd.conf
```

> Expected output: AP started, SSID visible. wlan0 in AP mode.

### Step 2: Set Up DHCP and Routing

**Context**: Provide IP addresses to connected devices and enable IP forwarding.

Configure dnsmasq for DHCP, then:
```bash
echo 1 > /proc/sys/net/ipv4/ip_forward
sysctl -w net.ipv4.ip_forward=1
```

> Successful if devices get IPs (e.g., 192.168.1.x) and can ping gateway.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rogue-ap
- wifi
