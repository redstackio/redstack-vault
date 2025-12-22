---
tags:
  - phishing
  - delivery
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:33.369Z'
sub_techniques: []
id: 4151b0d9-fee3-45b3-92e2-17df4bb57f94
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Deliver-Malicious-Link-to-Victim

## Summary

This procedure copies the vulnerable advanced search URL containing the reflected payload and distributes it to a victim for remote exploitation.

## Description

The crafted URL, when opened by a victim, replicates the DOM-based XSS in their browser context, allowing arbitrary JS execution. This enables attacks like session theft via cookie access or keylogging, without direct interaction from the attacker.

## Requirements

1. Generated advanced search URL with payload
2. Communication channel (email, messaging)
3. Victim with browser access to the site

## Defense

Defensive measures and detection strategies:

- Educate users on suspicious links
- Implement URL scanning for malicious payloads in emails/chats

## Objectives

1. Propagate the exploit link
2. Achieve remote code execution on victim
3. Enable follow-on attacks like data exfiltration

## Instructions

### Step 1: Copy the URL

**Context**: Extract the full malicious URL for sharing.

Right-click the advanced search page and select 'Copy Link Address' or use browser address bar.

> Expected: URL includes query param with `<script>prompt(1337)</script>` unescaped.

### Step 2: Share with Victim

**Context**: Send the link via a social engineering vector.

Paste the URL into an email or message, e.g., 'Check this search result: [URL]'.

> Expected: Victim clicks and opens, triggering prompt in their session.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- link-delivery
- victim-exploitation
