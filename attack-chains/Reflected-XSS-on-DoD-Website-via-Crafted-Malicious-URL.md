---
tags:
  - xss
  - reflected-xss
  - dod
  - web-vulnerability
  - javascript-injection
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
created_at: '2024-09-01T00:00:00Z'
procedures:
  - '[[procedures/Craft-Malicious-URL-for-Reflected-XSS]]'
step_count: 1
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:37.412Z'
description: >-
  A single-stage attack demonstrating a reflected XSS vulnerability on a U.S.
  Department of Defense website by crafting a URL that injects and executes
  malicious JavaScript in the victim's browser.
skill_level: beginner
impact_level: high
id: a0a32c47-a481-477d-940f-1fa58cdf1697
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Reflected XSS on DoD Website via Crafted Malicious URL

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[User Interaction via Crafted URL] --> B[Script Execution in Browser]
    B --> C[Session Theft or Content Modification]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Target OS/Platform: Web
- Required services/ports: HTTP/HTTPS (ports 80/443)
- Network access requirements: Internet access to the DoD website

### Initial Access Requirements

- Credential requirements: None (public-facing website)
- Network position: External attacker
- Prior access needed: None

## Detailed Attack Procedures

### Step 1: Craft and Deliver Malicious URL
procedure: [[procedures/Craft-Malicious-URL-for-Reflected-XSS]]

**Objective**: Inject malicious JavaScript into the website's response via a reflected parameter to execute arbitrary code in the victim's browser, potentially stealing session cookies or modifying page content.

**Instructions**: Identify a vulnerable input parameter on the DoD website (e.g., a search field). Craft a URL with a payload like `<script>alert('XSS')</script>` encoded if necessary. Deliver the URL to the victim via phishing or social engineering. Upon clicking, the script executes in their browser context.

For testing, open the crafted URL in your browser:

```bash
# Example using curl to fetch and inspect response (replace with actual vulnerable URL)
curl "https://example-dod-site.gov/search?q=<script>alert('XSS')</script>"
```

Then, verify execution by observing the alert popup or inspecting the page source for reflected payload.

**Expected Output**: The malicious script is reflected in the HTML response and executes, e.g., an alert box appears or console logs session data.

**Success Indicators**:
- Payload reflected in page source without sanitization
- JavaScript executes (e.g., alert triggers)
- Potential access to document.cookie or DOM manipulation

## Attack Chain Summary

### Key Achievements

1. Successful injection of JavaScript via URL parameter
2. Execution of arbitrary code in victim browser
3. Potential exfiltration of sensitive session information

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2024-09-01T00:00:00Z*
