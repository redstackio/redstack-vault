---
id: ac-uber-open-redirect-119236
tags:
  - open-redirect
  - phishing
  - url-manipulation
  - ip-obfuscation
  - uber
type: attack_chain
tools:
  - '[[tools/IP-Address-Converter]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Test-Double-Slash-Redirection]]'
  - '[[procedures/Exploit-IP-Based-Redirect]]'
  - '[[procedures/Obfuscate-IP-for-Phishing]]'
  - '[[procedures/Verify-Redirect-on-Multiple-Domains]]'
step_count: 4
techniques:
  - '[[Phishing]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:26.929Z'
description: >-
  Multi-stage attack exploiting open redirection on Uber.com using double
  slashes and IP obfuscation to craft phishing links.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
  - '[[Exploit Public-Facing Application]]'
---
# Open Redirection on Uber.com via Double Slash and IP Obfuscation

Multi-stage attack chain demonstrating how to exploit an open redirection vulnerability on Uber.com by manipulating URL paths with double slashes (//), testing with domains and IPs, and obfuscating IPs in decimal form to create convincing phishing links that redirect users to malicious sites.

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
    A[Initial Testing with Domains] --> B[Switch to IP Addresses]
    B --> C[Omit Protocol for Redirection]
    C --> D[Obfuscate IP and Verify]
    D --> E[Phishing Link Creation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#2ecc71
```

## Prerequisites & Requirements

### Required Tools

- [[tools/IP-Address-Converter]]

### Target Environment

- Web platform (Uber.com)
- No specific ports or services required beyond HTTP/HTTPS access
- Public internet access to test URLs

### Initial Access Requirements

- No credentials needed
- Direct network access to uber.com
- Browser or curl for testing redirections

## Detailed Attack Procedures

### Step 1: Test Double Slash with Domain
procedure: [[procedures/Test-Double-Slash-Redirection]]

**Objective**: Verify if double slashes in the URL path trigger a 404 or potential redirection when using a domain after the slashes.

**Instructions**: Access a malformed URL like https://www.uber.com//google.com/cities using a browser or curl to check for redirection behavior.

Use [[commands/curl-test-domain-redirect]] to simulate:

```bash
curl -L -I "https://www.uber.com//google.com/cities"
```

**Expected Output**: HTTP 404 Page Not Found response from Uber.

**Success Indicators**:
- 404 error confirms improper handling but no immediate redirect
- No redirection to external site

### Step 2: Attempt Redirection with IP and Protocol
procedure: [[procedures/Exploit-IP-Based-Redirect]]

**Objective**: Test redirection using an IP address after double slashes, including protocol, to identify SSL or 404 issues.

**Instructions**: Try URLs with IP addresses like https://www.uber.com//216.58.217.206/calendar and observe errors.

Execute [[commands/curl-test-ip-with-protocol]]:

```bash
curl -L -I "https://www.uber.com//216.58.217.206/calendar"
```

**Expected Output**: 404 or SSL certificate error due to protocol mismatch.

**Success Indicators**:
- Errors indicate protocol interference
- Confirms IP parsing but blocked by HTTPS

### Step 3: Enable Redirection by Omitting Protocol
procedure: [[procedures/Exploit-IP-Based-Redirect]]

**Objective**: Remove the protocol from the IP part to bypass errors and achieve successful redirection.

**Instructions**: Use http://uber.com//216.58.217.206/calendar to force HTTP redirection.

Run [[commands/curl-omit-protocol-redirect]]:

```bash
curl -L -I "http://uber.com//216.58.217.206/calendar"
```

**Expected Output**: 301/302 redirect to the target IP's site (e.g., Google Calendar) without errors.

**Success Indicators**:
- Successful redirect to external site
- No 404 or SSL issues

### Step 4: Obfuscate and Verify Phishing Links
procedure: [[procedures/Obfuscate-IP-for-Phishing]]
procedure: [[procedures/Verify-Redirect-on-Multiple-Domains]]

**Objective**: Convert IP to decimal for obfuscation and test on multiple domains to confirm exploit reliability for phishing.

**Instructions**: Convert IP 216.58.217.206 to decimal 3627735502 using the tool, then test http://uber.com//3627735502/calendar. Verify with other sites like hackerone.com.

Use [[commands/curl-obfuscated-ip-redirect]]:

```bash
curl -L -I "http://uber.com//3627735502/calendar"
```

**Expected Output**: Redirect to obfuscated target without detection.

**Success Indicators**:
- Redirect works with obfuscated IP
- Consistent behavior across domains like Facebook and Yahoo

## Attack Chain Summary

### Key Achievements

1. Identified open redirection via double slash mishandling
2. Bypassed errors by omitting protocol and using IPs
3. Obfuscated redirects with decimal IPs for phishing evasion
4. Verified exploit on multiple external domains

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Phishing]] Phishing
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
