---
tags:
  - xss
  - saml
  - authentication
  - web
  - reflected-xss
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Initiate-SAML-Authentication-Flow]]'
  - '[[procedures/Intercept-SAML-Request-with-Burp-Suite]]'
  - '[[procedures/Inject-XSS-Payload-into-SAMLResponse]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:20.062Z'
description: >-
  A multi-step attack exploiting a reflected XSS vulnerability in a SAML
  authentication endpoint to execute arbitrary JavaScript in the victim's
  browser, enabling session hijacking and further compromise.
skill_level: intermediate
impact_level: high
id: f816159d-f55a-4dc1-ae10-df9f3359f618
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Reflected XSS in SAML Authentication Endpoint for Arbitrary JavaScript Execution

Multi-stage attack chain demonstrating exploitation of a reflected Cross-Site Scripting (XSS) vulnerability in a SAML authentication endpoint of a U.S. Department of Defense web application. The attack allows injection of malicious JavaScript via the SAMLResponse parameter, leading to arbitrary code execution in the victim's browser. This can result in cookie theft for session hijacking, forging requests on behalf of the user, downloading malware disguised as legitimate content, and defacing the website.

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
    A[Initiate Authentication] --> B[Intercept Request]
    B --> C[Inject Payload]
    C --> D[Execute JavaScript]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web application with SAML authentication
- Publicly accessible logon page
- No specific ports required beyond standard HTTPS (443)

### Initial Access Requirements

- Network access to the target web application
- No prior credentials needed for discovery phase
- Browser or proxy tool for request interception

## Detailed Attack Procedures

### Step 1: Initiate Authentication Flow
procedure: [[procedures/Initiate-SAML-Authentication-Flow]]

**Objective**: Access the logon page to start the SAML authentication process and trigger the vulnerable endpoint.

**Instructions**: Open a web browser and navigate to the logon page URL, such as `https://███/+CSCOE+/logon.html`, appending the parameters `a0=15&a1=&a2=&a3=1`. This initiates the authentication flow and generates the SAML request that will be intercepted in the next step.

**Expected Output**: The logon page loads, and a POST request to the SAML endpoint is prepared in the browser.

**Success Indicators**:
- Logon page accessible without errors
- SAML authentication flow begins

### Step 2: Intercept SAML Request
procedure: [[procedures/Intercept-SAML-Request-with-Burp-Suite]]

**Objective**: Capture the outgoing SAML authentication request using a proxy tool to prepare for modification.

**Instructions**: Configure your browser to route traffic through Burp Suite as a proxy. With Burp Suite running, submit the logon form or proceed with authentication. Intercept the POST request to `/+CSCOE+/saml/sp/acs?tgname=a` in Burp's Proxy tab, then forward it to the Repeater module for editing.

**Expected Output**: The request is captured and displayed in Burp Repeater, showing the SAMLResponse parameter in the body.

**Success Indicators**:
- Request intercepted successfully
- SAMLResponse parameter visible in the request body

### Step 3: Inject XSS Payload
procedure: [[procedures/Inject-XSS-Payload-into-SAMLResponse]]

**Objective**: Modify the SAMLResponse parameter to include a malicious JavaScript payload, triggering reflected XSS execution upon resubmission.

**Instructions**: In Burp Repeater, edit the request body to replace or append to the SAMLResponse value with `"><svg/onload=alert('0xElkot')>`. Ensure the Content-Type is `application/x-www-form-urlencoded` and update Content-Length to 46. Resend the modified request to the server.

**Expected Output**: The server reflects the payload, executing the JavaScript in the browser, such as displaying an alert box with '0xElkot'.

**Success Indicators**:
- Alert box or JavaScript execution observed
- No server-side errors; payload reflected in response

## Attack Chain Summary

### Key Achievements

1. Successful initiation of SAML flow without authentication
2. Interception and modification of sensitive authentication request
3. Arbitrary JavaScript execution via reflected XSS, enabling further attacks like session theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Initial Access]]

---

*Last updated: 2023-10-01T00:00:00Z*
