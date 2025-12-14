---
tags:
  - path-disclosure
  - information-disclosure
  - beaker
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/send-long-session-id-cookie-for-path-disclosure]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:48.352Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 667d7512-33ee-41f2-b402-7db896134f96
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Trigger-Path-Disclosure-with-Long-Session-ID

## Summary

This procedure exploits the lack of validation on the beaker.session.id cookie in the EdgeRouter web management portal by sending a value of 250+ characters, triggering an error page that discloses internal file paths like /var/run/beaker/container_file/.

## Description

The Beaker session management in the Python-based web portal stores sessions as files in /var/run/beaker/container_file/. When a session ID exceeds 249 characters, it fails to create the file properly, resulting in a Python traceback or 500 error that exposes full server paths. This aids attackers in understanding the filesystem structure for further exploitation. The target is the unauthenticated GET / endpoint on the management interface.

## Requirements

1. Network access to the EdgeRouter management IP (e.g., 192.168.1.1 on ports 80/443)
2. HTTP client capable of setting custom cookies (e.g., curl, browser dev tools)
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Implement cookie length validation (limit to <250 characters) in the web application
- Configure error pages to suppress tracebacks and paths (e.g., custom 500 handler in Python)
- Monitor for anomalous long cookie requests in web logs
- Enable filesystem monitoring on /var/run for unusual file creation attempts

## Objectives

1. Reveal internal paths to map the target's filesystem
2. Validate the vulnerability for subsequent DoS escalation
3. Gather reconnaissance without authentication

## Instructions

### Step 1: Craft and Send Request

**Context**: Prepare an HTTP GET to the root path with an oversized beaker.session.id to force session storage failure and error exposure.

**Command** ([[commands/send-long-session-id-cookie-for-path-disclosure]]):
```bash
curl -X GET "http://192.168.1.1/" -H "Cookie: beaker.session.id=v8iG24fDKn8x5uD3V2uICZA1FJEoUJpqH5VTa03xB5blDRNOe5AfFp2GNIBpDX8th1IO8sS5ejsz4Swm175nUvipwU211S4n4RtCv0A6r18fsgJbrrbmhFT9k2cAXF3yyg0Uu0B0wPOWP7BOrMVnXp44aHoXSfJ06ZXk7HrD5J5R9AZIgQLmGutM9ESNxw3CVJtW4Rfxeh7JE2AD04B3g78FxRgBxY82I2Gzf6ZPMsc39d37LM90dd9cFA" -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -v
```

> This command sends a 250+ character random string as the session ID, causing Beaker to fail file creation and output a traceback. Expected output includes paths like /var/run/beaker/container_file/ in the error response.

### Step 2: Analyze Response

**Context**: Inspect the server response for disclosed paths.

No specific command; parse the curl verbose output or response body for traceback elements indicating file paths.

> Look for lines mentioning 'FileNotFoundError' or similar with absolute paths starting from /var/run/.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/send-long-session-id-cookie-for-path-disclosure]]

## Tools Used


## Tags

- path-disclosure
- information-disclosure
- edgerouter
