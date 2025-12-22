---
tags:
  - idor
  - bypass
  - manipulation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Persistence]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Account Manipulation]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 18d3c0ac-499b-4287-a443-5756bd58b5e7
created_at: '2025-12-14T17:30:27.268Z'
updated_at: '2025-12-14T17:30:27.268Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Manipulate ID Parameter for IDOR

## Summary

This procedure intercepts HTTP requests to the Autodesk profile edit endpoint and modifies the 'id' parameter to target unauthorized user profiles, exploiting the absence of server-side ownership validation.

## Description

The IDOR vulnerability in Autodesk's photo edit feature stems from direct object referencing via a predictable 'id' parameter in requests. Without checks ensuring the ID matches the authenticated user, attackers can redirect operations to any profile. This step uses request interception to alter the parameter, enabling unauthorized targeting in a web environment.

## Requirements

1. Burp Suite or similar proxy tool intercepting browser traffic
2. Active session from prior access step
3. Target user's ID (e.g., obtained from URL enumeration or public data)

## Defense

Defensive measures and detection strategies:

- Implement server-side checks comparing requested ID to session user ID
- Use randomized UUIDs instead of sequential IDs for object references
- Deploy WAF rules to detect ID parameter tampering and log discrepancies

## Objectives

1. Intercept the request containing the 'id' parameter
2. Substitute with target ID to bypass authorization
3. Validate the bypass by observing server acceptance

## Instructions

### Step 1: Configure Proxy Interception

**Context**: Set up tools to capture and edit requests before they reach the server.

**Instructions**: Launch [[tools/Burp-Suite]], enable Proxy interception (Proxy > Intercept > On). Configure browser proxy settings to route through Burp (127.0.0.1:8080). Navigate to the edit photo page from Step 1 to trigger interception.

### Step 2: Edit and Forward Request

**Context**: Modify the vulnerable parameter in the intercepted traffic.

**Instructions**: In the Burp Intercept tab, locate the 'id' parameter in the GET or POST body/query string (e.g., id=123). Change it to the target ID (e.g., id=456). Click 'Forward' to send the altered request. Drop and retry if needed to test variations.

> Expected: Server responds without authorization denial (e.g., 200 OK instead of 403), indicating successful bypass. Monitor for any client-side JS checks that might need additional disabling via browser console.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- idor
- parameter-manipulation
