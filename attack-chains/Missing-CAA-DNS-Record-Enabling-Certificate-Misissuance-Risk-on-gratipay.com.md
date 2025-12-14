---
id: ac-uuid-missing-caa-gratipay
tags:
  - dns
  - caa
  - certificate
  - tls
  - ssl
  - misconfiguration
type: attack_chain
tools:
  - '[[tools/Google-Public-DNS-Lookup]]'
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - DNS
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Query-DNS-for-CAA-Records]]'
step_count: 1
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:28:51.754Z'
description: >-
  A reconnaissance procedure to identify the absence of Certificate Authority
  Authorization (CAA) DNS records, increasing the risk of unauthorized SSL/TLS
  certificate issuance for the domain gratipay.com.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Missing CAA DNS Record Enabling Certificate Misissuance Risk on gratipay.com

Multi-stage attack chain demonstrating a complete attack workflow.

The absence of a CAA DNS record for gratipay.com allows any Certificate Authority to issue certificates for the domain, elevating the risk of phishing or man-in-the-middle attacks through fraudulent certificates. This chain focuses on reconnaissance to detect this misconfiguration via DNS querying.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Query DNS for CAA] --> B[Identify Missing Record and Risk]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Google-Public-DNS-Lookup]]

### Target Environment

- DNS resolution services
- Public access to DNS queries
- No authentication required

### Initial Access Requirements

- Internet connectivity
- No credentials needed
- Public DNS resolver access

## Detailed Attack Procedures

### Step 1: DNS Reconnaissance for CAA Records
procedure: [[procedures/Query-DNS-for-CAA-Records]]

**Objective**: Query the DNS for CAA resource records (type 257) on the target domain to detect if authorization rules for certificate issuance are missing.

**Instructions**: Use the [[tools/Google-Public-DNS-Lookup]] service to perform the query. Navigate to the tool's web interface and input the domain and record type.

For gratipay.com, construct the query URL as follows:

```url
https://dns.google.com/query?name=gratipay.com&type=257&dnssec=true
```

Submit the query and review the response for CAA records.

**Expected Output**: An empty or "No records found" response indicating the absence of CAA records.

**Success Indicators**:
- No CAA records returned in the DNS response
- Confirmation of missing authorization, signaling elevated risk for certificate misissuance

## Attack Chain Summary

### Key Achievements

1. Successful DNS query revealing missing CAA record
2. Identification of cryptographic misconfiguration
3. Assessment of potential for unauthorized certificate issuance

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Hardware]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]

---
*Last updated: 2023-10-01T00:00:00Z*
