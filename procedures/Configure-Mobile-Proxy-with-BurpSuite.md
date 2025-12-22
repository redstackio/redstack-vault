---
id: proc-configure-mobile-proxy-burp
tags:
  - proxy-setup
  - mobile-interception
type: procedure
tools:
  - '[[tools/BurpSuite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:41.847Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure Mobile Proxy with BurpSuite

## Summary

This procedure sets up BurpSuite as a proxy to intercept HTTPS traffic from an iOS app, enabling capture and modification of requests for security testing, such as analyzing authentication endpoints.

## Description

In the context of testing mobile apps like Instacart, configuring a proxy is essential to bypass potential SSL pinning and inspect API calls. This involves running BurpSuite on a host machine, configuring the iOS device's Wi-Fi proxy settings, and installing the necessary CA certificate to handle encrypted traffic. Prerequisites include a Mac or PC on the same network as the iOS device and admin access to install certificates.

## Requirements

1. BurpSuite Professional or Community edition installed on the attacker's machine
2. iOS device (iPhone/iPad) with the target app installed and Wi-Fi access
3. Same local network connectivity between device and attacker machine
4. Ability to trust enterprise certificates on iOS (Settings access)

## Defense

Defensive measures and detection strategies:

- Implement certificate pinning in mobile apps to prevent proxy interception
- Monitor for unusual proxy traffic or CA certificate installations on devices
- Use mobile device management (MDM) to restrict proxy configurations and untrusted certs

## Objectives

1. Establish a man-in-the-middle position for iOS app traffic
2. Enable real-time inspection and replay of API requests
3. Facilitate further exploitation like request modification

## Instructions

### Step 1: Launch and Configure BurpSuite

**Context**: Start BurpSuite and set it up to listen for proxy connections.

In BurpSuite, navigate to the Proxy tab > Options, ensure "Running" is checked, and note the listener on 127.0.0.1:8080. For remote access, add a new listener bound to all interfaces (0.0.0.0:8080) and enable "Support invisible proxying" for non-proxy-aware apps.

### Step 2: Configure iOS Wi-Fi Proxy

**Context**: Direct the iOS device's traffic through the proxy.

On the iOS device, go to Settings > Wi-Fi, tap the info (i) next to the network, scroll to HTTP Proxy > Manual, enter the attacker's IP address and port 8080. Save and verify by browsing a site; traffic should appear in Burp's Proxy > HTTP history.

### Step 3: Install and Trust Burp CA Certificate

**Context**: Handle HTTPS interception by installing the proxy's root certificate.

On iOS, open Safari and visit http://burp (replace with attacker IP:8080 if needed) to download the CA certificate. Go to Settings > General > VPN & Device Management (or About > Certificate Trust Settings), select the Burp certificate, and enable full trust. Relaunch the app to confirm interception.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/BurpSuite]]

## Tags

- [[proxy-setup]]
- [[mobile-interception]]
