---
id: ac-ipv6-libcurl-ssrf-001
tags:
  - ssrf
  - ipv6
  - libcurl
  - access-bypass
  - url-parsing
type: attack_chain
tools:
  - '[[tools/libcurl]]'
  - '[[tools/trurl]]'
  - '[[tools/gcc]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-libcurl-Test-Application]]'
  - '[[procedures/Submit-Malformed-IPv6-URL]]'
  - '[[procedures/Demonstrate-libcurl-Parsing-Stripping]]'
  - '[[procedures/Execute-Bypassing-Request]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:55.544Z'
description: >-
  Multi-stage attack exploiting inconsistent IPv6 URL parsing in libcurl,
  leading to SSRF by routing requests to unintended network interfaces and
  bypassing access controls.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SSRF and Access Control Bypass via IPv6 Zone Identifier Stripping in libcurl

Multi-stage attack chain demonstrating exploitation of libcurl's inconsistent handling of IPv6 addresses with zone identifiers, as per HackerOne report #2814750. This allows attackers to supply malformed URLs that cause requests to ignore specified network interfaces, enabling SSRF to internal resources and bypassing firewall or interface-based controls.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Application] --> B[Submit Malformed URL]
    B --> C[Parse and Strip Zone ID]
    C --> D[Execute Bypassing Request]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/libcurl]]
- [[tools/trurl]]
- [[tools/gcc]]

### Target Environment

- Linux (e.g., Ubuntu 20.04)
- Application using libcurl for URL fetching and validation
- Network interfaces with IPv6 link-local addresses (e.g., eth0)

### Initial Access Requirements

- Access to a web application endpoint that accepts and fetches user-supplied URLs via libcurl
- Ability to submit HTTP requests with custom URLs
- Internal network with restricted services accessible only via specific interfaces

## Detailed Attack Procedures

### Step 1: Setup Test Application
procedure: [[procedures/Setup-libcurl-Test-Application]]

**Objective**: Prepare a vulnerable application environment using libcurl to handle user-supplied URLs, assuming correct IPv6 parsing per RFC 6874.

**Instructions**: Compile and run a custom C program that uses libcurl to parse and fetch URLs, simulating a web app backend.

First, identify the environment using [[commands/identify-ubuntu-version]]:

```bash
lsb_release -a
```

Then compile the test code with [[commands/compile-libcurl-test]]:

```bash
gcc parserbatch.c -o parserbatch -lcurl
```

**Expected Output**: Successful compilation with no errors; executable 'parserbatch' created.

**Success Indicators**:
- Ubuntu 20.04 or similar Linux distro confirmed
- Test program compiles linking libcurl v7.68.0

### Step 2: Submit Malformed IPv6 URL
procedure: [[procedures/Submit-Malformed-IPv6-URL]]

**Objective**: Provide an attacker-controlled URL with an IPv6 link-local address and percent-encoded zone identifier to trigger parsing issues.

**Instructions**: In the application interface (e.g., web form), submit a URL like http://[fe80::1%25eth0]/ where %25 encodes the % for the zone ID 'eth0', intending routing via the eth0 interface.

No specific command needed; simulate via application input or curl submission if API exposed.

**Expected Output**: URL accepted by the application for processing.

**Success Indicators**:
- URL submitted without immediate rejection
- Application proceeds to fetch/parse the URL using libcurl

### Step 3: Demonstrate libcurl Parsing Stripping
procedure: [[procedures/Demonstrate-libcurl-Parsing-Stripping]]

**Objective**: Show how libcurl strips the zone identifier from the IPv6 hostname, deviating from RFC 6874.

**Instructions**: Run the test program to parse the URL and observe the hostname extraction. Use [[commands/run-libcurl-parsing-test]] on a file containing the test URL:

```bash
./parserbatch
```

Alternatively, use [[commands/extract-url-components-with-trurl]] for direct demonstration:

```bash
trurl --get 'Host: {host} Zone: {zoneid}' 'http://[fe80::1%25eth0]/'
```

**Expected Output**: Host: [fe80::1] Zone: eth0 (zone preserved separately, but hostname lacks it, leading to default interface use).

**Success Indicators**:
- Zone ID stripped from hostname in parsed output
- Comparison with other libraries (e.g., Python urllib) shows correct inclusion

### Step 4: Execute Bypassing Request
procedure: [[procedures/Execute-Bypassing-Request]]

**Objective**: Perform the fetch, routing the request to the default interface instead of the specified one, enabling SSRF or bypass.

**Instructions**: Trigger the libcurl fetch in the application context; the parsed hostname [fe80::1] connects via unintended interface, accessing internal services restricted to eth0.

Monitor network traffic to confirm routing anomaly.

**Expected Output**: Successful connection to fe80::1 on default interface, potentially reaching internal resources.

**Success Indicators**:
- Request bypasses interface-specific firewall rules
- Access to sensitive internal services or SSRF to metadata endpoints

## Attack Chain Summary

### Key Achievements

1. Demonstrated libcurl's unique stripping of IPv6 zone IDs, inconsistent with RFC 6874 and other parsers.
2. Enabled SSRF by routing to unintended interfaces, accessing internal networks.
3. Bypassed access controls tied to specific network interfaces.
4. Potential for information leakage from restricted services.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
