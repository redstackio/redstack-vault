---
id: proc-uuid-5678
name: Bypass-IDOR-via-HTTP-Method-Switch
tags:
  - idor
  - http-method-bypass
  - access-control
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-method-switch]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:34.141Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-IDOR-via-HTTP-Method-Switch

## Summary

This procedure exploits an Insecure Direct Object Reference (IDOR) vulnerability in the IBM Your Learning endpoint by switching the HTTP request method from the expected POST or PUT to GET, bypassing access controls and allowing unauthorized retrieval of other users' sensitive data objects.

## Description

In the IBM Your Learning application, the endpoint handling direct object references (e.g., /api/learning/objects/{id}) enforces access controls only for specific HTTP methods like POST or PUT. By changing the method to GET, an attacker can bypass these checks, directly accessing objects belonging to other users. This was discovered during security testing and reported via HackerOne, resulting in a critical severity rating (9.3) due to potential data exposure. The procedure assumes the attacker has initial authenticated access to the application and knowledge of object IDs, which can be enumerated or guessed.

## Requirements

1. Authenticated session to IBM Your Learning (valid token or cookies)
2. Knowledge of the vulnerable endpoint URL and object ID format
3. Tool for HTTP request manipulation (e.g., curl or Burp Suite)
4. Network access to the target service over HTTPS

## Defense

Defensive measures and detection strategies:

- Implement method-agnostic access controls that validate object ownership regardless of HTTP method
- Use proper authorization checks on all endpoints, including GET requests
- Monitor for anomalous HTTP method usage in application logs (e.g., unexpected GETs to mutation endpoints)
- Employ Web Application Firewalls (WAF) to detect method tampering patterns

## Objectives

1. Bypass IDOR protections to access unauthorized objects
2. Retrieve sensitive user data such as learning profiles or records
3. Demonstrate the vulnerability for reporting and remediation

## Instructions

### Step 1: Identify Vulnerable Endpoint and Object ID

**Context**: Locate the IDOR-affected endpoint in IBM Your Learning, typically something like /api/learning/objects/{id}, and obtain an object ID belonging to another user through enumeration or prior discovery.

**Command** ([[commands/curl-method-switch]]):
```bash
curl -X POST -H "Authorization: Bearer your-token" "https://yourlearning.ibm.com/api/learning/objects/target-id" -d '{}' -v
```

> This sends a legitimate POST request to confirm the expected behavior (e.g., 200 OK for owned objects, 403 for unauthorized). Note the method and response to prepare for switching.

### Step 2: Switch HTTP Method to Bypass Controls

**Context**: Intercept or craft a request identical to the legitimate one but change the method to GET, targeting an unauthorized object ID. This exploits the inadequate protection against method switching.

**Command** ([[commands/curl-method-switch]]):
```bash
curl -X GET -H "Authorization: Bearer your-token" "https://yourlearning.ibm.com/api/learning/objects/other-user-id" -v
```

> The switched request should return the object's data (e.g., JSON with user-sensitive info) without triggering access denial, confirming the bypass. Use -v for verbose output to inspect headers and status codes.

### Step 3: Validate Unauthorized Access

**Context**: Confirm the impact by checking the response for data not belonging to the authenticated user, such as another user's learning history.

**Command** ([[commands/curl-method-switch]]):
```bash
curl -X GET -H "Authorization: Bearer your-token" "https://yourlearning.ibm.com/api/learning/objects/other-user-id" | jq '.'
```

> Parse the JSON output (using jq if available) to verify sensitive fields like user IDs or content. Successful exploitation shows data exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-method-switch]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- idor
- http-method-bypass
- access-control
