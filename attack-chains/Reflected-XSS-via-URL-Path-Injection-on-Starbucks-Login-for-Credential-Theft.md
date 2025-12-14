---
tags:
  - xss
  - reflected-xss
  - javascript-injection
  - credential-theft
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Chrome]]'
  - '[[tools/Firefox]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Credential Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Prepare-Web-Browser-for-XSS-Testing]]'
  - '[[procedures/Craft-and-Navigate-to-Malicious-XSS-URL]]'
  - '[[procedures/Trigger-XSS-Payload-via-Mouseover]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:06.894Z'
description: >-
  A multi-step attack exploiting a reflected XSS vulnerability in the Starbucks
  login page URL path handling, allowing JavaScript injection via mouseover
  events to steal user credentials.
skill_level: intermediate
impact_level: high
id: 63612c40-5719-43ca-bef3-52a18bd422d4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Reflected XSS via URL Path Injection on Starbucks Login for Credential Theft

Multi-stage attack chain demonstrating exploitation of a reflected XSS vulnerability on the Starbucks login pages (www.starbucks.com and www.starbucks.co.uk), where improper URL path escaping allows attackers to inject malicious JavaScript event handlers, leading to credential theft via form data capture.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare Browser] --> B[Craft and Visit URL] --> C[Trigger Payload]
    C --> D[Credential Theft]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Chrome]]
- [[tools/Firefox]]

### Target Environment

- Web platform
- Access to Starbucks login pages (/account/signin on www.starbucks.com or www.starbucks.co.uk)
- No specific ports or services beyond standard HTTPS (443)

### Initial Access Requirements

- Public internet access
- No credentials needed for initial payload delivery (reflected XSS)
- Victim interaction required (mouseover on button)

## Detailed Attack Procedures

### Step 1: Prepare Web Browser for XSS Testing
procedure: [[procedures/Prepare-Web-Browser-for-XSS-Testing]]

**Objective**: Set up a browser environment to access and interact with the vulnerable Starbucks login page without interference.

**Instructions**: Launch Chrome or Firefox in a clean session to avoid extensions blocking JavaScript. Ensure developer tools are available for payload verification.

**Expected Output**: Browser window open and ready for navigation.

**Success Indicators**:
- Browser launches successfully
- No blocking extensions active

### Step 2: Craft and Navigate to Malicious XSS URL
procedure: [[procedures/Craft-and-Navigate-to-Malicious-XSS-URL]]

**Objective**: Construct a URL that injects a malicious payload into the page's link construction, breaking out of HTML attributes to embed an onmouseover event handler.

**Instructions**: In the browser address bar, enter the crafted URL such as `https://www.starbucks.com/account/(A(%22%20%252fonmouseover=%22alert%25%32%38%64%6f%63%75%6d%65%6e%74.%64%6f%6d%61%69%6e%25%32%39%22))/signin` for a domain alert test, or for password theft: `https://www.starbucks.com/account/(F(%22%20%252fonmouseover=%22%2561%256c%2565%2572%2574%2528%2564%256f%2563%2575%256d%2565%256e%2574%252e%2567%2565%2574%2545%256c%2565%256d%2565%256e%2574%2573%2542%2579%254e%2561%256d%2565%2528%2527%2541%2563%2563%256f%2575%256e%2574%252e%2550%2561%2573%2573%2557%256f%2572%2564%2527%2529%255b%2530%255d%252e%2576%2561%256c%2575%2565%2529%22))/signin`. Press Enter to load the page.

**Expected Output**: The login page loads with the injected payload embedded in a link, visible in the page source as an altered href attribute on elements like the 'Find the Store' button.

**Success Indicators**:
- Page loads without errors
- Inspect element shows payload in link attributes

### Step 3: Trigger XSS Payload via Mouseover
procedure: [[procedures/Trigger-XSS-Payload-via-Mouseover]]

**Objective**: Execute the injected JavaScript by interacting with the vulnerable element, capturing sensitive data like the password field value.

**Instructions**: Locate the 'Find the Store' button in the upper right-hand corner of the page and hover the mouse over it to trigger the onmouseover event.

**Expected Output**: JavaScript execution, such as an alert box displaying the document domain or the captured password value from the form input.

**Success Indicators**:
- Alert or script output appears
- In a real attack, form data (e.g., password) is exfiltrated to attacker-controlled server

## Attack Chain Summary

### Key Achievements

1. Successful injection of JavaScript via URL path manipulation due to ASP.NET URI handling flaws.
2. Execution of arbitrary code in the victim's browser context on the login page.
3. Potential theft of user credentials, enabling account compromise.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Credential Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
