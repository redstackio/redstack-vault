---
id: proc-chain-self-xss-171398
tags:
  - self-xss
  - csrf
  - xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.385Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Chain-Self-XSS-with-Login-CSRF

## Summary

This procedure chains Login CSRF-forced authentication with stored Self-XSS in victim-only areas of HackerOne to execute arbitrary JavaScript in the victim's session, enabling data theft from confidential reports.

## Description

Self-XSS payloads are stored in internal areas accessible only to the victim but can be triggered under attacker control after forcing a login via CSRF. The sequence: Malicious page triggers CSRF login, accesses victim-only zone to store/activate XSS, logs out, waits for victim re-interaction (e.g., sign-in) to execute the payload. This leads to session hijacking and info leakage. Prerequisites: Prior Self-XSS payload placement. Outcome: Malicious code runs as victim, stealing session data.

## Requirements

1. Pre-placed Self-XSS payload in victim-accessible area
2. Successful Login CSRF execution
3. Victim's subsequent interaction

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs to prevent XSS storage
- Implement Content Security Policy (CSP) to block inline JS
- Audit victim-only areas for anomalous script execution

## Objectives

1. Force login to access restricted areas
2. Trigger Self-XSS execution
3. Exfiltrate session data or perform actions

## Instructions

### Step 1: Force Login via CSRF

**Context**: Use prior procedure to authenticate as victim.

Load malicious page to start SAML flow and gain session.

> Session now active in victim-only zones.

### Step 2: Store and Trigger Self-XSS

**Context**: Access area to activate stored payload.

Navigate to victim-only page where Self-XSS is embedded (e.g., via forced session).

> Payload executes only for victim; chain logs out to await re-login.

### Step 3: Execute on Victim Re-Interaction

**Context**: Wait for victim to sign in again.

Upon victim's next login, XSS triggers, e.g., stealing cookies or accessing reports.

> Expected: Payload sends data to attacker (e.g., via fetch to external endpoint).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Credential Access]] Credential Access

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[self-xss]]
- [[xss]]
