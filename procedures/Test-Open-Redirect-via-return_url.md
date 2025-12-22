---
id: proc-adobe-open-redirect-test
tags:
  - open-redirect
  - phishing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-redirect]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Phishing]]'
updated_at: '2025-12-14T03:15:52.945Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Phishing]]'
---
# Test Open Redirect via return_url

## Summary

This procedure tests the return_url parameter for open redirect vulnerability by injecting external URLs, allowing attackers to redirect authenticated users to malicious sites for phishing credential theft.

## Description

The Adobe Youth Voices login page at http://youthvoices.adobe.com/community processes return_url without validating the domain or protocol, permitting protocol-relative URLs like //www.google.com. After a victim logs in or registers using the crafted link, they are redirected externally. This enables phishing by pointing to fake login pages mimicking Adobe's site. Testing requires simulating user interaction; impacts include unauthorized access to credentials.

## Requirements

1. Web browser for crafting and testing URLs.
2. Access to the target endpoint.
3. Optional: A controlled external site for redirect target.

## Defense

Defensive measures and detection strategies:

- Validate return_url against a whitelist of allowed domains.
- Strip or encode protocol-relative and external schemes.
- Monitor for redirects to untrusted domains in server logs.

## Objectives

1. Confirm arbitrary redirect capability.
2. Demonstrate phishing vector.
3. Assess potential for credential harvest.

## Instructions

### Step 1: Craft Redirect Payload

**Context**: Build the malicious URL using protocol-relative scheme to bypass basic checks.

Execute [[commands/curl-test-redirect]] to simulate the request:

```bash
curl -L "http://youthvoices.adobe.com/community?return_url=//www.attacker.com/phish" -c cookies.txt
```

> This follows the redirect (-L) and saves cookies; in a real attack, send the URL to victim via email/social engineering.

### Step 2: Simulate Victim Authentication

**Context**: After victim clicks and logs in, observe the redirect.

Manually access the crafted URL, complete login, and verify redirection to attacker.com.

> Expected: Browser navigates away from Adobe site to external domain post-auth.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Phishing]] Phishing

### Sub-Techniques


## Commands Used

- [[commands/curl-test-redirect]]

## Tools Used


## Tags

- [[open-redirect]]
- [[Phishing]]
