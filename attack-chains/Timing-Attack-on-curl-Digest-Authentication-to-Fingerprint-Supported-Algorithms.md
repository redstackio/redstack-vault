---
tags:
  - timing-attack
  - curl
  - digest-authentication
  - reconnaissance
type: attack_chain
tools:
  - '[[tools/Python]]'
  - '[[tools/requests-module]]'
  - '[[tools/poc-timing-attack-py]]'
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
complexity: medium
created_at: '2024-12-14T00:00:00Z'
procedures:
  - '[[procedures/Set-Up-Test-Server-for-Digest-Auth]]'
  - '[[procedures/Execute-Timing-Attack-PoC]]'
  - '[[procedures/Analyze-Response-Timings]]'
  - '[[procedures/Identify-Supported-Algorithm]]'
step_count: 4
techniques:
  - '[[Vulnerability Scanning]]'
  - '[[Hardware]]'
updated_at: '2025-12-14T17:31:30.980Z'
description: >-
  A multi-step attack chain exploiting a timing vulnerability in curl's Digest
  Authentication to fingerprint supported algorithms via response time analysis.
skill_level: intermediate
impact_level: low
id: eb409cc8-cd03-46e8-b3c9-c94d64eb7a47
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
  - '[[Hardware]]'
---
# Timing Attack on curl Digest Authentication to Fingerprint Supported Algorithms

Multi-stage attack chain demonstrating exploitation of a timing vulnerability in curl's Digest Authentication implementation to fingerprint supported algorithms through response time discrepancies.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Set Up Test Server] --> B[Run Timing Attack PoC]
    B --> C[Observe Timing Differences]
    C --> D[Identify Supported Algorithm]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Python]]
- [[tools/requests-module]]
- [[tools/poc-timing-attack-py]]

### Target Environment

- Linux platform
- HTTP service on port 8080
- curl client with vulnerable Digest Authentication (pre-8.5.0 versions)

### Initial Access Requirements

- Local network access to run test server
- Python 3 environment with requests module
- No prior credentials needed; focuses on protocol reconnaissance

## Detailed Attack Procedures

### Step 1: Set Up Test Server
procedure: [[procedures/Set-Up-Test-Server-for-Digest-Auth]]

**Objective**: Establish a local HTTP server with Digest Authentication to simulate a vulnerable target for timing measurements.

**Instructions**: Start a Python-based HTTP server configured for Digest Authentication on port 8080 using [[commands/python3-http-server-digest]]:

```bash
python3 -m http.server 8080 --digest
```

**Expected Output**: Server output indicating it's running on http://localhost:8080, serving protected resources.

**Success Indicators**:
- Server starts without errors
- Access to http://localhost:8080/protected requires authentication

### Step 2: Execute Timing Attack PoC
procedure: [[procedures/Execute-Timing-Attack-PoC]]

**Objective**: Send authentication requests using curl with different algorithms to measure response times and exploit the non-constant-time comparison.

**Instructions**: Run the PoC script against the local server using [[commands/python3-poc-timing-attack]]:

```bash
python3 poc_timing_attack.py http://localhost:8080/protected
```

The script tests algorithms like MD5, MD5-sess, and SHA-1, capturing timings during curl's strcmp() at digest.c line 360.

**Expected Output**: Timing logs such as 'Testing algorithm: MD5 - 963236.5 ns' for each attempt.

**Success Indicators**:
- Script completes without errors
- Multiple timing measurements recorded

### Step 3: Observe Timing Differences
procedure: [[procedures/Analyze-Response-Timings]]

**Objective**: Review response times to identify discrepancies caused by the vulnerable string comparison in curl.

**Instructions**: Examine the PoC output for variations in response times across algorithms. No additional command needed; analyze printed results.

**Expected Output**: Timings like MD5: 963236.5 ns, MD5-sess: 826390.0 ns, SHA-1: 814495.0 ns, showing differences due to strcmp() early exits.

**Success Indicators**:
- Clear timing variations observed (e.g., one algorithm takes longer)
- Confirmation of non-constant-time behavior

### Step 4: Identify Supported Algorithm
procedure: [[procedures/Identify-Supported-Algorithm]]

**Objective**: Use timing deviations to fingerprint the server's supported Digest algorithm, aiding reconnaissance.

**Instructions**: Calculate deviations from the PoC results (e.g., MD5 shows +25.9% deviation). The longest time indicates the matched algorithm.

**Expected Output**: Detection message like 'VULNERABILITY CONFIRMED: Timing attack possible. The server likely uses algorithm: MD5'.

**Success Indicators**:
- Specific algorithm identified (e.g., MD5)
- Reconnaissance value confirmed for targeting weaker configs

## Attack Chain Summary

### Key Achievements

1. Simulated vulnerable server setup for controlled testing
2. Exploited curl's timing side-channel to measure authentication discrepancies
3. Fingerprinted supported algorithms like MD5 via response analysis
4. Demonstrated low-impact reconnaissance potential despite protocol announcements

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Vulnerability Scanning]] Vulnerability Scanning
- [[Hardware]] Gather Victim Host Information: Hardware

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance

---

*Last updated: 2024-12-14T00:00:00Z*
