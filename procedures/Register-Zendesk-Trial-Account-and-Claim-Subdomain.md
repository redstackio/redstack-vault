---
id: proc-uuid-2
tags:
  - zendesk
  - account-creation
  - subdomain-claim
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
updated_at: '2025-12-14T05:32:23.602Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Register Zendesk Trial Account and Claim Subdomain

## Summary

This procedure creates a free trial account on Zendesk and claims an available subdomain, exploiting unclaimed CNAMEs for takeover.

## Description

After detecting a vulnerable subdomain, register a new Zendesk instance using the unclaimed subdomain name. This grants control over the pointed domain, allowing custom content hosting in web-based support platforms. Prerequisites include confirmed availability from prior DNS checks.

## Requirements

1. Valid email for trial signup
2. Confirmed subdomain availability
3. Web browser access to Zendesk

## Defense

Defensive measures and detection strategies:

- Proactively claim and monitor subdomains on services like Zendesk
- Use enterprise Zendesk plans with custom domain locks
- Alert on new subdomain registrations matching owned domains

## Objectives

1. Gain initial control of the subdomain via free account
2. Establish Zendesk instance under the vulnerable name
3. Prepare for domain mapping

## Instructions

### Step 1: Initiate Signup

**Context**: Start the Zendesk trial registration process.

Navigate to the Zendesk signup page and enter your email to begin.

> Expected: Prompt for account details and subdomain selection.

### Step 2: Select and Claim Subdomain

**Context**: Input the vulnerable subdomain during setup to claim it.

Enter 'tictail' as the subdomain for zendesk.com; confirm the green availability mark and complete signup.

> Expected: Account created successfully with subdomain tictail.zendesk.com assigned.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[zendesk]]
- [[account-creation]]
- [[subdomain-claim]]
