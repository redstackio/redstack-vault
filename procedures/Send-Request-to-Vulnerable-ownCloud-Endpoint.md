---
tags:
  - xss
  - web
  - http
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-send-referer-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:08.020Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b19774e7-ac13-4555-8d6c-2f230595e74e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send-Request-to-Vulnerable-ownCloud-Endpoint

## Summary

This procedure sends an HTTP GET request to vulnerable ownCloud endpoints with a malicious Referer header, causing the server to reflect the payload into the response HTML.

## Description

Target endpoints such as /messages/?action=newmessage&username=anderslund or /usermanager/edit.php?key=... directly insert the Referer into an onclick attribute. Using tools like curl, attackers simulate a request from a malicious site. Expected outcome: The response includes the unescaped payload, setting up for XSS execution. This requires network access to the public-facing app and no authentication for the endpoints.

## Requirements

1. Network connectivity to https://apps.owncloud.com
2. Crafted malicious Referer from prior procedure
3. HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Implement Referer header validation or stripping on the server
- Use HTTPS and HSTS to limit Referer leakage
- Log and alert on suspicious Referer patterns (e.g., containing script tags)

## Objectives

1. Deliver the payload to the reflection point
2. Receive a response with reflected content
3. Confirm no sanitization occurred

## Instructions

### Step 1: Prepare the Request

**Context**: Set up the HTTP client with the malicious Referer.

Use [[commands/curl-send-referer-xss]] for the GET request.

### Step 2: Execute the Request

**Context**: Send to one of the vulnerable URLs and capture the response.

**Command** ([[commands/curl-send-referer-xss]]):
```bash
curl -H "Referer: http://www.myevilsite.com/qwe';alert(1)+'" -v https://apps.owncloud.com/messages/?action=newmessage&username=anderslund
```

> The -v flag shows headers; inspect the response body for the onclick reflection. Expected: HTML with onclick="location.href='malicious payload'".

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-send-referer-xss]]

## Tools Used


## Tags

- xss
- http
