---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567895
tags:
  - clickjacking
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
updated_at: '2025-12-14T17:32:58.322Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Induce-Victim-to-Visit-Malicious-Post

## Summary

Direct the victim to the malicious post URL, triggering the hidden iframe and JavaScript execution in their session.

## Description

The post loads normally, but the invisible iframe exploits the logged-in session to submit profile changes, bypassing CSRF with a fresh nonce.

## Requirements

1. Published post URL
2. Active victim session

## Defense

Defensive measures and detection strategies:

- Educate users on phishing links
- Block suspicious iframes

## Objectives

1. Victim page load
2. Payload execution

## Instructions

### Step 1: Share URL

**Context**: Lure victim.

Provide post URL via email or chat.

### Step 2: Visit Post

**Context**: Trigger attack.

Victim pastes and enters URL in browser.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[drive-by]]
