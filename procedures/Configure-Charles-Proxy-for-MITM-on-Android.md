---
tags:
  - mitm
  - ssl-proxy
  - certificate-pinning-bypass
  - android
type: procedure
tools:
  - '[[tools/Charles-Proxy]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:24:41.672Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 0cf696ce-12fa-4955-9eab-7125e0e9cc8a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Configure-Charles-Proxy-for-MITM-on-Android

## Summary

This procedure sets up Charles Proxy as an intercepting proxy to route traffic from an Android device, installs the proxy's root CA certificate to bypass SSL verification (exploiting missing certificate pinning), and enables decryption of HTTPS traffic to the Coinbase API, allowing observation and manipulation of app communications.

## Description

Due to the absence of SSL certificate or public key pinning in the Coinbase Android app, it trusts the device's default CA store, making it vulnerable to MITM attacks when a custom CA is installed. This procedure configures Charles Proxy on a host machine (e.g., laptop), installs its charles.crt on the Android device to trust forged certificates, sets the device's Wi-Fi proxy to the host's IP:8888, and activates SSL proxying for coinbase.com domains. The target environment is an Android device on the same local network as the proxy host. Prerequisites include physical access to the device for CA installation. Expected outcomes: Full decryption and interception of app-to-API HTTPS traffic, revealing plaintext data like tokens and requests.

## Requirements

1. Charles Proxy installed on host machine (macOS/Windows/Linux)
2. Android device with Coinbase app and developer options enabled for CA installation
3. Local network shared between host and device
4. Administrative access on device to install certificates

## Defense

Defensive measures and detection strategies:

- Implement certificate pinning in mobile apps to reject untrusted CAs
- Detect proxy usage via app-level network checks or anomaly detection in traffic patterns
- Use device management policies to restrict custom CA installations and proxy configurations

## Objectives

1. Route Android traffic through Charles Proxy
2. Bypass SSL pinning by trusting the proxy CA
3. Enable HTTPS decryption for coinbase.com API endpoints

## Instructions

### Step 1: Install and Launch Charles Proxy

**Context**: Set up the proxy server on the host machine to intercept HTTP/HTTPS traffic.

No specific command; download from http://www.charlesproxy.com and launch the application.

> Configure Charles to listen on port 8888 (default). Ensure the host IP is noted for device configuration.

### Step 2: Install Proxy CA Certificate on Android Device

**Context**: Download and install the Charles root CA to allow the device to trust proxy-issued certificates for coinbase.com.

No specific command; use device browser to visit http://www.charlesproxy.com/charles.crt, download, and install via Settings > Security > Install from storage.

> Enable "Trust this CA for SSL" in certificate details. This exploits the app's reliance on system CA trust without pinning.

### Step 3: Configure Device Proxy Settings

**Context**: Route the Android device's Wi-Fi traffic through the proxy.

No specific command; go to Wi-Fi settings, long-press the network, select Modify > Advanced > Proxy > Manual, enter host IP and port 8888.

> Save settings. Test by browsing a site; traffic should appear in Charles.

### Step 4: Enable SSL Proxying

**Context**: Activate decryption for HTTPS traffic to Coinbase domains.

No specific command; in Charles, go to Proxy > SSL Proxying Settings, add "*.coinbase.com" to the list, and enable.

> Restart Charles if needed. Launch Coinbase app; login requests should now decrypt in the proxy interface.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Charles-Proxy]]

## Tags

- mitm
- ssl-proxy
