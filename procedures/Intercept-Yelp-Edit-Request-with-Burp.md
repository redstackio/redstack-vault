---
id: proc-intercept-yelp-edit-001
tags:
  - intercept
  - proxy
  - burp
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:23.168Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Intercept-Yelp-Edit-Request-with-Burp

## Summary

This procedure uses Burp Suite to intercept the HTTP GET request triggered by clicking the edit button on a Yelp profile location, capturing the vulnerable locid parameter for later modification in an IDOR attack.

## Description

In the context of Yelp's web application, editing a saved location generates a GET request to /profile_location/add_or_edit with parameters including nonce and locid. By proxying traffic through Burp Suite, the attacker can pause and inspect this request. This targets web browsers interacting with Yelp's frontend and backend, requiring an active authenticated session. Successful interception allows visibility of the locid hash, which can be manipulated to access other users' data due to missing access controls.

## Requirements

1. Burp Suite installed and running as a proxy
2. Browser configured to route traffic through Burp (e.g., proxy on 127.0.0.1:8080)
3. Active Yelp session from prior login

## Defense

Defensive measures and detection strategies:

- Use HTTPS everywhere to encrypt traffic, though proxy interception still possible with MITM
- Implement client-side request signing or CSRF tokens to detect tampering
- Log and alert on proxy-like user agents or unusual request patterns

## Objectives

1. Capture the edit request containing the locid parameter
2. Pause the request for inspection and modification
3. Prepare for IDOR exploitation by analyzing the parameter structure

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up Burp Suite to intercept browser traffic.

No specific command; launch Burp Suite, ensure the proxy listener is active on port 8080, and configure the browser's proxy settings accordingly.

> Burp's proxy tab shows incoming traffic; enable interception for GET requests to yelp.com.

### Step 2: Trigger and Intercept Edit Request

**Context**: Interact with the profile locations page to generate the target request.

No specific command; on https://www.yelp.com/profile_location, click the edit button for a saved location.

> The request to /profile_location/add_or_edit?nonce=<nonce>&locid=<locid> is intercepted and held in Burp.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- intercept
- proxy
- burp
- web
