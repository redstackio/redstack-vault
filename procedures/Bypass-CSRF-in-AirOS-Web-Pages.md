---
tags:
  - csrf
  - bypass
  - airos
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Embedded Device
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:35.851Z'
sub_techniques: []
id: 8f53ce04-72f2-4e0a-9276-65cdcf58cfd8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-CSRF-in-AirOS-Web-Pages

## Summary

This procedure exploits the lack of CSRF validation in certain web pages of the AirOS interface on Ubiquiti PowerBeam M5 300 devices, allowing unauthorized modification of device configuration without proper tokens.

## Description

In AirOS 6.1.5 and prior, specific web endpoints fail to enforce CSRF protections, enabling attackers to send forged requests from external sites. This is particularly effective against authenticated users via social engineering, leading to unauthorized config changes that set up further exploits like XSS injection. The target environment is the device's web UI, typically accessible on port 80/443, and requires no special tools beyond a browser or scripting capability.

## Requirements

1. Network access to the AirOS web interface
2. Knowledge of vulnerable endpoints (e.g., config update pages)
3. Ability to host or craft a malicious webpage for request submission

## Defense

Defensive measures and detection strategies:

- Implement strict CSRF token validation on all state-changing endpoints
- Use Content Security Policy (CSP) to restrict cross-origin requests
- Monitor for anomalous config changes in device logs

## Objectives

1. Send unauthorized requests to modify device settings
2. Prepare for injection of malicious payloads
3. Gain initial foothold without direct authentication

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Analyze the AirOS web interface to find pages lacking CSRF checks, such as configuration modification forms.

Use browser developer tools to inspect forms and confirm absence of token fields.

### Step 2: Craft Malicious Request

**Context**: Create a simple HTML page that auto-submits a POST request to the vulnerable endpoint.

Example HTML (host on attacker server):

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrf-form" action="http://target-device-ip/cgi-bin/webproc" method="post">
<input type="hidden" name="opt" value="app_config">
<input type="hidden" name="sys_location" value="<script>alert('CSRF Success')</script>">
</form>
<script>document.getElementById('csrf-form').submit();</script>
</body>
</html>
```

> This submits a config change injecting a basic XSS payload; replace with actual vulnerable params from analysis.

### Step 3: Trigger the Bypass

**Context**: Lure the target user to visit the malicious page while authenticated to the device.

Observe if the request succeeds by checking device config or error responses.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[bypass]]
- [[airos]]
