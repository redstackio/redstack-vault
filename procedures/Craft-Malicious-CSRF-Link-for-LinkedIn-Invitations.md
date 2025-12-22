---
id: proc-uuid-1
tags:
  - csrf
  - link-crafting
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:50.457Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-CSRF-Link-for-LinkedIn-Invitations

## Summary

This procedure involves constructing a malicious URL that exploits a CSRF vulnerability in LinkedIn's connection invitation endpoint, allowing an attacker to forge requests that force authenticated victims to send invitations without confirmation.

## Description

The attack targets the `/comm/mynetwork/send-invite/<USERNAME>/` endpoint, which lacks proper CSRF tokens or origin validation. By mimicking parameters from legitimate 'People You May Know' emails (e.g., lipi, midSig, midToken, trkEmail, trk, _sig), the attacker crafts a link using the victim's profile as the sender and the attacker's as the recipient. When clicked by an authenticated victim, the browser executes the POST-like action cross-origin, expanding the attacker's network illicitly. Prerequisites include knowledge of the victim's public profile URL name and the attacker's own username.

## Requirements

1. Access to LinkedIn's invitation URL structure (e.g., via email inspection)
2. Victim's public profile username (e.g., linkedin.com/in/victim-name)
3. Attacker's LinkedIn username for the target

## Defense

Defensive measures and detection strategies:

- Implement anti-CSRF tokens (e.g., Synchronizer Token Pattern) on invitation endpoints
- Enforce same-origin policy and validate referer headers
- Require user confirmation for all connection actions
- Monitor for anomalous invitation spikes from single sources

## Objectives

1. Forge a functional CSRF link targeting the invitation feature
2. Bypass single-user restrictions for targeted spam
3. Enable unwanted connection requests without victim awareness

## Instructions

### Step 1: Analyze Legitimate Invitation Structure

**Context**: Inspect a real LinkedIn 'People You May Know' email or URL to extract base format and parameters.

No specific command; manually note the endpoint `/comm/mynetwork/send-invite/<TARGET>/` and parameters like `?lipi=abc123&midSig=xyz&midToken=def&trkEmail=info&trk=people-guest_people_you_may_know&trkInfo=...&_sig=hash`.

> Expected: Understanding of parameter roles for forgery.

### Step 2: Construct Malicious Link

**Context**: Replace the target username with the attacker's and adjust parameters to point to the victim as sender.

Manually build the URL: `https://www.linkedin.com/comm/mynetwork/send-invite/attacker-username?lipi=...&midSig=...` (copy values from legit example, ensuring it mimics email tracking).

> Expected: A URL that, when opened in a victim's authenticated browser, triggers the invitation.

### Step 3: Test Link (Optional, in Controlled Environment)

**Context**: Verify the link structure without targeting real users.

Paste the URL into a browser logged into a test account; observe if it attempts the invitation action silently.

> Expected: No errors; invitation queued if targeting self or test.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web-exploitation]]
