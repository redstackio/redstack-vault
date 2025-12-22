---
tags:
  - curl
  - globbing
  - lfi
  - ssrf
  - port-scanning
  - bypass
type: attack_chain
tools:
  - '[[tools/curl]]'
  - '[[tools/wget]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Verify-Curl-Version-and-Globbing-Support]]'
  - '[[procedures/Exploit-Curl-Globbing-for-File-Protocol-Bypass]]'
  - '[[procedures/Compare-Curl-Behavior-with-Wget]]'
  - '[[procedures/Demonstrate-Port-Scanning-via-Curl-Globbing]]'
step_count: 4
techniques:
  - '[[File and Directory Discovery]]'
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T17:26:06.328Z'
description: >-
  Multi-stage attack chain exploiting curl's URL globbing feature to bypass
  protocol blacklists, enabling local file inclusion (LFI), server-side request
  forgery (SSRF), remote file access, and port scanning on Linux systems.
skill_level: intermediate
impact_level: high
id: a3fba514-2424-46be-8e36-bd1c72f8e03c
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
  - '[[Network Service Scanning]]'
---
# Bypass Protocol Filters via Curl URL Globbing for Local File Inclusion and Port Scanning

Multi-stage attack chain demonstrating exploitation of curl's built-in URL globbing feature to expand bracketed patterns in URLs, bypassing protocol filters and enabling unauthorized access to local files or internal services via LFI, SSRF, or port scanning.

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
    A[Verify Curl Environment] --> B[Bypass File Protocol Filter]
    B --> C[Compare with Alternative Tool]
    C --> D[Scan Ports via Globbing]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- [[tools/wget]]

### Target Environment

- Linux platform with curl 7.83.1 or similar (x86_64-pc-linux-gnu)
- Local access to curl binary
- Supported protocols including file:// and http://
- No network restrictions for port scanning examples

### Initial Access Requirements

- Local shell access on the target system
- No credentials needed for local execution
- Prior knowledge of curl's globbing feature

## Detailed Attack Procedures

### Step 1: Verify Curl Environment

procedure: [[procedures/Verify-Curl-Version-and-Globbing-Support]]

**Objective**: Confirm the curl version and features to ensure globbing and file protocol support are available for exploitation.

**Instructions**: Execute the version check using [[commands/curl-version-check]] to verify the environment:

```bash
./curl -Version
```

**Expected Output**: Version details including supported protocols like file and features like globbing.

**Success Indicators**:
- Curl version 7.83.1 or compatible displayed
- File protocol listed in supported protocols

### Step 2: Bypass File Protocol Filter

procedure: [[procedures/Exploit-Curl-Globbing-for-File-Protocol-Bypass]]

**Objective**: Use URL globbing to generate a file:// request, bypassing blacklists and reading sensitive local files like /etc/passwd.

**Instructions**: Run the globbed URL with verbose output using [[commands/curl-glob-file-bypass]]:

```bash
./curl -vv 'f[h-j]le:///etc/passwd'
```

**Expected Output**: Expansion to multiple protocols, with file:// succeeding to output /etc/passwd contents.

**Success Indicators**:
- Sensitive file contents (e.g., user entries) displayed
- Errors for invalid protocols but success for file://

### Step 3: Compare Tool Behavior

procedure: [[procedures/Compare-Curl-Behavior-with-Wget]]

**Objective**: Demonstrate that the globbing bypass is curl-specific by testing the same URL with wget, which fails to expand it.

**Instructions**: Attempt the same globbed URL using [[commands/wget-glob-fail]]:

```bash
wget 'f[h-j]le:///etc/passwd'
```

**Expected Output**: Error indicating invalid protocol, no file access.

**Success Indicators**:
- Wget fails without expansion or access
- Confirms curl's unique vulnerability to this technique

### Step 4: Perform Port Scanning

procedure: [[procedures/Demonstrate-Port-Scanning-via-Curl-Globbing]]

**Objective**: Exploit port globbing to scan a range of ports, identifying open services for further SSRF or reconnaissance.

**Instructions**: Execute the port range glob using [[commands/curl-port-scan-glob]] with verbose output:

```bash
curl -vv 'http://1.1.1.1:[80-9000]/'
```

**Expected Output**: Multiple connection attempts, successes for open ports, timeouts for closed ones.

**Success Indicators**:
- Open ports identified via successful responses
- Evidence of scanning across the port range

## Attack Chain Summary

### Key Achievements

1. Verified curl environment supports necessary features
2. Bypassed protocol filters to read local sensitive files
3. Highlighted tool-specific behavior for targeted exploitation
4. Enabled port scanning to discover internal services

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]] File and Directory Discovery
- [[Network Service Scanning]] Network Service Scanning

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery

---

*Last updated: 2023-10-01T00:00:00Z*
