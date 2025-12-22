---
tags:
  - subdomain-takeover
  - unbounce
  - verification
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:24.209Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 0eb4d3ba-9e9f-4926-86c0-9b905de4ef60
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Subdomain-Availability-on-Unbounce

## Summary

This procedure confirms whether a subdomain linked via CNAME to Unbounce is claimed or available for registration, a critical step in assessing subdomain takeover feasibility without executing the takeover.

## Description

Following DNS discovery of a CNAME pointing to unbouncepages.com, this manual verification involves contacting Unbounce support to check if the parent domain (e.g., udemy.com) is registered on their platform. If unclaimed, an attacker could sign up and point custom HTML/JavaScript to the subdomain, enabling phishing sites mimicking Udemy or XSS attacks on visitors. This targets web-based landing pages and requires no technical tools beyond a browser for support chat. Outcomes include confirmation of vulnerability, highlighting risks like arbitrary content hosting on trusted subdomains.

## Requirements

1. Access to Unbounce support channels (chat, email)
2. Details of the discovered CNAME (subdomain and service)
3. Ethical disclosure mindset to avoid unauthorized actions

## Defense

Defensive measures and detection strategies:

- Monitor third-party service dashboards for unlinked domains
- Automate availability checks during DNS audits
- Train teams to promptly claim or remove dangling records

## Objectives

1. Confirm unclaimed status on Unbounce for the target subdomain
2. Evaluate potential for malicious content deployment
3. Document evidence for vulnerability reporting

## Instructions

### Step 1: Access Unbounce Support

**Context**: Navigate to Unbounce's support portal to initiate verification without attempting registration.

**Command** ():

> Open a browser and go to https://unbounce.com/support or start a live chat. No command-line tool is needed; this is a manual web interaction.

### Step 2: Inquire About Domain Claim

**Context**: Provide specific details to support and request confirmation of the domain's status.

**Command** ():

> In the chat, state: "I noticed a CNAME for landing.udemy.com pointing to unbouncepages.com. Is udemy.com or this subdomain currently linked or claimed on your platform?" Expected response: Confirmation that it is not linked, indicating availability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[unbounce]]
- [[verification]]
