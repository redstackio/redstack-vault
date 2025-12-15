---
id: proc-intercept-delete-burp
tags:
  - request-interception
  - burp-proxy
  - fabric-io
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
updated_at: '2025-12-14T17:28:58.773Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-DELETE-Request-with-Burp-Proxy

## Summary

Use Burp Proxy to capture a legitimate DELETE request for member removal in the attacker's own organization, obtaining the format for modification.

## Description

Logged in as ex-admin (Hackeradmin), navigate to own HackerOrg settings and trigger a member removal to intercept the API request. This provides the template for the exploit. The procedure relies on Burp Suite for traffic interception in a web session to fabric.io.

## Requirements

1. Burp Suite installed and running
2. Browser proxy configured to 127.0.0.1:8080
3. Hackeradmin session active

## Defense

Defensive measures and detection strategies:

- Monitor for unusual proxy traffic or tool signatures
- Rate-limit API requests to detect interception attempts

## Objectives

1. Capture exact DELETE endpoint and headers
2. Verify request succeeds in own org
3. Prepare for parameter tampering

## Instructions

### Step 1: Configure and Login

**Context**: Set up interception and authenticate.

Start Burp Proxy, set browser to use it, log in to fabric.io as Hackeradmin.

**Expected Output**: Active session with access to HackerOrg.

### Step 2: Trigger and Intercept Request

**Context**: Perform a removal action to capture the DELETE.

Go to settings > organizations > HackerOrg > Team members, click 'x' on Hackermember to remove, intercept in Burp.

**Expected Output**: Captured request: `DELETE /api/v3/accounts/54c1e78b9ea696b3cb00026a/organizations/54aa36e3937ae35559011d17/leave HTTP/1.1 Host: fabric.io` with auth headers.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[request-interception]]
- [[burp-proxy]]
