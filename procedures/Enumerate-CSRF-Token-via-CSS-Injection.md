---
tags:
  - csrf-leak
  - side-channel
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
updated_at: '2025-12-14T17:27:57.198Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: c656a8b1-5444-4ae8-b997-4ae9ebd02f5d
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Enumerate-CSRF-Token-via-CSS-Injection

## Summary

This procedure exploits CSS injection to leak a user's CSRF token by injecting rules that change page colors based on token characters, detectable via visual or timing-based side-channel attacks.

## Description

Building on confirmed CSS injection, this targets the CSRF token embedded in the page DOM. Payloads are crafted to select elements containing specific token characters (e.g., via attribute selectors like [data-token^='a']), applying unique colors. An external POC demo simulates the victim's session, allowing observation of color shifts to infer the token sequentially. The scenario involves embedding the vulnerable iframe in a controlled page, with outcomes including full token reconstruction for CSRF bypass. Prerequisites include the injection point and a way to observe the rendered page, such as screenshots or automated timing.

## Requirements

1. Confirmed CSS injection capability from prior step
2. Access to a POC environment or victim session simulation
3. Ability to observe visual changes (e.g., browser or screenshot tool)

## Defense

Defensive measures and detection strategies:

- Obfuscate or randomize CSRF tokens to hinder enumeration
- Apply Content Security Policy (CSP) to restrict inline CSS
- Log and alert on repeated color-changing payloads

## Objectives

1. Detect token characters through color-based side-channels
2. Reconstruct the full CSRF token
3. Enable subsequent CSRF attacks on the application

## Instructions

### Step 1: Reset POC Environment

**Context**: Prepare the demonstration setup to simulate a fresh token.

Access the reset URL:

```url
http://d0nut.pythonanywhere.com/demo/token_stealing/7GTt5qD1LD273WYkJyaR/reset
```

> This clears any prior state. Expected output: Confirmation of reset, ready for injection testing.

### Step 2: Inject and Observe Token Enumeration

**Context**: Load the injection page with CSS payloads targeting token characters, observing sequential color changes.

Access:

```url
http://d0nut.pythonanywhere.com/demo/token_stealing/7GTt5qD1LD273WYkJyaR
```

Craft payloads like `%7D[data-csrf^='a']%7Bbackground:blue%7D` for each possible character (a-z, 0-9), cycling through to match colors.

> Use visual inspection or timing (e.g., via GIF like cssi.gif) to note which payload triggers a change, revealing the character. Repeat for each token position. Expected output: Inferred token string, e.g., 'abc123'.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf-leak]]
- [[side-channel]]
