---
id: proc-mitm-cors-spoof
tags:
  - mitm
  - cors
  - origin-spoofing
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
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.775Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# MITM-Origin-Spoofing-for-CORS-Bypass

## Summary

This procedure demonstrates performing a Man-in-the-Middle (MITM) attack to intercept unencrypted HTTP requests on local networks, spoof the Origin header to a trusted subdomain, and enable subsequent cross-origin requests by exploiting lax CORS policies that reflect the Origin without validation.

## Description

In scenarios where victims connect to public Wi-Fi or unsecured networks, an attacker can position themselves to intercept traffic to sites like grammarly.com. By redirecting to a spoofed subdomain (e.g., http://evil.grammarly.com) and setting the Origin header to a valid one (e.g., http://www.grammarly.com), the server accepts the request due to its CORS misconfiguration allowing HTTP schemes and subdomains. This sets the stage for injecting malicious payloads. Prerequisites include network proximity and tools like Burp Suite for interception.

## Requirements

1. Access to victim's network (e.g., same Wi-Fi)
2. Burp Suite configured as a transparent proxy
3. Victim's browser must support HTTP downgrades or have unencrypted traffic
4. Target endpoint with reflective CORS (e.g., https://g-mail.grammarly.com)

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS-only connections and HSTS to prevent HTTP interception
- Validate Origin header against a strict whitelist, rejecting HTTP schemes and untrusted subdomains
- Monitor for anomalous Origin headers in server logs
- Use network segmentation to limit MITM opportunities on internal/local networks

## Objectives

1. Spoof origin to bypass CORS preflight checks
2. Establish MITM position for response modification
3. Enable credentialed cross-origin access using victim's cookies

## Instructions

### Step 1: Set Up MITM Proxy

**Context**: Configure Burp Suite to intercept traffic on the network, targeting unencrypted requests to grammarly.com.

**Instructions**: Launch Burp Suite, enable invisible proxying, and use ARP spoofing or Wi-Fi evil twin if needed to route traffic through your machine.

### Step 2: Intercept and Modify Request

**Context**: Capture the victim's request and alter it to spoof the origin.

**Instructions**: In Burp's Proxy tab, intercept the request, change the Host to evil.grammarly.com, set Origin: http://www.grammarly.com, and issue a 302 redirect in the response to load the spoofed page.

> This tricks the browser into believing the request came from a trusted subdomain, allowing CORS headers to reflect and permit credentials.

**Expected Output**: Browser follows redirect, and subsequent requests include the spoofed Origin, accepted by the server with Access-Control-Allow-Origin: http://www.grammarly.com and Access-Control-Allow-Credentials: true.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- mitm
- cors
- origin-spoofing
