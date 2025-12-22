---
tags:
  - verification
  - takeover
  - gitlab
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:38:49.258Z'
sub_techniques: []
id: 482d12f5-c56b-49f8-86b1-b311863f181a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify Subdomain Takeover on GitLab Pages

## Summary

This procedure validates a successful subdomain takeover by accessing the dangling domain and confirming that the attacker's GitLab Pages content is served, including any redirects or responses.

## Description

Post-domain addition, GitLab proxies requests to the attacker's site. Verification involves HTTP access to check for content loading, redirects (e.g., 302 to HTTPS), and GitLab-specific responses (e.g., 401). Used to confirm exploit success in takeover attacks. Target: Taken-over subdomain; prerequisites: Domain added. Outcomes: Proof of control, enabling further attacks like phishing.

## Requirements

1. Web browser or curl for access testing
2. Successful prior steps (domain added)
3. Knowledge of expected attacker content

## Defense

Defensive measures and detection strategies:

- Set up domain monitoring for unexpected content changes
- Use certificate transparency logs to detect unauthorized TLS issuance
- Implement CSP and CORS strictly on subdomains

## Objectives

1. Confirm content serving on victim domain
2. Validate proxying and redirects
3. Assess impact (e.g., load malicious JS)

## Instructions

### Step 1: Access the Domain

**Context**: Visit the subdomain over HTTP to trigger serving.

**Command** (Browser or curl):
```bash
curl -i http://docs-dev.gitlab.com/
```

> Expected: 302 redirect to HTTPS, then 401 or content from attacker's site.

### Step 2: Inspect Response

**Context**: Check for GitLab Pages indicators and custom content.

**Command** (Follow-up curl):

> If redirected, follow to HTTPS; success if attacker HTML/JS loads.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[takeover]]
- [[gitlab]]
