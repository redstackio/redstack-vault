---
tags:
  - takeover-verification
  - subdomain-control
  - xss-phishing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud (Azure)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:01.991Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 6209a3ff-a07e-4869-96a0-fd3774e02a26
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify Subdomain Takeover and Control

## Summary

This procedure tests the takeover by accessing the subdomain and confirming the ability to serve custom content, validating impacts like SOP bypass for XSS or phishing.

## Description

Post-registration, the subdomain's traffic routes to the attacker's App Service. Accessing http:// and https:// versions ensures full control, allowing arbitrary HTML/JS serving for malicious purposes.

## Requirements

1. Claimed App Service with deployed content (e.g., a simple index.html)
2. Browser or curl for testing
3. Subdomain URL (e.g., datacafe-cert.starbucks.com)

## Defense

Defensive measures and detection strategies:

- Implement subdomain isolation with strict CSP
- Monitor traffic anomalies on subdomains
- Use certificate pinning to detect hijacks

## Objectives

1. Confirm DNS resolution to attacker resource
2. Validate content serving capability
3. Assess potential for further exploits

## Instructions

### Step 1: Deploy Test Content

**Context**: Upload a simple page to the App Service.

**Command** (Via Azure portal or FTP):

No CLI; use Azure portal to deploy index.html with "Takeover Successful" message.

> Ensures content is live on the service.

### Step 2: Access Subdomain URLs

**Context**: Test HTTP and HTTPS access to verify control.

**Command** ([[commands/curl-access]]):

```bash
curl -k http://datacafe-cert.starbucks.com/
curl -k https://datacafe-cert.starbucks.com/
```

> Returns custom content, confirming takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-access]]

## Tools Used

- Browser or curl

## Tags

- [[takeover-verification]]
- [[subdomain-control]]
