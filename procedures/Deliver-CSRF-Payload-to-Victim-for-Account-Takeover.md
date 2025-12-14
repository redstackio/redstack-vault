---
id: p-deliver-csrf-payload-concrete
tags:
  - csrf
  - social-engineering
  - phishing
  - account-takeover
  - concrete-cms
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
updated_at: '2025-12-14T17:33:06.323Z'
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
# Deliver CSRF Payload to Victim for Account Takeover

## Summary

This procedure involves social engineering to lure an authenticated victim into loading the malicious HTML page, triggering the CSRF attack and resulting in full control over their Concrete CMS account.

## Description

By hosting the malicious form on an attacker-controlled site and disguising the link (e.g., as a legitimate resource), the victim is tricked into visiting while logged in. The auto-submitting form forges the profile update, changing credentials to the attacker's, enabling session hijacking or password reset takeover without further interaction.

## Requirements

1. Hosted malicious HTML page accessible via URL
2. Social engineering channels (email, chat, etc.) to deliver the link
3. Victim's authentication to the target site at delivery time

## Defense

Defensive measures and detection strategies:

- User training on suspicious links
- Browser extensions for CSRF protection (e.g., NoScript)
- Server-side logging of cross-origin requests

## Objectives

1. Ensure victim loads page while authenticated
2. Confirm account details are overwritten
3. Gain persistent access to the hijacked account

## Instructions

### Step 1: Host the Malicious Page

**Context**: Make the HTML publicly accessible to deliver via link.

Upload to a free host like GitHub Pages or use ngrok for local serving to get a public URL (e.g., `https://attacker-site.com/csrf.html`).

**Expected Output**: Stable URL pointing to the auto-submitting form.

### Step 2: Craft Delivery Message

**Context**: Use phishing or pretexting to entice the victim.

Send an email or message: "Check this important update: https://attacker-site.com/csrf.html" ensuring it appears legitimate.

**Expected Output**: Victim clicks and loads the page.

### Step 3: Verify Takeover

**Context**: Monitor for successful update and access the new credentials.

After delivery, attempt login with the forged email and reset password if needed.

**Expected Output**: Access to victim's account with elevated privileges.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[Phishing]]
- [[account-takeover]]
