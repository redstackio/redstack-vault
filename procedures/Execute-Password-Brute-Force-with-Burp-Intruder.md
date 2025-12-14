---
tags:
  - burp-intruder
  - brute-force
  - account-takeover
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:31:43.019Z'
sub_techniques: []
id: 45d3a078-0e58-4c34-a82e-f5f24202ec51
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Execute-Password-Brute-Force-with-Burp-Intruder

## Summary

This procedure uses Burp Suite's Intruder module to automate brute force attacks on the WebDAV Basic Auth endpoint, sending multiple encoded payloads until a successful authentication is achieved, leading to account takeover.

## Description

Burp Intruder allows positioning the payload in the Authorization header of the captured request and iterating through the Base64-encoded list. Without rate limiting, the attack can run unrestricted, returning HTTP 200 on success, granting access to the victim's Nextcloud resources via WebDAV.

## Requirements

1. Captured request from previous step
2. Prepared Base64 payload list
3. Burp Suite Professional (Intruder feature)

## Defense

Defensive measures and detection strategies:

- Deploy fail2ban or similar to block IPs after failed auth attempts
- Use HTTPS and monitor for unusual HTTP 401 spikes on WebDAV paths
- Patch Nextcloud to enable brute force protection (e.g., via app or config)

## Objectives

1. Automate credential testing
2. Identify valid password
3. Gain authenticated WebDAV access

## Instructions

### Step 1: Send Request to Intruder

**Context**: Load the captured auth request into Intruder for modification.

No command required; in Burp:

- Right-click the request in Proxy > Send to Intruder
- Clear any existing positions (§ symbol)
- Mark the Base64 value after 'Basic ' in Authorization header as payload position (e.g., Authorization: Basic §<payload>§)

> Expected output: Positions tab shows one payload position.

### Step 2: Load Payloads and Attack

**Context**: Configure and launch the brute force.

No command required; in Intruder:

- Go to Payloads tab > Load the Base64-encoded list
- Set attack type to Sniper (single position)
- Start attack in Intruder tab
- Sort results by response code/length to spot HTTP 200

> Expected output: Table of responses; HTTP 200 with shorter length or specific content indicates success. Decode the matching payload to reveal the password.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[burp-intruder]]
- [[account-takeover]]
