---
id: proc-claim-subdomain-freshdesk
tags:
  - subdomain-takeover
  - phishing
  - impersonation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-resolve-subdomain]]'
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:23.275Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim-Subdomain-via-Expired-Service

## Summary

This procedure details how to claim control of a dangling subdomain by registering it with an expired third-party service like FreshDesk, allowing hosting of malicious content for phishing or support impersonation.

## Description

Following identification of a dangling record (e.g., service.kiwi.ki pointing to expired FreshDesk), attackers create a new account on the provider and claim the domain via their verification process. This exploits the lack of DNS cleanup after service trials. The target environment is public DNS with SaaS integrations; outcomes include full subdomain control, enabling deployment of fake support pages to phish KIWI customers for credentials. Prerequisites: Free account creation on the service; no advanced skills needed.

## Requirements

1. Access to the third-party service signup (e.g., FreshDesk free trial)
2. Confirmed dangling DNS record from prior reconnaissance
3. Basic web interface navigation for domain addition

## Defense

Defensive measures and detection strategies:

- Expire and remove DNS records immediately after SaaS trials
- Use subdomain monitoring tools like certificate transparency logs to detect takeovers
- Implement wildcard certificates or strict subdomain policies to limit impact

## Objectives

1. Gain control of the subdomain through service claiming
2. Deploy malicious content to impersonate legitimate services
3. Achieve phishing or data exfiltration from users

## Instructions

### Step 1: Register New Service Account

**Context**: Create a fresh account on the provider to initiate the claiming process.

No command; use web browser to sign up at freshdesk.com and start a free trial.

### Step 2: Add and Verify Custom Domain

**Context**: Input the dangling subdomain during setup to claim it automatically via existing DNS.

No command; in the dashboard, go to Settings > Domains > Add Custom Domain, enter 'service.kiwi.ki', and verify (DNS already points correctly, so it claims instantly).

### Step 3: Test and Deploy Content

**Context**: Confirm control and upload phishing pages.

**Command** ([[commands/curl-resolve-subdomain]]):
```bash
curl -I http://service.kiwi.ki/
```

> After claiming, this should return your custom page headers. Expected output: 200 OK with attacker content. Then, customize the FreshDesk portal with phishing forms mimicking KIWI support.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-resolve-subdomain]]

## Tools Used


## Tags

- [[Phishing]]
- [[domain-hijacking]]
