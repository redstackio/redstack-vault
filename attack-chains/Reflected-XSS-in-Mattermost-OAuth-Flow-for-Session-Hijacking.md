---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - xss
  - mattermost
  - oauth
  - session-hijacking
  - reflected-xss
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Craft-and-Visit-Malicious-OAuth-Redirect-URL]]'
  - '[[procedures/Verify-XSS-JavaScript-Execution]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.236Z'
description: >-
  A multi-stage attack exploiting a reflected XSS vulnerability in Mattermost
  Server's OAuth authentication flow to execute arbitrary JavaScript and hijack
  user sessions.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Reflected XSS in Mattermost OAuth Flow for Session Hijacking

Multi-stage attack chain demonstrating a complete attack workflow exploiting unsanitized 'redirect_to' parameter in Mattermost's OAuth flow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Visit Malicious URL] --> B[Trigger XSS Execution]
    B --> C[Hijack Session and Steal Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Mattermost Server with OAuth enabled (e.g., version vulnerable to CVE or similar, pre-patch)
- Web platform
- Services: Mattermost Server, OAuth provider (e.g., custom 'shielder')
- Tech stack: Go-based webapp
- Network access: Publicly accessible Mattermost URL

### Initial Access Requirements

- Ability to trick victim into clicking a malicious link (e.g., via phishing email or social engineering)
- No prior credentials needed; exploits reflected XSS in authentication flow
- Victim must be authenticated or in process of OAuth login

## Detailed Attack Procedures

### Step 1: Craft and Visit Malicious OAuth Redirect URL
procedure: [[procedures/Craft-and-Visit-Malicious-OAuth-Redirect-URL]]

**Objective**: Inject a malicious payload into the 'redirect_to' parameter to close the HTML attribute and insert executable JavaScript during the OAuth mobile login flow.

**Instructions**: Construct the malicious URL by appending a payload to the OAuth endpoint that breaks out of the href attribute and injects an <img> tag with an onerror handler. For example, use the following URL structure:

https://<mattermost_url>/oauth/shielder/mobile_login?redirect_to=%22%3E%3Cimg%20src=%22%22%20onerror=%22alert(%27zi0Black%20@%20Shielder%27)%22%3E

Trick the victim into visiting this URL via a phishing link. The payload decodes to ">%3Cimg src="" onerror="alert('zi0Black @ Shielder')"%3E, which injects the script.

**Expected Output**: The browser loads the OAuth page, but the injected HTML renders, triggering the JavaScript.

**Success Indicators**:
- Page loads with altered HTML (inspect source to see injected <img> tag)
- No immediate errors; payload is reflected without sanitization

### Step 2: Verify XSS JavaScript Execution
procedure: [[procedures/Verify-XSS-JavaScript-Execution]]

**Objective**: Confirm arbitrary JavaScript execution in the victim's browser context, enabling session theft or further exploitation.

**Instructions**: Upon visiting the URL from Step 1, observe the browser's rendering of the unsanitized response. The invalid src on the <img> tag triggers the onerror event, executing the alert. In a real attack, replace the alert with code to exfiltrate session cookies (e.g., document.cookie) to an attacker-controlled server.

**Expected Output**: Alert popup displays 'zi0Black @ Shielder' (or custom payload executes), confirming XSS. For session hijacking, stolen cookies can be used to impersonate the user.

**Success Indicators**:
- JavaScript alert or console log appears
- Session data (chats for users, admin privileges for admins) accessible via hijacked session

## Attack Chain Summary

### Key Achievements

1. Successful injection of arbitrary JavaScript via reflected XSS in OAuth flow
2. Demonstration of session hijacking potential, allowing chat content theft or server configuration changes
3. Exploitation without authentication, relying on social engineering for initial click

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2023-10-01T12:00:00Z*
