---
id: ac-uuid-001
tags:
  - subdomain-takeover
  - dns
  - heroku
  - reconnaissance
type: attack_chain
tools:
  - '[[tools/knockpy]]'
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
  - Heroku
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Subdomain-Enumeration-with-Knockpy]]'
  - '[[procedures/Verify-Dangling-DNS-Records-for-Takeover]]'
step_count: 2
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T05:32:23.011Z'
description: >-
  A reconnaissance-driven attack chain identifying and verifying potential
  subdomain takeover opportunities through dangling DNS records pointing to
  unclaimed Heroku applications.
skill_level: intermediate
impact_level: medium
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Subdomain Takeover via Dangling Heroku DNS Record

Multi-stage attack chain demonstrating reconnaissance to identify subdomain takeover vulnerabilities via dangling DNS records on Heroku.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Enumerate Subdomains] --> B[Verification: Check Dangling Records]
    B --> C[Potential Takeover: Register and Host Malicious Content]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/knockpy]]

### Target Environment

- Web platform with DNS records
- Heroku services
- No specific ports required; uses standard HTTP/HTTPS (80/443)

### Initial Access Requirements

- Public internet access to the target domain
- No credentials needed for reconnaissance phase
- Browser for verification

## Detailed Attack Procedures

### Step 1: Initial Reconnaissance
procedure: [[procedures/Subdomain-Enumeration-with-Knockpy]]

**Objective**: Discover subdomains of the target domain to identify potential dangling records.

**Instructions**: Execute the subdomain enumeration using [[commands/knockpy-enumerate-subdomains]] to scan for hidden or forgotten subdomains:

```bash
knockpy gratipay.com
```

**Expected Output**: A list of discovered subdomains, including potentially vulnerable ones like 'www.gratipay.com.herokudns.com'.

**Success Indicators**:
- Subdomains enumerated successfully
- Anomalous subdomains (e.g., those with third-party service suffixes like herokudns.com) identified

### Step 2: Verification of Takeover Potential
procedure: [[procedures/Verify-Dangling-DNS-Records-for-Takeover]]

**Objective**: Confirm if discovered subdomains point to unclaimed resources, enabling potential takeover.

**Instructions**: Access the suspicious subdomain in a web browser to check for service-specific error messages indicating an unregistered app. For Heroku, navigate to the URL and observe the response.

No command-line tool is required here; use a browser like Firefox or Chrome to visit 'http://www.gratipay.com.herokudns.com'.

**Expected Output**: Heroku error page stating 'No such app', confirming the DNS record is dangling and unclaimed.

**Success Indicators**:
- Error message from the service (e.g., Heroku's 'No such app')
- No active content served, indicating takeover opportunity

## Attack Chain Summary

### Key Achievements

1. Identified a dangling DNS record for subdomain takeover
2. Verified the unclaimed status on Heroku
3. Highlighted theoretical impact of hosting malicious content

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Hardware]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]

---
*Last updated: 2023-10-01T00:00:00Z*
