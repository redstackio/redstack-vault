---
tags:
  - nextcloud
  - ip-rotation
  - bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/IP-Rotate]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:28:28.122Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: f76cb108-6a4a-43cd-a785-839b2759b62a
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Bypass-Rate-Limit-with-IP-Rotation

## Summary

This procedure bypasses Nextcloud's IP-based rate limit on password reset by using Burp Intruder with the IP Rotate extension to send requests from varying IPs.

## Description

Send the request to Intruder, enable IP Rotate (a Burp extension for proxy rotation), set position to null payloads (no changes to body/headers), and launch. This evades the limit as each request appears from a new IP. No CAPTCHA or user-based limits allow unlimited sends. Expected outcome: Requests succeed indefinitely.

## Requirements

1. Tested request from Repeater
2. IP Rotate extension installed in Burp
3. Multiple proxy IPs available (e.g., via VPN or extension config)

## Defense

Defensive measures and detection strategies:

- Add CAPTCHA after failed resets
- Track resets per user/email across IPs
- Monitor for rapid requests from proxy-like IPs

## Objectives

1. Evade IP restrictions
2. Enable scalable flooding
3. Demonstrate vulnerability

## Instructions

### Step 1: Send to Intruder

**Context**: Prepare for automated sending.

Right-click request in Repeater > Send to Intruder.

### Step 2: Configure IP Rotate

**Context**: Enable rotation to bypass limits.

In Intruder, go to Options > Extensions > Enable IP Rotate. Set payloads to null, start attack.

> Expected output: Attack log shows successful 200 responses, IPs rotating per request.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]
- [[tools/IP-Rotate]]

## Tags

- [[nextcloud]]
- [[ip-rotation]]
