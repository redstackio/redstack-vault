---
tags:
  - ssrf
  - nextcloud
  - ip-bypass
  - aws-metadata
  - localhost
type: attack_chain
tools:
  - '[[tools/PHP]]'
  - '[[tools/cURL]]'
  - '[[tools/Symfony-IpUtils]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - PHP
  - AWS
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Review-Nextcloud-Source-Code-for-Validation-Flaws]]'
  - '[[procedures/Set-Up-Local-PHP-Test-Environment]]'
  - '[[procedures/Test-Standard-SSRF-Payloads]]'
  - '[[procedures/Test-Enclosed-Alphanumeric-IP-Payload]]'
  - '[[procedures/Test-Octal-IP-Notation-Bypass]]'
  - '[[procedures/Verify-Impact-with-Localhost-Access]]'
step_count: 6
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:53:38.304Z'
description: >-
  A multi-stage attack chain exploiting SSRF in Nextcloud's IP validation
  functions to bypass local IP restrictions and access internal endpoints like
  localhost and AWS metadata services.
skill_level: intermediate
impact_level: high
id: b7842648-f477-4b64-9bdb-82dd1f13d133
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Nextcloud SSRF Bypass Using Enclosed Alphanumeric and Octal IP Notations to Access Internal Resources

Multi-stage attack chain demonstrating exploitation of SSRF in Nextcloud's `ThrowIfLocalIp` and `ThrowIfLocalAddress` functions by bypassing IP validation with non-standard notations, leading to access of internal resources such as localhost services and AWS instance metadata.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Review Source Code] --> B[Set Up Test Environment]
    B --> C[Test Standard Payloads]
    C --> D[Test Alphanumeric Bypass]
    D --> E[Test Octal Bypass]
    E --> F[Verify Internal Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/PHP]]
- [[tools/cURL]]
- [[tools/Symfony-IpUtils]]

### Target Environment

- Nextcloud server running on PHP with Symfony components
- Local PHP test environment mimicking Nextcloud validation logic
- Access to internal services like localhost (port 80/443) or AWS metadata endpoint (169.254.169.254)

### Initial Access Requirements

- Source code access to Nextcloud (e.g., via prior report or public repo)
- Local development setup with PHP and Composer for Symfony
- Network access to target Nextcloud instance for payload testing

## Detailed Attack Procedures

### Step 1: Review Source Code
procedure: [[procedures/Review-Nextcloud-Source-Code-for-Validation-Flaws]]

**Objective**: Identify flaws in IP validation logic to inform payload development.

**Instructions**: Analyze Nextcloud source code from report #1608039, focusing on `ThrowIfLocalIp` using `filter_var` with `FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE` and `IpUtils::checkIp` for local ranges like 100.64.0.0/10 and 192.0.0.0/24.

**Expected Output**: Understanding of validation weaknesses, such as lack of normalization for octal or encoded IPs.

**Success Indicators**:
- Flaws in `filter_var` and `IpUtils` identified
- Potential bypass vectors noted (e.g., non-ASCII characters, octal notation)

### Step 2: Set Up Test Environment
procedure: [[procedures/Set-Up-Local-PHP-Test-Environment]]

**Objective**: Replicate Nextcloud's validation to safely test SSRF payloads.

**Instructions**: Create a PHP script requiring Symfony autoload, implement `ThrowIfLocalIp` and `ThrowIfLocalAddress`, accept ?ip= or ?host= parameters, validate, and use cURL to fetch if passed.

**Expected Output**: Local server echoing 'Pass' for valid IPs or content from fetched endpoints.

**Success Indicators**:
- Script runs without errors
- Validation functions throw exceptions on standard private IPs

### Step 3: Test Standard Payloads
procedure: [[procedures/Test-Standard-SSRF-Payloads]]

**Objective**: Confirm baseline blocking of known SSRF targets.

**Instructions**: Test payloads like http://100.100.100.200 (Alibaba metadata) and http://169.254.169.254 (AWS metadata) using the test script's ?ip= parameter.

**Expected Output**: Exceptions thrown due to private/reserved range detection.

**Success Indicators**:
- Standard private IPs blocked
- Validation logs show filter_var and IpUtils triggering

### Step 4: Test Enclosed Alphanumeric Payload
procedure: [[procedures/Test-Enclosed-Alphanumeric-IP-Payload]]

**Objective**: Bypass IP filters using encoded characters.

**Instructions**: Use payload `⑯⑨。②⑤④。⑯⑨｡②⑤④` (resolves to 169.254.169.254) in ?ip=; check if `filter_var` treats it as public IP.

**Expected Output**: 'Pass' echoed, but `ThrowIfLocalAddress` may catch via hostname check (substr_count($host, '.') === 0).

**Success Indicators**:
- Payload bypasses `ThrowIfLocalIp`
- Potential for AWS metadata access confirmed

### Step 5: Test Octal IP Notation Bypass
procedure: [[procedures/Test-Octal-IP-Notation-Bypass]]

**Objective**: Exploit parsing failures with octal notation for localhost and metadata access.

**Instructions**: Test `http://0177.0.0.1/` (octal 127.0.0.1) and `0251.0376.0251.0376` (octal 169.254.169.254) using ?host= in the script with embedded cURL.

**Expected Output**: cURL fetches internal content without exceptions; logs show requests to internal IPs.

**Success Indicators**:
- Octal payloads evade parse_url and filter_var
- Localhost or metadata response returned

### Step 6: Verify Impact with Localhost Access
procedure: [[procedures/Verify-Impact-with-Localhost-Access]]

**Objective**: Confirm SSRF enables information disclosure from internal services.

**Instructions**: Use successful octal payload to access a dummy localhost page; monitor server logs for internal requests.

**Expected Output**: Internal page content echoed; logs confirm SSRF execution.

**Success Indicators**:
- Sensitive internal data accessed
- Potential for further exploitation (e.g., RCE via internal services)

## Attack Chain Summary

### Key Achievements

1. Identified validation flaws in Nextcloud's IP functions
2. Bypassed filters using alphanumeric encoding and octal notation
3. Accessed localhost and AWS metadata, enabling information disclosure

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---

*Last updated: 2023-10-01T00:00:00Z*
