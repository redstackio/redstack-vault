---
tags:
  - poc
  - verification
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-access-url]]'
platforms:
  - Web
  - AWS
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 5abc8396-5fdb-4614-b9a2-27f692333e83
created_at: '2025-12-14T04:51:26.415Z'
updated_at: '2025-12-14T04:51:26.415Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Subdomain-Takeover-with-POC

## Summary

This procedure validates a subdomain takeover by accessing the controlled subdomain and confirming it serves the attacker's hosted content.

## Description

After claiming the S3 bucket, traffic to the subdomain (e.g., blog.gnipcentral.com) should redirect to the attacker's S3 path (e.g., /asd/index.html). This POC demonstrates control, potentially showing a custom page or redirect to a malicious site. It confirms the exploit's success and highlights risks like phishing under the trusted domain.

## Requirements

1. Successful bucket claim and content upload
2. Network access to the subdomain
3. Browser or curl for testing

## Defense

Defensive measures and detection strategies:

- Monitor subdomain traffic for unexpected redirects
- Use certificate transparency logs to detect unauthorized subdomains
- Implement DNSSEC to prevent CNAME spoofing

## Objectives

1. Confirm redirection to attacker-controlled content
2. Document proof for reporting
3. Assess potential for further abuse

## Instructions

### Step 1: Access and Observe Redirect

**Context**: Test the subdomain URL to verify it resolves to the uploaded content.

**Command** ([[commands/curl-access-url]]):
```bash
curl -L http://blog.gnipcentral.com/
```

> Follows redirects (-L flag) and displays the content from the S3 bucket, proving takeover.

### Step 2: Validate in Browser

**Context**: Manually inspect for visual confirmation.

**Command** (No CLI; use browser):
Navigate to http://blog.gnipcentral.com/ and observe the served page.

> Expect the POC HTML (e.g., <h1>POC Takeover</h1>) or redirect behavior.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-url]]

## Tools Used


## Tags

- [[poc]]
- [[subdomain-takeover]]
