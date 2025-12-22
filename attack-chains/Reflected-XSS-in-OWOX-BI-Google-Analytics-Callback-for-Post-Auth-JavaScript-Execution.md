---
tags:
  - xss
  - reflected-xss
  - javascript-execution
  - oauth-callback
  - google-analytics
type: attack_chain
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
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
  - '[[procedures/Access-OWOX-BI-Data-Source-Setup]]'
  - '[[procedures/Craft-Malicious-XSS-Callback-URL]]'
  - '[[procedures/Deliver-URL-and-Trigger-XSS-Execution]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:30.471Z'
description: >-
  A phishing-style attack exploiting a reflected XSS vulnerability in the OWOX
  BI Google Analytics OAuth callback to execute arbitrary JavaScript in the
  victim's authenticated browser session.
skill_level: intermediate
impact_level: high
id: 3ac9eeb4-239c-4a22-b9b2-ded022b037fa
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Reflected XSS in OWOX BI Google Analytics Callback for Post-Auth JavaScript Execution

Multi-stage attack chain demonstrating a reflected XSS vulnerability in the OWOX BI application's Google Analytics integration, allowing arbitrary JavaScript execution in an authenticated user's browser context. The attack leverages an unsanitized URL path in the OAuth callback to inject and reflect HTML/JavaScript payloads, enabling session hijacking, data theft, or further exploitation after the victim logs in.

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
    A[Access Setup Page] --> B[Craft Malicious URL]
    B --> C[Deliver to Victim and Execute]
    A:::initial
    B:::execution
    C:::impact

    classDef initial fill:#e74c3c
    classDef execution fill:#f39c12
    classDef impact fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Firefox]]
- [[tools/Chrome]]

### Target Environment

- Web platform
- OWOX BI application at https://bi.owox.com
- Google Analytics OAuth integration
- Access to Gmail credentials for setup simulation

### Initial Access Requirements

- No prior credentials needed for attacker; victim must have OWOX BI account
- Ability to share URLs via phishing (e.g., email, messaging)
- Network access to the internet

## Detailed Attack Procedures

### Step 1: Access Vulnerable Setup Page
procedure: [[procedures/Access-OWOX-BI-Data-Source-Setup]]

**Objective**: Initiate the Google Analytics data source connection process to reach the vulnerable OAuth callback endpoint.

**Instructions**: Open a browser and navigate to the OWOX BI connected services setup page. Select Google Analytics as the data source and enter valid Gmail credentials to proceed to the authorization redirect.

**Expected Output**: An error or redirect link is generated, exposing the callback URL structure at https://bi.owox.com/ui/callbacks/google-supervisors/.

**Success Indicators**:
- Setup page loads successfully
- Gmail OAuth prompt appears and is completed
- Callback URL path is visible for modification

### Step 2: Craft Malicious URL with XSS Payload
procedure: [[procedures/Craft-Malicious-XSS-Callback-URL]]

**Objective**: Inject a URL-encoded XSS payload into the callback URL path to enable reflected execution upon access.

**Instructions**: Modify the callback URL by appending the encoded payload '%3Cimg%20src=xss%20onerror=prompt(1)%3E' (decoding to <img src=xss onerror=prompt(1)>) after 'analytics' in the path, resulting in a URL like https://bi.owox.com/ui/callbacks/google-supervisors/analytics%3Cimg%20src=xss%20onerror=prompt(1)%3E/?state=...&code=.... Test the URL in a browser to confirm reflection without execution.

**Expected Output**: The modified URL renders the page with the injected payload visible in the HTML source, but no execution until accessed post-login.

**Success Indicators**:
- Payload appears unescaped in the page source
- No immediate errors or sanitization occurs
- URL is shareable without breaking

### Step 3: Deliver Malicious URL to Victim and Trigger Execution
procedure: [[procedures/Deliver-URL-and-Trigger-XSS-Execution]]

**Objective**: Trick the victim into accessing the malicious URL, leading to login and subsequent JavaScript execution in their authenticated session.

**Instructions**: Send the crafted URL to the target victim via phishing (e.g., email claiming an integration issue). Upon access, the victim will be prompted to log in to OWOX BI; post-login, the reflected payload executes, such as displaying a prompt dialog.

**Expected Output**: JavaScript alert or prompt (e.g., prompt(1)) appears in the victim's browser after login, confirming execution.

**Success Indicators**:
- Victim accesses and logs in via the URL
- Payload executes, allowing further actions like cookie theft
- Attacker observes effects if payload is modified for exfiltration

## Attack Chain Summary

### Key Achievements

1. Successful injection and reflection of XSS payload in OAuth callback
2. Post-authentication JavaScript execution in victim browser
3. Potential for session theft or data exfiltration affecting all OWOX BI users

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---

*Last updated: 2023-10-01T00:00:00Z*
