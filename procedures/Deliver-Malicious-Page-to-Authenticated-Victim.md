---
tags:
  - csrf
  - phishing
  - social-engineering
  - web
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
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:27:16.039Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b8568a09-cb7d-45e4-b6d8-312c40e87606
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Deliver-Malicious-Page-to-Authenticated-Victim

## Summary

This procedure covers tricking an authenticated user into loading the malicious CSRF HTML page, triggering the personal key regeneration on staging.login.gov without their knowledge.

## Description

Delivery relies on social engineering, such as phishing emails or malicious links, to lure the victim to the attacker's hosted page while they remain logged into the target site. Upon loading, the page auto-submits the form, forcing a new personal key generation and invalidating the old one. The victim is redirected to the management page showing the new key, but the change occurs silently.

## Requirements

1. Hosted malicious HTML page accessible via URL
2. Method to contact victim (e.g., email, chat)
3. Victim must have an active session on staging.login.gov

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication for key changes
- Train users to verify links before clicking
- Use email filters to block suspicious phishing attempts

## Objectives

1. Ensure victim loads the page in an authenticated state
2. Trigger the CSRF submission seamlessly
3. Observe the redirect and key display as confirmation

## Instructions

### Step 1: Host the Malicious Page

**Context**: Make the HTML accessible over the web to enable link delivery.

Upload the crafted HTML to a web server (e.g., GitHub Pages, ngrok for local testing) and obtain the public URL, such as http://attacker-site.com/csrf.html.

**Expected Output**: Page loads and auto-submits when visited.

### Step 2: Craft and Send Phishing Delivery

**Context**: Disguise the link to entice the victim to click while logged in.

Create a phishing email: "Urgent: Update your personal key at [malicious URL disguised as login.gov link]." Send to victim.

When victim clicks and loads the page:

**Expected Output**: Automatic POST to target endpoint, followed by redirect to https://staging.login.gov/manage/personal_key?resend=true showing new key.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.002]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[csrf-delivery]]
- [[social-engineering]]
