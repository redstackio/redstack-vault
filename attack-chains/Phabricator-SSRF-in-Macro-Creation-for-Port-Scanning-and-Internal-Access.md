---
id: ac-phabricator-ssrf-macro
tags:
  - ssrf
  - port-scanning
  - information-disclosure
  - phabricator
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Phabricator-Macro-Creation-Page]]'
  - '[[procedures/Test-SSRF-with-Localhost-Ports]]'
  - '[[procedures/Differentiate-with-External-Host-Behaviors]]'
  - '[[procedures/Exploit-Redirects-and-DNS-Rebinding]]'
  - '[[procedures/Analyze-Responses-for-Information-Disclosure]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T04:39:02.197Z'
description: >-
  A multi-stage attack exploiting SSRF in Phabricator's macro creation to scan
  internal ports, access localhost services, and disclose information via error
  messages and redirects.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Vulnerability Scanning]]'
---
# Phabricator SSRF in Macro Creation for Port Scanning and Internal Access

Multi-stage attack chain demonstrating exploitation of SSRF in Phabricator's macro creation feature to perform internal reconnaissance, port scanning, and potential access to restricted services.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Macro Page] --> B[Test Local Ports]
    B --> C[External Differentiation]
    C --> D[Exploit Redirects]
    D --> E[Analyze Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser for form submission

### Target Environment

- Phabricator instance accessible via web
- Macro creation feature enabled
- Internal services on localhost or private IPs

### Initial Access Requirements

- Valid user session in Phabricator (authenticated access to /macro/create/)
- Network position allowing HTTP requests to the Phabricator server

## Detailed Attack Procedures

### Step 1: Access Macro Creation Page
procedure: [[procedures/Access-Phabricator-Macro-Creation-Page]]

**Objective**: Gain access to the vulnerable URL input field for SSRF exploitation.

**Instructions**: Navigate to the Phabricator macro creation endpoint at `/macro/create/` using a web browser. Locate the URL field designed for fetching images or resources.

**Expected Output**: Form page with URL input field visible.

**Success Indicators**:
- Macro creation form loads successfully
- URL field is present and submittable

### Step 2: Test SSRF with Localhost Ports
procedure: [[procedures/Test-SSRF-with-Localhost-Ports]]

**Objective**: Trigger SSRF to scan open ports on localhost and observe error differences.

**Instructions**: In the URL field, enter test URLs like `http://localhost:22/` or `http://localhost:21/`. Submit the form to initiate server-side fetch via cURL.

**Expected Output**: cURL error messages indicating port status (e.g., connection errors for closed ports).

**Success Indicators**:
- Distinct error codes for open vs. closed ports
- Confirmation of server-side request execution

### Step 3: Differentiate with External Host Behaviors
procedure: [[procedures/Differentiate-with-External-Host-Behaviors]]

**Objective**: Confirm SSRF by comparing localhost responses to external ones.

**Instructions**: Submit URLs like `http://google.com:22/` and observe timeout or connection behaviors, contrasting with localhost results.

**Expected Output**: Different error patterns (e.g., timeouts for external closed ports vs. immediate errors for local).

**Success Indicators**:
- Behavioral differences validate SSRF
- No external access issues but internal fetch succeeds

### Step 4: Exploit Redirects and DNS Rebinding
procedure: [[procedures/Exploit-Redirects-and-DNS-Rebinding]]

**Objective**: Bypass restrictions to access internal resources via redirects or rebinding.

**Instructions**: Use URLs such as `http://davenport.net.nz/test.php` (redirects to localhost), `http://testing.allthethings.co.nz/` (DNS to localhost), or `http://127.0.0.1/` in the form.

**Expected Output**: Fetched internal HTTP responses or error pages from restricted services.

**Success Indicators**:
- Internal content or errors returned
- Bypass of direct localhost blocks

### Step 5: Analyze Responses for Information Disclosure
procedure: [[procedures/Analyze-Responses-for-Information-Disclosure]]

**Objective**: Extract sensitive information from errors or fetched content.

**Instructions**: Review response errors (e.g., CURLE_RECV_ERROR for open ports) or HTTP responses (e.g., 500 errors with server details). Save non-HTML files for viewing.

**Expected Output**: Details on open ports, internal services, or server configurations.

**Success Indicators**:
- Identification of running services (e.g., SSH on port 22)
- Disclosure of internal application content

## Attack Chain Summary

### Key Achievements

1. Successful port scanning of localhost services
2. Bypass of firewall restrictions to internal networks
3. Information disclosure via unsanitized cURL errors and responses
4. Potential for further exploitation of internal endpoints

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Vulnerability Scanning]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Reconnaissance]]

---
*Last updated: 2023-10-01T00:00:00Z*
