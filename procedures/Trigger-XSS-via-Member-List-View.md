---
id: proc-concretecms-trigger-xss-memberlist
tags:
  - xss-trigger
  - member-list
  - cookie-theft
  - concrete-cms
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.647Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Member-List-View

## Summary

This procedure triggers the reflected XSS by accessing the member list in Concrete CMS, where the injected City field value renders unsanitized, executing the JavaScript payload in the attacker's or victim's browser to steal cookies.

## Description

The member list view in Concrete CMS displays user profile data, including the City field, without output encoding. When viewed, the payload executes client-side, allowing arbitrary JS like alerting document.cookie. This can lead to session theft if viewed by admins or other users.

## Requirements

1. Injected payload from prior procedure stored in a profile
2. Access to the member list page (public or authenticated view)
3. Victim browser context for execution (e.g., another user viewing the list)

## Defense

Defensive measures and detection strategies:

- Apply output encoding (e.g., HTML escaping) when rendering user data in views
- Content Security Policy (CSP) to block inline JS execution
- Monitor for JS errors or alerts in browser consoles on member list pages

## Objectives

1. Reflect the stored payload in the member list
2. Execute JS to demonstrate impact (e.g., cookie alert)
3. Enable further attacks like data exfiltration

## Instructions

### Step 1: Navigate to Member List

**Context**: Access the page that displays profile data unsanitized.

From the dashboard, go to the 'Members' or 'Member List' section.

**Expected Output**: List of users loads, including the targeted profile's City field.

### Step 2: Observe Payload Execution

**Context**: Trigger the reflection and JS run.

View the entry for the injected profile; the payload should render and execute the <img> onerror, alerting cookies.

**Expected Output**: Browser alert box showing document.cookie contents.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[member-list]]
- [[cookie-theft]]
- [[concrete-cms]]
