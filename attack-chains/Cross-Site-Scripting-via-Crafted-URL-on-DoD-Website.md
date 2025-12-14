---
tags:
  - xss
  - web-vulnerability
  - dod
  - script-injection
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Craft-and-Deliver-XSS-Payload-via-URL]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.166Z'
description: >-
  Demonstration of an XSS vulnerability on a U.S. Department of Defense website
  by crafting a malicious URL to inject and execute scripts in a victim's
  browser, potentially exposing session data or altering content.
skill_level: intermediate
impact_level: high
id: acf5a52b-938f-47f6-b41e-cc4fffdb906a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Cross-Site Scripting via Crafted URL on DoD Website

Multi-stage attack chain demonstrating a complete attack workflow.

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
    A[Craft Malicious URL] --> B[Inject and Execute Script]
    B --> C[Exfiltrate Session Data or Modify Content]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- None (manual crafting)

### Target Environment

- Web platform
- Public-facing DoD website with insufficient input sanitization
- No specific ports or services required beyond standard HTTP/HTTPS

### Initial Access Requirements

- Ability to craft and share URLs (e.g., via phishing or social engineering)
- Victim interaction: User must click the crafted URL while authenticated on the site
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Craft and Deliver Malicious URL
procedure: [[procedures/Craft-and-Deliver-XSS-Payload-via-URL]]

**Objective**: Create a specially formatted URL that injects a malicious script into the victim's browser upon access, exploiting the XSS vulnerability to execute JavaScript.

**Instructions**: Identify a vulnerable parameter or endpoint on the DoD website (e.g., a search or redirect field). Craft a URL embedding a script payload, such as `<script>alert('XSS')</script>`, URL-encoded if necessary. For demonstration, use a payload that alerts or exfiltrates session data. Share the URL with the victim via email or link to trick them into clicking it while on the site.

Example crafted URL (generic, as exact not specified): `https://dod-site.example.com/search?q=<script>alert(document.cookie)</script>`

**Expected Output**: Upon clicking, the script executes in the victim's browser, displaying an alert with session cookies or sending data to an attacker-controlled server.

**Success Indicators**:
- Script execution confirmed (e.g., alert pops up)
- Session data (cookies) revealed or exfiltrated
- Page content modified if payload alters DOM
