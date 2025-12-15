---
tags:
  - burp-suite
  - intercept
  - http-history
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:07.443Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: b80cc117-ca55-4c29-874c-b3aa9760400f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture-Note-Saving-Request-with-Burp-Suite

## Summary

This procedure uses Burp Suite to intercept and log the HTTP POST request for saving notes on Tucows, enabling analysis for CSRF exploitation.

## Description

With Burp Suite configured as a proxy, the save action is performed, and the request appears in the HTTP history tab. This captures details like the endpoint, parameters (ajax=save_note, etc.), and lack of CSRF tokens, confirming vulnerability. Targeted at web apps, prerequisites include proxy setup in the browser.

## Requirements

1. Burp Suite installed and running
2. Browser proxy set to Burp (e.g., 127.0.0.1:8080)
3. Active Tucows session

## Defense

Defensive measures and detection strategies:

- Deploy web application firewalls (WAF) to detect proxy interception patterns
- Encrypt traffic with HSTS to hinder interception

## Objectives

1. Log the vulnerable POST request
2. Verify parameter structure
3. Prepare for PoC generation

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp to intercept traffic.

Launch Burp Suite and ensure the proxy listener is active on port 8080.

> Configure browser to use this proxy for all traffic.

### Step 2: Perform Save and Check History

**Context**: Trigger request and view in Burp.

Save a note on Tucows; switch to Burp's HTTP history tab to locate the POST.

> Expected: Request details including body with ajax=save_note.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- burp-suite
- intercept
