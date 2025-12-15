---
id: uuid-1
tags:
  - intercept
  - proxy
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite-Community-Edition]]'
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
updated_at: '2025-12-14T17:24:27.011Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Reddit-AMA-Request-with-Burp

## Summary

This procedure captures a legitimate HTTP POST request to Reddit's AMA form endpoint using Burp Suite's proxy interception, enabling subsequent modification for vulnerability testing.

## Description

In the context of testing for open redirects, intercepting requests during user interaction with the AMA form at www.redditinc.com/ama allows identification of user-controllable parameters like 'failed'. This step requires Burp Suite configured as a proxy in the browser. Expected outcome is a captured multipart/form-data POST request ready for analysis.

## Requirements

1. Burp Suite Community Edition installed and running
2. Browser proxy set to Burp (e.g., 127.0.0.1:8080)
3. Access to www.redditinc.com/ama form

## Defense

Defensive measures and detection strategies:

- Monitor proxy traffic anomalies in web application firewalls (WAF)
- Implement client-side certificate pinning to detect proxy interception

## Objectives

1. Capture legitimate AMA submission request
2. Identify 'failed' parameter in POST body
3. Prepare for request tampering

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up Burp to intercept traffic from the browser.

In Burp Suite, ensure the Proxy tab is active and interception is enabled. Configure your browser to use Burp as proxy.

### Step 2: Interact with AMA Form

**Context**: Trigger the POST request by submitting the form.

Navigate to www.redditinc.com/ama, fill out the form to simulate submission, and allow Burp to intercept the request to /ama.

**Expected Output**: Intercepted request in Burp's Intercept tab showing POST /ama with multipart/form-data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Community-Edition]]

## Tags

- [[intercept]]
- [[proxy]]
- [[web]]
