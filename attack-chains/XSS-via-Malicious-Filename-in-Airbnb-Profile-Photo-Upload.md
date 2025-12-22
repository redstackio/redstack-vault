---
tags:
  - xss
  - web
  - filename-injection
  - airbnb
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Craft-Malicious-XSS-Filename]]'
  - '[[procedures/Upload-XSS-Payload-to-Profile-Photo]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:53.057Z'
description: >-
  A cross-site scripting attack exploiting insufficient sanitization of uploaded
  filenames in the Airbnb.es profile photo feature, leading to arbitrary
  JavaScript execution and session hijacking.
skill_level: beginner
impact_level: high
id: 7611b199-f66b-4a9d-b2b1-b6bd91867fad
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# XSS via Malicious Filename in Airbnb Profile Photo Upload

Multi-stage attack chain demonstrating a complete XSS exploitation workflow on airbnb.es.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Craft Malicious Filename] --> B[Upload to Profile Photo]
    B --> C[XSS Execution and Cookie Theft]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome with developer tools)
- Text editor for crafting filenames

### Target Environment

- Web platform: airbnb.es
- Required services/ports: HTTPS on port 443
- Network access requirements: Internet access to airbnb.es

### Initial Access Requirements

- User account on Airbnb.es (authenticated session)
- No special privileges needed beyond profile editing access

## Detailed Attack Procedures

### Step 1: Craft Malicious Filename
procedure: [[procedures/Craft-Malicious-XSS-Filename]]

**Objective**: Create a filename that injects an XSS payload to execute JavaScript when processed or displayed.

**Instructions**: Use a text editor to name a harmless file (e.g., a .txt file) with a payload like "><img src='x' onerror=alert(document.cookie)>.txt. This payload closes any open HTML attributes and injects an <img> tag that triggers an onerror event to alert the user's cookies.

**Expected Output**: A file ready for upload with the malicious name.

**Success Indicators**:
- Filename contains valid XSS payload without syntax errors
- Payload tested in a local HTML file to confirm execution

### Step 2: Upload to Profile Photo
procedure: [[procedures/Upload-XSS-Payload-to-Profile-Photo]]

**Objective**: Upload the malicious file to trigger XSS execution during profile photo processing or display.

**Instructions**: Log in to airbnb.es, navigate to the profile photo upload feature, and select the crafted file. The unsanitized filename will be reflected in the HTML, executing the payload when the profile is viewed or processed.

**Expected Output**: Alert box displaying document.cookie upon execution, confirming XSS success.

**Success Indicators**:
- JavaScript alert fires with cookie data
- Potential session hijacking if payload is modified to exfiltrate data

## Attack Chain Summary

### Key Achievements

1. Successful injection of XSS payload via filename
2. Execution of arbitrary JavaScript in the victim's browser
3. Ability to steal cookies and hijack user sessions

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
