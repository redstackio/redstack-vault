---
tags:
  - xss
  - stored-xss
  - payload-injection
  - wordpress
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - WordPress
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e0f6f013-ca7b-4a0c-b294-76b936c1750a
created_at: '2025-12-13T23:55:20.651Z'
updated_at: '2025-12-13T23:55:20.651Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-User-Bio

## Summary

This procedure exploits a parsing flaw in WordPress's wp_targeted_link_rel function by injecting a crafted <a> tag into the user bio, allowing attribute injection for stored XSS execution on profile views.

## Description

The wp_targeted_link_rel filter uses regex to parse <a> tags but fails to respect attribute positioning, enabling attackers to place the rel attribute inside another attribute's value (e.g., title). This injects delimiters and adds malicious attributes like onmouseover without proper quoting. The payload is stored in the database and rendered on BuddyPress profile pages, affecting all viewers.

## Requirements

1. Logged-in unprivileged user account
2. Access to profile editing (Users > Profile or front-end edit)
3. Knowledge of the vulnerable parsing in wp_targeted_link_rel

## Defense

Defensive measures and detection strategies:

- Update WordPress core and plugins to patched versions
- Implement content security policy (CSP) to block inline scripts
- Sanitize user inputs with strict HTML parsing libraries
- Monitor for anomalous JavaScript in user fields

## Objectives

1. Bypass link filtering to inject executable attributes
2. Store the payload persistently in the user bio
3. Enable execution on subsequent profile loads

## Instructions

### Step 1: Log In and Access Profile Edit

**Context**: Prepare to modify the vulnerable bio field.

Log in with the unprivileged account and navigate to profile editing.

> Go to `/wp-admin/profile.php` or BuddyPress front-end edit page.

### Step 2: Craft and Insert Payload

**Context**: Use a payload that exploits attribute position to inject onmouseover.

Paste the following into the description/bio field:

`<a href="#" title=" target='abc' rel= onmouseover=alert(/XSS/) ">This is a PoC for a Stored XSS</a>`

> The rel attribute is placed after title's value but before its close, tricking the regex into adding unquoted attributes.

### Step 3: Save and Verify Storage

**Context**: Confirm the payload is saved without immediate execution.

Click Update Profile and view the bio to ensure the link appears (but does not trigger yet).

> Check source code to confirm the injected attributes are present post-filtering.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[attribute-injection]]
