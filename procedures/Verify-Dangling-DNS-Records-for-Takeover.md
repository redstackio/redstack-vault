---
id: proc-uuid-002
tags:
  - subdomain-takeover
  - dns-verification
  - heroku
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - Heroku
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T05:32:23.001Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Verify-Dangling-DNS-Records-for-Takeover

## Summary

This procedure verifies if a discovered subdomain points to an unclaimed resource on a third-party service like Heroku, confirming a subdomain takeover opportunity by checking for service-specific error messages.

## Description

Subdomain takeover occurs when a DNS record points to a deleted or unclaimed resource on a cloud provider. By accessing the subdomain in a browser, testers can confirm if it's vulnerable. In the Gratipay case, 'www.gratipay.com.herokudns.com' returned Heroku's 'No such app' error, indicating an attacker could claim it to host phishing or malicious content. This step requires no tools beyond a web browser and assumes the subdomain was previously enumerated.

## Requirements

1. Web browser (e.g., Firefox, Chrome)
2. Public access to the subdomain URL
3. Knowledge of the service's error messages (e.g., Heroku's unclaimed app response)

## Defense

Defensive measures and detection strategies:

- Delete unused DNS records promptly after decommissioning apps
- Monitor for subdomain resolution errors using DNS logging tools like BIND or PowerDNS
- Implement subdomain validation scripts to check for takeovers periodically

## Objectives

1. Confirm the subdomain resolves but serves no active content
2. Identify the hosting service and its claim status
3. Assess the potential for malicious use

## Instructions

### Step 1: Access Subdomain in Browser

**Context**: Navigate to the suspicious subdomain to observe the response from the hosting service.

No command; use a browser to visit the URL.

> Enter 'http://www.gratipay.com.herokudns.com' (or HTTPS if applicable). Expected output is an error page from Heroku stating 'No such app', confirming it's unclaimed and takeover-eligible.

### Step 2: Document and Validate

**Context**: Screenshot or note the error for reporting; optionally use curl for scripted verification.

**Command** (optional, for automation):
```bash
curl -I http://www.gratipay.com.herokudns.com
```

> Look for HTTP 404 or service-specific headers indicating no app exists.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[dns-verification]]
