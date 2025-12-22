---
tags:
  - idor
  - recon
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/burp-intercept-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:23.546Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: bb7ca395-22fb-4e88-8765-104af536d7d2
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-IDOR-Vulnerable-Endpoint

## Summary

This procedure involves reconnaissance on a web application to identify endpoints susceptible to Insecure Direct Object Reference (IDOR) vulnerabilities, where object identifiers like user IDs or content IDs are directly exposed and manipulable without access controls.

## Description

In the context of the DoD website, IDOR allows attackers to access or manipulate objects they shouldn't by simply changing parameters in requests. This procedure uses web proxy tools to intercept traffic and test for predictable references, targeting public-facing web objects. Prerequisites include basic web navigation knowledge and a proxy setup. Expected outcomes are confirmation of vulnerable endpoints leading to unauthorized data access.

## Requirements

1. Access to the target web application (e.g., DoD website)
2. Web proxy tool like Burp Suite installed and configured
3. Valid session cookie if authentication is required for endpoints

## Defense

Defensive measures and detection strategies:

- Implement indirect object references (e.g., hashed IDs) and server-side access checks
- Monitor for anomalous parameter values in logs (e.g., sequential ID jumps)
- Use Web Application Firewalls (WAF) to detect parameter tampering

## Objectives

1. Locate endpoints using direct object references
2. Test for missing authorization checks
3. Confirm potential for unauthorized access

## Instructions

### Step 1: Setup Proxy and Intercept Traffic

**Context**: Configure a proxy to capture requests while interacting with the target website, focusing on pages that display or manage user-specific content.

**Command** ([[commands/burp-intercept-request]]):
```bash
# Launch Burp Suite and configure browser proxy to 127.0.0.1:8080
# Browse to DoD website and navigate to content management sections
# In Burp Proxy, intercept a request like GET /user/profile?id=123
```

> This captures the baseline request. Analyze the response for object-specific data.

### Step 2: Test Parameter Manipulation

**Context**: Modify the object identifier in the intercepted request to access other objects, checking if authorization is enforced.

**Command** ([[commands/burp-intercept-request]]):
```bash
# In Burp Repeater, change id=123 to id=124 and forward the request
GET /user/profile?id=124 HTTP/1.1
Host: dod-website.example
Cookie: session=valid_session
```

> If the response returns data for id=124 without errors, IDOR is confirmed. Repeat with various IDs to map accessible objects.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/burp-intercept-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[idor]]
- [[recon]]
