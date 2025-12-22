---
tags:
  - xss
  - cookie-theft
  - session-hijacking
type: procedure
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
  - '[[Credentials In Files]]'
updated_at: '2025-12-13T23:08:55.613Z'
skill_level: intermediate
impact_level: high
sub_techniques: []
id: 085b3639-a124-4630-925b-4cdcbfeabed9
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Credentials In Files]]'
---
# Observe-JavaScript-Execution-and-Cookie-Theft

## Summary

This procedure monitors the impact of the XSS, where the JavaScript accesses and exfiltrates the victim's session cookie, enabling hijacking and channel compromise.

## Description

The payload JS sets innerHTML to display the cookie, but in advanced variants, it could exfil to attacker server. Targets IRCCloud session tokens; requires successful embed load. Outcome: Attacker gains victim's auth, allowing message sending as victim and potential mass actions in channels.

## Requirements

1. Successful JS execution from prior steps
2. Access to observe or receive exfiltrated data
3. Victim's active session

## Defense

Defensive measures and detection strategies:

- Use HttpOnly and Secure flags on session cookies to prevent JS access
- Monitor for anomalous session usage or cookie modifications in logs

## Objectives

1. Steal session cookie via JS
2. Hijack victim session
3. Enable further compromise

## Instructions

### Step 1: Confirm JS Impact

**Context**: Watch for payload effects in the victim's client.

The JS runs: top.document.body.innerHTML = "hi your cookie is " + document.cookie; // Observe body change or console.

> Cookie value now visible; copy for replay.

### Step 2: Replay Cookie for Hijacking

**Context**: Use stolen token to impersonate.

In a new browser, set the cookie and access IRCCloud to take over the session.

> Test by sending a message as victim.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Credentials In Files]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[session-hijacking]]
