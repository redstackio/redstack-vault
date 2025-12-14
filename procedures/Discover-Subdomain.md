---
tags:
  - reconnaissance
  - subdomain-enumeration
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T03:47:18.409Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 1f33460d-cd6c-40e8-91c3-7744cb6f8c94
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Discover-Subdomain

## Summary

This procedure involves identifying exposed subdomains associated with a target domain, such as during reconnaissance for Ubiquiti applications, to uncover potential attack surfaces like the dev-ucrm-billing-demo.ubnt.com billing demo.

## Description

In the context of web application testing, subdomain discovery expands the attack surface by revealing hidden or development instances. For this attack, the subdomain https://dev-ucrm-billing-demo.ubnt.com/ was identified while enumerating Ubiquiti subdomains, leading to the discovery of the stored XSS vulnerability. This step requires no special tools beyond browser access and is typically manual during initial testing.

## Requirements

1. Access to the internet and target domain (ubnt.com).
2. Basic knowledge of DNS and web navigation.
3. Optional: Subdomain enumeration tools like subfinder or Amass for automation.

## Defense

Defensive measures and detection strategies:

- Implement DNS monitoring to detect anomalous subdomain resolutions.
- Use web application firewalls (WAF) to block access to dev/staging environments from unauthorized IPs.
- Regularly audit exposed subdomains with tools like dnsdumpster or security scanners.

## Objectives

1. Identify live subdomains for further testing.
2. Prioritize development or demo instances as they often have weaker security.
3. Establish the initial attack vector without alerting defenses.

## Instructions

### Step 1: Manual Subdomain Identification

**Context**: Start with known domains and check for common subdomain patterns like 'dev' or 'demo'.

No specific command; use browser to visit https://dev-ucrm-billing-demo.ubnt.com/ or query DNS.

> Manually append 'dev-ucrm-billing-demo' to ubnt.com and verify resolution. Expected output: Page loads with login form.

### Step 2: Verify Accessibility

**Context**: Confirm the subdomain is live and not behind access controls.

Use browser developer tools to inspect the response.

> Load the URL in a browser. Expected output: HTTP 200 response with application login page.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[subdomain-enumeration]]
