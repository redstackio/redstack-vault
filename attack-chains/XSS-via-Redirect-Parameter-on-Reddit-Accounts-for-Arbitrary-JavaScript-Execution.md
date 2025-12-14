---
tags:
  - xss
  - web
  - reddit
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/craft-xss-payload-url]]'
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Craft-Malicious-Redirect-URL]]'
  - '[[procedures/Exploit-XSS-on-Reddit-Accounts]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
description: >-
  Exploitation of a cross-site scripting vulnerability in the dest parameter of
  accounts.reddit.com to execute arbitrary JavaScript
skill_level: beginner
impact_level: high
id: 767c7213-e165-4e8e-b05f-f2e5816237bf
created_at: '2025-12-14T00:11:25.246Z'
updated_at: '2025-12-14T00:11:25.246Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# XSS via Redirect Parameter on Reddit Accounts for Arbitrary JavaScript Execution

Multi-stage attack chain demonstrating the exploitation of a cross-site scripting vulnerability in the dest parameter on accounts.reddit.com, allowing arbitrary JavaScript execution via a javascript: URI. This can lead to cookie theft, session hijacking, or other client-side attacks.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access] --> B[Execution]
    style A fill:#e74c3c
    style B fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- None

### Target Environment

- Web browser
- Access to accounts.reddit.com
- No specific ports or services required

### Initial Access Requirements

- Ability to craft and share URLs
- Victim must interact with the URL

## Detailed Attack Procedures

### Step 1: Craft Malicious URL
procedure: [[procedures/Craft-Malicious-Redirect-URL]]

**Objective**: Create a URL with a malicious dest parameter containing a javascript: payload.

**Instructions**: Construct the URL by setting the dest parameter to a javascript: URI, such as using [[commands/craft-xss-payload-url]]:

```bash
# Example URL construction (manual or via script)
echo 'https://accounts.reddit.com/?dest=javascript:alert(document.domain)' > malicious_url.txt
```

**Expected Output**: A crafted URL ready for delivery.

**Success Indicators**:
- URL is correctly formed with javascript: payload
- No syntax errors in the URI

### Step 2: Exploit XSS on Login
procedure: [[procedures/Exploit-XSS-on-Reddit-Accounts]]

**Objective**: Trick the victim into accessing the URL, leading to JavaScript execution upon login or immediately if logged in.

**Instructions**: Deliver the crafted URL to the victim. When accessed, if not logged in, the victim is prompted to log in, after which the XSS executes. If already logged in, it executes immediately.

**Expected Output**: Arbitrary JavaScript executes in the victim's browser under accounts.reddit.com domain.

**Success Indicators**:
- JavaScript payload triggers (e.g., alert pops up)
- Potential for cookie theft or other actions

## Attack Chain Summary

### Key Achievements

1. Successful crafting of malicious redirect URL
2. Execution of arbitrary JavaScript in victim's browser
3. Potential for session hijacking or data exfiltration

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

*Last updated: 2023-10-01*
