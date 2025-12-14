---
tags:
  - ssrf
  - xss
  - cors-proxy
  - flyte
  - uberinternal
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Flyte-Console-Instance]]'
  - '[[procedures/Audit-Flyte-Open-Source-Code]]'
  - '[[procedures/Exploit-SSRF-via-CORS-Proxy]]'
  - '[[procedures/Demonstrate-Reflected-XSS-via-Proxy]]'
step_count: 4
techniques:
  - '[[Active Scanning]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:53:38.210Z'
description: >-
  Multi-stage attack exploiting an unauthenticated CORS proxy in Flyte Console
  to perform server-side request forgery and enable reflected XSS attacks on
  internal Uber resources.
skill_level: intermediate
impact_level: high
id: fa54c9d5-9f4a-4966-9923-4951f5c22880
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Active Scanning]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
---
# Full Read SSRF via Unauthenticated CORS Proxy in Flyte Console Leading to Reflected XSS

Multi-stage attack chain demonstrating discovery, auditing, exploitation of SSRF in Flyte Console's CORS proxy, and chaining to reflected XSS for potential internal resource access and client-side attacks.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discovery of Flyte Instance] --> B[Code Audit for Vulnerabilities]
    B --> C[SSRF Exploitation via Proxy]
    C --> D[Reflected XSS Demonstration]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools for manual testing
- Access to public Flyte documentation and GitHub repository

### Target Environment

- Web platform with Flyte Console deployed (e.g., on internal domains like uberinternal.com)
- No authentication required for the vulnerable CORS proxy route
- Network access to the Flyte instance URL

### Initial Access Requirements

- Public internet access to audit open-source code
- No prior credentials needed due to unauthenticated endpoint
- Knowledge of the target domain (e.g., flyte-poc-us-east4.uberinternal.com)

## Detailed Attack Procedures

### Step 1: Discover Flyte Console Instance
procedure: [[procedures/Discover-Flyte-Console-Instance]]

**Objective**: Identify the presence of a Flyte Console instance on the target domain to establish the attack surface.

**Instructions**: Manually inspect the target domain (e.g., uberinternal.com) for deployed Flyte instances. Use browser navigation or search for known Flyte endpoints like /console. Verify the instance is accessible without authentication.

**Expected Output**: Confirmation of Flyte Console running, such as the login or dashboard page loading.

**Success Indicators**:
- Flyte Console interface visible at the target URL
- No authentication prompt for initial access

### Step 2: Audit Open-Source Code
procedure: [[procedures/Audit-Flyte-Open-Source-Code]]

**Objective**: Review the Flyte codebase to identify potential vulnerabilities in unauthenticated routes.

**Instructions**: Clone the Flyte GitHub repository and search for CORS proxy implementations. Look for routes handling proxy requests without auth checks, such as those proxying external resources for browser CORS bypass.

**Expected Output**: Identification of an unauthenticated /proxy route or similar that forwards requests server-side.

**Success Indicators**:
- Code reveals lack of validation on proxy endpoints
- Route allows arbitrary URL proxying

### Step 3: Exploit SSRF via CORS Proxy
procedure: [[procedures/Exploit-SSRF-via-CORS-Proxy]]

**Objective**: Leverage the unauthenticated proxy to forge server-side requests to internal resources and read responses.

**Instructions**: Craft requests to the CORS proxy endpoint, specifying internal URLs (e.g., metadata services) as the target. Use tools like curl or browser to send the proxy request and capture the full response body.

**Expected Output**: Server forwards the request internally and returns sensitive data, such as internal API responses.

**Success Indicators**:
- Full response from internal resource received
- Ability to read arbitrary server-side content

### Step 4: Demonstrate Reflected XSS
procedure: [[procedures/Demonstrate-Reflected-XSS-via-Proxy]]

**Objective**: Chain SSRF to inject and reflect malicious HTML/JS via the proxy for client-side execution.

**Instructions**: Proxy a malicious HTML payload through the CORS proxy, embedding JavaScript for XSS. Deliver via a phishing link or direct request to trigger reflection in the user's browser.

**Expected Output**: Malicious script executes in the victim's browser context, potentially stealing session data.

**Success Indicators**:
- Alert or payload execution in browser console
- CORS policy bypassed due to proxy origin

## Attack Chain Summary

### Key Achievements

1. Discovered vulnerable Flyte deployment on internal Uber domain
2. Audited code to uncover unauthenticated CORS proxy flaw
3. Exploited SSRF for full read access to internal resources
4. Chained to reflected XSS for potential account compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Active Scanning]] Active Scanning
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Drive-by Compromise]] Drive-by Compromise

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access
- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
