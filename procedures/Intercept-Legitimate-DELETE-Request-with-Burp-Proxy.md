---
tags:
  - intercept
  - proxy
  - http
type: procedure
tools:
  - '[[tools/Burp-Proxy]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/fabric-delete-team-member-original]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:44.806Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
id: 249cf723-ae17-458e-a361-f6db2c40bcc9
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Intercept-Legitimate-DELETE-Request-with-Burp-Proxy

## Summary

This procedure uses Burp Proxy to capture a legitimate HTTP DELETE request for removing a team member from an authorized Fabric.io application, allowing analysis of the request format for later tampering.

## Description

Authenticated as an app admin, the attacker navigates to the team management interface and initiates a deletion, routing traffic through Burp Proxy to intercept the request. The captured request reveals parameters like account_id, app_id, and admin=true, which are essential for understanding the endpoint's structure. This step occurs in the attacker's own app to avoid immediate detection.

## Requirements

1. Burp Proxy running and browser configured to use it (e.g., localhost:8080)
2. Valid admin session in HackerApp
3. Access to HackerApp team settings

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS with HSTS to prevent proxy interception in production
- Log all DELETE requests with full parameters for audit
- Detect unusual proxy traffic patterns via WAF

## Objectives

1. Capture baseline DELETE request structure
2. Identify modifiable parameters for bypass
3. Ensure legitimate deletion for cover

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up interception to route Fabric.io traffic through Burp.

Launch Burp Suite, enable Intercept in Proxy tab, and set browser proxy to 127.0.0.1:8080. Install Burp CA certificate in browser.

**Expected Output**: Traffic from fabric.io visible in Burp.

### Step 2: Initiate Legitimate Deletion

**Context**: Trigger the DELETE action to capture the request.

Log in as Hackeradmin, go to HackerApp > Settings > Team, select Hackermember, and click delete. Intercept the request in Burp.

**Command** ([[commands/fabric-delete-team-member-original]]):

The intercepted request is:

```http
DELETE /accounts/54aa37d8f61d7749430127ee?admin=true&app_id=54aeafc28bfc55053d000028 HTTP/1.1
Host: fabric.io
```

> This command deletes Hackermember from HackerApp. Expected output: 200 OK or similar success response.

### Step 3: Forward and Verify

**Context**: Allow the request to proceed and confirm deletion.

Forward in Burp and check HackerApp team list.

**Expected Output**: Hackermember removed.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used

- [[commands/fabric-delete-team-member-original]]

## Tools Used

- [[tools/Burp-Proxy]]

## Tags

- intercept
- proxy
- http
