---
tags:
  - ssrf
  - dns-bypass
  - line-social-plugins
  - internal-access
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-ssrf-bypass-test]]'
platforms:
  - Web
complexity: medium
procedures:
  - >-
    [[procedures/Bypass-DNS-Verification-for-SSRF-in-LINE-Shared-Content-Parameter]]
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  A single-stage attack exploiting an SSRF vulnerability in the LINE Social
  Plugins service by bypassing DNS verification on a shared content parameter to
  access internal web services' HTML content via HTTP requests.
skill_level: intermediate
impact_level: high
id: 011818d0-7062-4a93-ab9f-5b5e9840d0cc
created_at: '2025-12-14T04:08:48.521Z'
updated_at: '2025-12-14T04:08:48.521Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SSRF in LINE Social Plugins via DNS Bypass to Access Internal HTML Pages

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via SSRF Bypass] --> B[Access Internal Resources]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[commands/curl-ssrf-bypass-test]]

### Target Environment

- Target Platform: Web
- Required Services: LINE Social Plugins (social-plugins.line.me)
- Network Access Requirements: Public internet access to the LINE Social Plugins endpoint

### Initial Access Requirements

- No credentials required
- External network position (no internal access needed initially)
- Prior access: None, as it exploits a public-facing application

## Detailed Attack Procedures

### Step 1: Bypass DNS Verification for SSRF
procedure: [[procedures/Bypass-DNS-Verification-for-SSRF-in-LINE-Shared-Content-Parameter]]

**Objective**: Exploit the inadequate DNS verification in the shared content page information parameter to perform SSRF and access internal HTTP endpoints serving HTML pages.

**Instructions**: Identify the vulnerable parameter in the LINE Social Plugins service, typically a URL parameter used for verifying shared content. Manipulate it to point to internal resources by bypassing DNS checks, such as using a controlled domain that resolves to internal IPs or directly crafting HTTP requests to internal hosts.

Use [[commands/curl-ssrf-bypass-test]] to send a request with a bypassed parameter targeting an internal service:

```bash
curl -X GET "https://social-plugins.line.me/api/shared-content?url=http://internal-host.internal/" -H "User-Agent: Mozilla/5.0"
```

Analyze the response for internal HTML content leakage.

**Expected Output**: Server response containing HTML from internal web services, indicating successful SSRF.

**Success Indicators**:
- Response includes internal page elements (e.g., server headers, HTML structure not from public sources)
- No DNS resolution errors; request reaches internal endpoint

## Attack Chain Summary

### Key Achievements

1. Bypassed DNS verification to enable SSRF over HTTP protocol
2. Accessed internal web services' HTML content from the vulnerable server
3. Demonstrated limited impact to internal HTML pages without broader exploitation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01*
