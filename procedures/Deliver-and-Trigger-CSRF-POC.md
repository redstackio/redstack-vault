---
id: proc-deliver-csrf-poc
tags:
  - csrf
  - delivery
  - phishing
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
updated_at: '2025-12-14T17:27:03.106Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Deliver and Trigger CSRF POC

## Summary

This procedure involves hosting or distributing the malicious CSRF HTML form to a victim, triggering the unauthorized password change when they load it while authenticated to the target site.

## Description

Delivery can occur via phishing emails, malicious links on external sites, or embedded in ads. The victim must be logged into the target (e.g., Coinbase) for the session cookie to authorize the forged request. Modify the POC form with desired new password values. In the reported case, hosting the HTML allowed submission to the password_reset endpoint. Monitor for success via follow-up access attempts.

## Requirements

1. Hosted location for HTML (e.g., attacker server, GitHub page)
2. Method to lure victim (email, social engineering)
3. Victim authenticated to target site

## Defense

Defensive measures and detection strategies:

- SameSite cookie attributes to block cross-site requests
- User training on suspicious links
- WAF rules to detect anomalous form submissions

## Objectives

1. Lure victim to malicious page
2. Auto-submit forged request
3. Achieve password change and account control

## Instructions

### Step 1: Host the POC

**Context**: Make the HTML accessible via URL.

Upload csrf_poc.html to a web server or free host, obtain URL like http://attacker.com/csrf.html.

> Expected output: Publicly accessible page.

### Step 2: Deliver to Victim

**Context**: Trick victim into visiting while logged in.

Send link via email: "Click here to update your info: http://attacker.com/csrf.html". Or embed in a forum post.

> Page loads and submits form silently. Expected output: POST request sent to target.

### Step 3: Verify Impact

**Context**: Check if password changed.

Attempt login with new password or monitor account activity.

> Success if access granted without old password knowledge.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[drive-by-compromise]]
