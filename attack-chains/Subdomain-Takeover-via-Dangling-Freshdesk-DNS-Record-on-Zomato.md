---
id: ac-subdomain-takeover-fddkim-zomato
tags:
  - subdomain-takeover
  - dns-dangling
  - freshdesk
  - phishing
  - impersonation
type: attack_chain
tools:
  - '[[tools/Subfinder]]'
  - '[[tools/Dig]]'
tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - DNS
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Enumerate-Subdomains-for-Takeover]]'
  - '[[procedures/Verify-Dangling-DNS-Records]]'
  - '[[procedures/Claim-Subdomain-on-Freshdesk]]'
step_count: 3
techniques:
  - '[[Hardware]]'
  - '[[T1583.001]]'
updated_at: '2025-12-14T04:38:39.900Z'
description: >-
  An attack chain exploiting a dangling DNS record for fddkim.zomato.com
  pointing to an inactive Freshdesk instance, allowing an attacker to claim the
  subdomain and host malicious content.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Hardware]]'
  - '[[T1583.001]]'
---
# Subdomain Takeover via Dangling Freshdesk DNS Record on Zomato

Multi-stage attack chain demonstrating the discovery and exploitation of a subdomain takeover vulnerability on fddkim.zomato.com, where a dangling DNS record allowed registration on Freshdesk for potential phishing or impersonation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Subdomain Enumeration] --> B[Verify Dangling DNS]
    B --> C[Claim Subdomain on Freshdesk]
    C --> D[Host Malicious Content]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Subfinder]]
- [[tools/Dig]]

### Target Environment

- DNS resolution access
- Internet connectivity for subdomain enumeration
- Freshdesk account for claiming (free tier sufficient)

### Initial Access Requirements

- No prior credentials needed
- Public DNS queries
- No authenticated access to target

## Detailed Attack Procedures

### Step 1: Subdomain Enumeration
procedure: [[procedures/Enumerate-Subdomains-for-Takeover]]

**Objective**: Identify all subdomains of the target domain to uncover potential takeover opportunities.

**Instructions**: Use [[commands/subfinder-enumerate]] to passively enumerate subdomains:

```bash
subfinder -d zomato.com -all -o subdomains.txt
```

Filter for interesting subdomains like those potentially using third-party services (e.g., fddkim).

**Expected Output**: A text file listing subdomains, including fddkim.zomato.com.

**Success Indicators**:
- List of 100+ subdomains generated
- Identification of service-specific subdomains (e.g., Freshdesk patterns)

### Step 2: Verify Dangling DNS Records
procedure: [[procedures/Verify-Dangling-DNS-Records]]

**Objective**: Check DNS records for dangling pointers to inactive third-party services like Freshdesk.

**Instructions**: Query DNS for the subdomain using [[commands/dig-lookup]]:

```bash
dig fddkim.zomato.com TXT +short
```

Look for CNAME or TXT records pointing to unclaimed Freshdesk endpoints (e.g., fddkim.freshdesk.com). Attempt to access the pointed URL to confirm inactivity.

**Expected Output**: DNS response showing a record to an inactive Freshdesk instance.

**Success Indicators**:
- CNAME points to claimable service
- HTTP access to the subdomain returns 404 or service unclaimed message

### Step 3: Claim Subdomain on Freshdesk
procedure: [[procedures/Claim-Subdomain-on-Freshdesk]]

**Objective**: Register the dangling subdomain on Freshdesk to gain control and host phishing or malicious content.

**Instructions**: Create a free Freshdesk account and navigate to domain settings to claim fddkim.freshdesk.com, which propagates to fddkim.zomato.com via the dangling DNS.

**Expected Output**: Successful claim confirmation; subdomain now resolves to attacker's Freshdesk page.

**Success Indicators**:
- Subdomain under attacker control
- Ability to upload custom HTML/JS for phishing

## Attack Chain Summary

### Key Achievements

1. Discovery of dangling DNS record via enumeration
2. Verification of takeover feasibility on Freshdesk
3. Successful subdomain claim enabling impersonation attacks

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Hardware]] Gather Victim Host Information: Domains
- [[T1583.001]] Acquire Infrastructure: Domains

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
