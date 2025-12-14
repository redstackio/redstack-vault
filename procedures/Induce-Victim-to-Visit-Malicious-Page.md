---
tags:
  - csrf
  - phishing
  - drive-by
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:29.354Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: cae2ed46-dd7f-49b3-af5d-e27eefff4dff
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Induce-Victim-to-Visit-Malicious-Page

## Summary

This procedure focuses on social engineering the victim to visit the hosted CSRF PoC page while authenticated to the target application, triggering the unauthorized form submission and account modification.

## Description

In the ███████mil CSRF attack, the victim must be logged in for their session cookies to be sent with the forged request. The attacker uses phishing (e.g., email with a disguised link) to lure the victim to the PoC URL. Upon loading, the page's JavaScript submits the forms invisibly, exploiting the lack of token validation. Prerequisites: Hosted PoC and victim targeting info. Expected outcome: Silent execution of the exploit, altering the victim's account without notice.

## Requirements

1. Hosted CSRF PoC page URL
2. Victim's contact method (email, etc.)
3. Timing: Victim must be authenticated to ███████mil

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and suspicious links
- Use multi-factor authentication (MFA) to protect against credential changes
- Log and alert on rapid successive updates to account details

## Objectives

1. Deliver the malicious link to the victim
2. Ensure visit occurs during active session
3. Achieve forged request submission

## Instructions

### Step 1: Craft Phishing Delivery

**Context**: Create a convincing lure to prompt the visit.

Compose an email or message with a link to the PoC, e.g., "Check this urgent update: http://fake-site.com/csrf-poc.html" disguised as legitimate.

### Step 2: Monitor and Confirm Trigger

**Context**: Verify the exploit fires upon visit.

Send the phishing attempt. Monitor target application logs if accessible, or check for account changes post-visit.

**Expected Output**: Victim's browser submits the request; changes appear in their account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[drive-by-compromise]]
- [[social-engineering]]
