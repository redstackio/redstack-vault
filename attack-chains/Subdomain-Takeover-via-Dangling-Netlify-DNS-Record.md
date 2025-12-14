---
tags:
  - subdomain-takeover
  - netlify
  - dns-misconfiguration
type: attack_chain
tools:
  - '[[tools/Subfinder]]'
tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - Netlify
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Detect-and-Exploit-Netlify-Subdomain-Takeover]]'
step_count: 1
techniques:
  - '[[Active Scanning]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:23.660Z'
description: >-
  An attack chain exploiting a misconfigured DNS record pointing to an unclaimed
  Netlify target, allowing takeover of a subdomain for malicious control.
skill_level: intermediate
impact_level: high
id: 45bcc31a-d018-4ed0-b9d2-d52c63cfc697
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
  - '[[Exploit Public-Facing Application]]'
---
# Subdomain Takeover via Dangling Netlify DNS Record

Multi-stage attack chain demonstrating a complete attack workflow exploiting a dangling DNS record for subdomain takeover on Netlify.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discovery of Misconfigured Subdomain] --> B[Subdomain Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Subfinder]]
- [[commands/dig-dns-lookup]]

### Target Environment

- Web platform with DNS records
- Netlify as hosting service
- Public DNS resolution

### Initial Access Requirements

- No credentials required for discovery
- Internet access for DNS queries
- Netlify account for claiming the subdomain

## Detailed Attack Procedures

### Step 1: Discovery and Takeover
procedure: [[procedures/Detect-and-Exploit-Netlify-Subdomain-Takeover]]

**Objective**: Identify a misconfigured subdomain with a dangling CNAME to Netlify and claim control for potential phishing or content manipulation.

**Instructions**: Begin by enumerating subdomains using [[tools/Subfinder]] to identify potential targets:

```bash
subfinder -d get8x8.com -o subdomains.txt
```

Next, probe for live subdomains and check DNS records using [[commands/dig-dns-lookup]] on suspected subdomains like "██.get8x8.com":

```bash
dig CNAME ██.get8x8.com
```

If the CNAME points to an unclaimed Netlify target (e.g., something like "project-name.netlify.app" that resolves but shows no active site), verify takeover eligibility by attempting to access the Netlify dashboard and search for the dangling target.

**Expected Output**: DNS response showing CNAME to Netlify; Netlify dashboard confirms unclaimed status.

**Success Indicators**:
- Subdomain enumeration yields misconfigured entry
- DNS query reveals dangling Netlify pointer
- Successful claim on Netlify grants control

## Attack Chain Summary

### Key Achievements

1. Discovery of vulnerable subdomain through enumeration
2. Confirmation of dangling DNS record to Netlify
3. Potential takeover enabling malicious content hosting

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Active Scanning]] Active Scanning
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
