---
tags:
  - xss
  - self-xss
  - phabricator
  - web
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Phabricator-Time-of-Day-XSS]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:35.649Z'
description: >-
  A self-XSS vulnerability in Phabricator's user preferences allowing JavaScript
  injection through the Time-of-Day Format field, triggered when viewing
  repository overviews.
skill_level: low
impact_level: low
id: ecc745c7-4790-4371-868e-230470506027
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Phabricator Self-XSS via Time-of-Day Format Preference

Multi-stage attack chain demonstrating a complete self-XSS workflow in Phabricator.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~1 minute |
| Skill Level | Low |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access User Preferences] --> B[Inject Obfuscated Payload]
    B --> C[Trigger in Repository View]
    C --> D[XSS Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual browser actions)

### Target Environment

- Phabricator web application
- Authenticated user session
- Access to Diffusion (repository) feature

### Initial Access Requirements

- Valid Phabricator account credentials
- Browser with JavaScript enabled
- No special network access beyond standard web login

## Detailed Attack Procedures

### Step 1: Access User Preferences
procedure: [[procedures/Exploit-Phabricator-Time-of-Day-XSS]]

**Objective**: Navigate to the user settings to prepare for payload injection.

**Instructions**: Log in to the Phabricator instance and access the user preferences menu.

**Expected Output**: User preferences page loaded, including the Time-of-Day Format field.

**Success Indicators**:
- Preferences interface visible
- Time-of-Day Format field accessible for input

### Step 2: Inject Obfuscated Payload
procedure: [[procedures/Exploit-Phabricator-Time-of-Day-XSS]]

**Objective**: Insert a JavaScript payload into the Time-of-Day Format field without triggering immediate validation errors.

**Instructions**: Enter the obfuscated payload `'<\/i\m\g \s\r\c=x \o\n\e\r\r\o\r=\a\l\e\r\t(\'X\S\S\')\>'` (which decodes to `<img src=x onerror=alert('XSS')>`) into the Time-of-Day Format field, ensuring the surrounding single quotes are included. Save the preferences.

**Expected Output**: Preferences saved without errors; no immediate alert triggered.

**Success Indicators**:
- Payload accepted and saved
- No sanitization errors on save

### Step 3: Trigger XSS in Repository View
procedure: [[procedures/Exploit-Phabricator-Time-of-Day-XSS]]

**Objective**: Render the malicious preference in a context that executes the injected JavaScript.

**Instructions**: Navigate to a repository file-overview in the Diffusion feature, where the Time-of-Day Format value is rendered in the web interface.

**Expected Output**: JavaScript alert popup displaying 'XSS' upon page load.

**Success Indicators**:
- Alert popup executes
- Confirms arbitrary JavaScript execution in the browser session

## Attack Chain Summary

### Key Achievements

1. Successful injection of obfuscated XSS payload into user preferences
2. Triggering of self-XSS without affecting other users
3. Demonstration of insufficient output sanitization in Phabricator's rendering

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
