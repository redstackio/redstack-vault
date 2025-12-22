---
tags:
  - http-request-smuggling
  - cloudflare
  - transform-rules
  - header-injection
  - te.cl
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
  - Cloud (Cloudflare)
complexity: medium
procedures:
  - >-
    [[procedures/Inject-Newline-into-Headers-Using-Hex-Escapes-in-Concat-Function]]
  - '[[procedures/Smuggle-Internal-Request-via-Chunked-Transfer-Encoding]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploits a vulnerability in Cloudflare's Transform Rules by injecting newlines
  via hex escapes in concat() to enable TE.CL request smuggling and access
  internal resources.
skill_level: intermediate
impact_level: high
id: bde3402c-f6d1-44a2-b3fc-a11c6c2fe5e2
created_at: '2025-12-14T17:28:36.461Z'
updated_at: '2025-12-14T17:28:36.461Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# HTTP Request Smuggling via Hexadecimal Escape Sequences in Cloudflare Transform Rules

Multi-stage attack chain demonstrating a complete attack workflow exploiting Cloudflare's Edge Rules engine.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Malicious Transform Rule] --> B[Send Smuggled POST Request]
    B --> C[Access Internal Origin Server]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses Cloudflare dashboard and HTTP client like curl)

### Target Environment

- Cloudflare-enabled web application
- Access to Cloudflare dashboard for rule creation
- Internal origin servers protected by Cloudflare Access

### Initial Access Requirements

- Administrative access to Cloudflare account or ability to create custom rules
- Network access to send requests to the Cloudflare-proxied endpoint
- No prior credentials needed for the exploit itself

## Detailed Attack Procedures

### Step 1: Create Malicious Transform Rule
procedure: [[procedures/Inject-Newline-into-Headers-Using-Hex-Escapes-in-Concat-Function]]

**Objective**: Inject a newline and Transfer-Encoding header into an HTTP response to enable chunked encoding manipulation.

**Instructions**: Log into the Cloudflare dashboard, navigate to Rules > Transform Rules, and create a dynamic rewrite rule for headers using the concat() function with hex escapes.

**Expected Output**: Rule successfully created and activated, injecting '\r\nTransfer-Encoding: chunked' into the target header.

**Success Indicators**:
- Rule saves without errors in dashboard
- Test request shows manipulated header in response (e.g., via browser dev tools or curl -v)

### Step 2: Send Smuggled POST Request
procedure: [[procedures/Smuggle-Internal-Request-via-Chunked-Transfer-Encoding]]

**Objective**: Leverage the injected header to smuggle a GET request to an internal host within a chunked POST body, bypassing Cloudflare Access.

**Instructions**: Craft and send a POST request with a chunked body containing the smuggled GET request to the target endpoint.

**Expected Output**: Response containing content from the internal origin server, indicating successful smuggling.

**Success Indicators**:
- Internal resource content (e.g., / HTTP/1.1 response from internal.example.com) appears in the outer response
- No access denial from Cloudflare Access

## Attack Chain Summary

### Key Achievements

1. Bypassed Cloudflare's security controls including Access policies
2. Achieved HTTP request smuggling (TE.CL variant) to access internal servers
3. Demonstrated header injection via unsanitized hex escapes in rule engine

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2024-10-01*
