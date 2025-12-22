---
id: ac-nextcloud-ssrf-portscan-1746582
tags:
  - ssrf
  - blind-ssrf
  - port-scanning
  - nextcloud
  - internal-recon
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Configure-Valid-IMAP-Settings-for-Mail-Setup]]'
  - '[[procedures/Send-SSRF-POST-Request-via-smtpHost]]'
  - '[[procedures/Measure-Response-Times-for-Port-Detection]]'
  - '[[procedures/Enumerate-Internal-Services-via-Port-Probing]]'
step_count: 4
techniques:
  - '[[Network Service Scanning]]'
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:39:09.862Z'
description: >-
  Multi-stage attack exploiting blind SSRF in Nextcloud Mail app to perform port
  scanning on internal network services using response timing differences.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
  - '[[Active Scanning]]'
---
# Blind SSRF Port Scanning via Nextcloud Mail App smtpHost Parameter

Multi-stage attack chain demonstrating exploitation of a blind Server-Side Request Forgery (SSRF) vulnerability in the Nextcloud Mail app. An authenticated user can configure mail settings to force the server to connect to arbitrary internal hosts and ports, using response timing to infer open services without direct output, enabling reconnaissance of sensitive internal infrastructure.

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
    A[Configure IMAP] --> B[Trigger SMTP SSRF]
    B --> C[Time Responses]
    C --> D[Enumerate Services]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Nextcloud instance with Mail app enabled
- Required services/ports: IMAP (993), SMTP (variable)
- Network access requirements: Authenticated access to Nextcloud web interface

### Initial Access Requirements

- Valid Nextcloud user credentials
- Network position: External or internal authenticated user
- Prior access needed: Mail app permissions

## Detailed Attack Procedures

### Step 1: Configure Valid IMAP Settings
procedure: [[procedures/Configure-Valid-IMAP-Settings-for-Mail-Setup]]

**Objective**: Establish valid IMAP configuration to bypass initial validation and reach SMTP checks.

**Instructions**: Set up IMAP parameters using a known valid server to ensure the request proceeds to SMTP validation.

**Expected Output**: Successful IMAP validation, allowing SMTP attempt.

**Success Indicators**:
- Response indicates IMAP check passed (no early error)
- Request advances to SMTP connection phase

### Step 2: Trigger SSRF via smtpHost
procedure: [[procedures/Send-SSRF-POST-Request-via-smtpHost]]

**Objective**: Send a POST request with malicious smtpHost to force internal connections.

**Instructions**: Use [[commands/curl-post-mail-setup]] to submit the payload targeting localhost and a specific port.

```bash
curl -X POST -H "OCS-APIRequest: true" -H "Content-Type: application/json" -d '{"imapHost":"ssl0.ovh.net","imapPort":993,"imapSslMode":"ssl","imapUser":"user","imapPassword":"pass","smtpHost":"127.0.0.1","smtpPort":8080,"smtpSslMode":"none","smtpUser":"user","smtpPassword":"pass"}' https://nextcloud.example.com/ocs/v2.php/apps/mail/api/v1/accounts
```

**Expected Output**: Server response after attempting SMTP connection to 127.0.0.1:8080.

**Success Indicators**:
- No immediate validation error on smtpHost
- Delayed response if port open

### Step 3: Detect Open Ports via Timing
procedure: [[procedures/Measure-Response-Times-for-Port-Detection]]

**Objective**: Analyze response delays to identify open vs. closed ports.

**Instructions**: Repeat Step 2 for multiple ports, timing the responses with [[commands/curl-post-mail-setup]].

**Expected Output**: Response times >1000ms for open ports, <100ms for closed.

**Success Indicators**:
- Consistent delays correlating to open services
- Ability to distinguish port states

### Step 4: Probe and Enumerate Services
procedure: [[procedures/Enumerate-Internal-Services-via-Port-Probing]]

**Objective**: Map internal services by scanning common ports.

**Instructions**: Target ports like 80, 443, 8080 using repeated [[commands/curl-post-mail-setup]] executions.

**Expected Output**: Timing data revealing services (e.g., 5200ms for Apache2 on 80).

**Success Indicators**:
- Identification of services like Apache2, PostgreSQL, Redis
- Mapping of internal infrastructure

## Attack Chain Summary

### Key Achievements

1. Bypassed validation to reach SSRF trigger
2. Performed blind port scanning without direct feedback
3. Enumerated sensitive internal services (Apache2, CrowdSec, PostgreSQL, Redis)

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Network Service Scanning]] Network Service Scanning
- [[Active Scanning]] Active Scanning: Scanning IP Blocks

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery
- [[Reconnaissance]] Reconnaissance

---
*Last updated: 2023-10-01T00:00:00Z*
