---
type: procedure
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - '[[techniques/Adversary-in-the-Middle|T1557 - Adversary-in-the-Middle]]'
  - '[[techniques/Network Sniffing|T1040 - Network Sniffing]]'
sub_techniques:
  - >-
    [[techniques/Adversary-in-the-Middle/ARP Cache Poisoning|T1557.002 - ARP
    Cache Poisoning]]
tags:
  - bettercap
  - mitm
  - arp-spoofing
  - traffic-interception
commands:
  - '[[commands/list-network-interfaces]]'
  - '[[commands/bettercap-launch-proxy-spoofing]]'
  - '[[commands/view-arp-cache]]'
tools:
  - '[[tools/bettercap]]'
platforms:
  - Linux
  - macOS
skill_level: intermediate
impact_level: high
detection_risk: high
verified: true
validated: true
---

# Intercept Network Traffic with Bettercap Proxy Spoofing

## Summary

The Bettercap Proxy Spoofing procedure enables an attacker to perform a man-in-the-middle (MITM) attack on a local network by using ARP spoofing to redirect a target's traffic through the attacker's machine and intercepting HTTP and HTTPS requests with Bettercap's proxy modules. This technique is useful for capturing sensitive data such as login credentials in environments with unencrypted or vulnerable traffic, particularly on shared Wi-Fi or LAN segments.

## Description

This procedure leverages Bettercap, a versatile network attack tool, to poison the ARP cache of a target device, causing it to send traffic to the attacker's IP instead of the legitimate gateway. Once traffic is routed through the attacker, the built-in proxy modules capture and potentially modify requests. It is most effective in non-switched networks or where the attacker can position themselves appropriately. The technique assumes the attacker has Layer 2 access to the same broadcast domain as the target. Success depends on the network configuration and the target's use of encryption; HTTPS interception requires additional CA certificate installation on the target for full decryption, which is beyond this procedure's scope.

## Requirements

1. Bettercap installed on the attacker's Linux or macOS machine (see [[tools/bettercap]] for installation).
2. Root or administrator privileges on the attacker machine to perform packet injection and interface manipulation.
3. Physical or wireless access to the same local network segment (LAN or Wi-Fi) as the target device.
4. Knowledge of the target's IP address.
5. Optional: A wordlist or tool for credential analysis if capturing login attempts.

## Defense

- Implement HTTPS with HSTS to prevent proxy interception of encrypted traffic.
- Deploy ARP spoofing detection tools like ARPwatch or dynamic ARP inspection on switches.
- Use network segmentation (VLANs) to isolate critical devices and limit broadcast domains.
- Monitor for anomalous ARP table changes and unexpected traffic routing via IDS/IPS systems like Snort or Suricata.
- Educate users on avoiding public Wi-Fi for sensitive activities and using VPNs for encryption.

## Objectives

1. Redirect the target's network traffic through the attacker's machine via ARP spoofing.
2. Intercept and log HTTP/HTTPS requests to capture sensitive information like credentials.
3. Perform real-time analysis or modification of intercepted traffic for further exploitation.
4. Maintain stealth by mimicking legitimate network behavior to avoid detection.

## Instructions

### Step 1: Identify the Network Interface

**Context**: Determine the correct network interface connected to the target's network to ensure Bettercap operates on the right adapter for spoofing and sniffing. This step prevents errors from using the wrong interface, such as Wi-Fi vs. Ethernet.

**Command** ([[commands/list-network-interfaces]]):
```bash
ip link show
```

> This command lists all available network interfaces. Identify the one active on the target network (e.g., 'eth0' for wired or 'wlan0' for wireless) by checking the state (UP) and IP configuration. If the Bettercap command requires an interface flag, note it here; otherwise, proceed as the tool auto-detects in many cases.

### Step 2: Launch Bettercap for Proxy Spoofing

**Context**: Initiate the MITM attack by starting Bettercap with flags to enable experimental features, proxy modules for HTTP/HTTPS interception, and targeting the victim's IP. This poisons the ARP cache and routes traffic through your machine for inspection.

**Command** ([[commands/bettercap-launch-proxy-spoofing]]):
```bash
bettercap -X --proxy --proxy-https -T $_TARGET_IP
```

> Run this as root. Bettercap will load the necessary modules, perform host discovery if needed, and begin ARP spoofing. Monitor the console output for confirmation that the proxy is listening (typically on port 8080) and ARP replies are being sent. If on a switched network, ensure you're in the path or use additional techniques like spanning tree manipulation.

### Step 3: Verify ARP Spoofing Success

**Context**: Confirm the spoofing is active by checking the local ARP cache to see if the target's IP now resolves to your machine's MAC address, indicating successful traffic redirection.

**Command** ([[commands/view-arp-cache]]):
```bash
arp -a | grep $_TARGET_IP
```

> This filters the ARP table for the target IP. Success is indicated if your MAC address appears instead of the gateway's. From the target machine, you can also run the same command to verify the poisoning took effect.

## Expected Output

Successful execution produces console logs from Bettercap showing module activation (e.g., "[http.proxy] Starting on 0.0.0.0:8080", "[arp.spoof] Sending spoofed ARP replies"), discovered hosts, and intercepted requests like "GET /login HTTP/1.1" with headers and payloads. In the ARP verification, output resembles "? (192.168.1.100) at aa:bb:cc:dd:ee:ff [ether] on eth0", where the MAC is yours. Captured credentials appear in plain text for HTTP or as encrypted for HTTPS (requiring further decryption).

---

*Last updated: 2023-10-01T00:00:00Z*
