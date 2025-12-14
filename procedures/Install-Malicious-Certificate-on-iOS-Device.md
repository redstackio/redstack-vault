---
id: proc-uuid-001
tags:
  - mitm
  - certificate-install
  - ios
type: procedure
tools:
  - '[[tools/Burp-Proxy]]'
  - '[[tools/mitmproxy]]'
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:24:39.457Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Install-Malicious-Certificate-on-iOS-Device

## Summary

This procedure involves installing a malicious SSL certificate on an iOS device and configuring it to be trusted, enabling the device to accept connections validated by the attacker's custom Certificate Authority (CA). It is a prerequisite for MitM attacks on apps like Shopify POS that lack certificate pinning.

## Description

The Shopify iOS POS app uses standard iOS SSL validation via the keychain, without pinning to Shopify's specific certificate or public key. An attacker can generate a fake CA certificate, export it as a .mobileconfig profile, and trick the user into installing it (e.g., via email or malicious app). Once trusted in Settings, the device will accept any certificate signed by this CA, allowing proxy tools to impersonate Shopify servers. This targets physical access scenarios or social engineering, with outcomes including full traffic interception.

## Requirements

1. Access to a machine to generate the certificate (e.g., OpenSSL installed)
2. Delivery method to the iOS device (email, website, or MDM if advanced)
3. iOS device with user interaction capability (unlocked)

## Defense

Defensive measures and detection strategies:

- Implement app-level certificate pinning to reject non-Shopify certs
- Educate users on avoiding unknown profiles and reviewing Settings > General > VPN & Device Management
- Use MDM to restrict profile installations and monitor for anomalous certificates

## Objectives

1. Establish trust in attacker's CA on the target device
2. Enable subsequent proxying without SSL errors
3. Prepare for interception of app-specific traffic

## Instructions

### Step 1: Generate Malicious Certificate

**Context**: Create a self-signed CA and export it for iOS installation.

Use OpenSSL to generate the CA (no specific command here, but assume manual generation):

On a test machine, run:

```bash
openssl req -x509 -newkey rsa:4096 -keyout ca.key -out ca.crt -days 365 -nodes
openssl x509 -req -out ca.crt -in ca.csr -signkey ca.key -CA ca.crt -CAkey ca.key -CAcreateserial -days 500 -sha256
```

> This creates ca.crt, which can be packaged into a .mobileconfig profile using tools like iPhone Configuration Utility. Expected output: ca.crt file ready for delivery.

### Step 2: Deliver and Install Profile

**Context**: Trick the user into installing the profile to add the certificate to the keychain.

Send the .mobileconfig file via email or host on a site. User opens it in Safari, taps Install, enters passcode, and goes to Settings to trust.

**Expected Output**: Profile installed; certificate visible in trusted list.

### Step 3: Verify Trust

**Context**: Confirm the device accepts the fake cert.

Browse to a test HTTPS site configured with the CA-signed cert; no warnings should appear.

**Expected Output**: Successful HTTPS connection without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Adversary-in-the-Middle]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Proxy]]
- [[tools/mitmproxy]]

## Tags

- mitm
- certificate
- ios
