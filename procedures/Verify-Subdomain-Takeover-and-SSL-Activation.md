---
tags:
  - verification
  - ssl
  - takeover-confirmation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:51:26.541Z'
sub_techniques: []
id: 83d2589f-c29e-476d-a019-3c855cd061dd
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Verify-Subdomain-Takeover-and-SSL-Activation

## Summary

This procedure confirms the subdomain takeover by accessing the hijacked domain and ensuring it serves controlled content under HTTPS, validating full control and SSL functionality.

## Description

After claiming, verification involves browsing the subdomain to load Ghost content and checking the certificate. This step ensures the attack's success in a web/DNS context, allowing for phishing or misinformation deployment. It requires no tools beyond a browser and confirms the impact on the target's brand.

## Requirements

1. Completed DNS configuration in Ghost
2. Web browser for access
3. Time for SSL propagation (5-10 minutes)

## Defense

Defensive measures and detection strategies:

- Set up alerts for DNS resolution changes on critical subdomains
- Use browser extensions or tools to monitor subdomain content shifts
- Regularly test SSL certificates for unauthorized issuances

## Objectives

1. Confirm resolution to attacker-controlled content
2. Validate SSL certificate validity
3. Assess potential for exploitation (e.g., phishing)

## Instructions

### Step 1: Access the Subdomain

**Context**: Load the HTTPS URL to check content serving.

No command; open https://engineering.udemy.com in a browser.

> Expected: Ghost publication content loads instead of original or error.

### Step 2: Inspect SSL and Content

**Context**: Verify certificate and ensure no errors.

No command; click the padlock icon to view certificate details.

> Success if certificate is valid (issued by Ghost/Let's Encrypt) and content is customizable.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Hardware]] Gather Victim Host Information: DNS

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[ssl]]
- [[takeover-confirmation]]
