---
id: ac-uuid-001
name: Discovery of Dangling DNS Record for Potential Subdomain Takeover on Fastly
tags:
  - subdomain-takeover
  - dns-reconnaissance
  - fastly
  - cloud
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Dangling-DNS-Records-for-Subdomain-Takeover]]'
step_count: 1
techniques:
  - '[[Determine Physical Locations]]'
updated_at: '2025-12-14T05:32:23.694Z'
description: >-
  A reconnaissance-based attack chain identifying a dangling DNS record pointing
  to an unconfigured Fastly service, enabling potential subdomain takeover if
  unmitigated.
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Determine Physical Locations]]'
---
# Discovery of Dangling DNS Record for Potential Subdomain Takeover on Fastly

Multi-stage attack chain demonstrating a complete attack workflow focused on reconnaissance to identify subdomain takeover opportunities via dangling DNS records.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: DNS Enumeration] --> B[Validation: Check Service Configuration]
    B --> C[Potential Takeover Assessment]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- None specific; standard DNS tools like dig or nslookup suffice.

### Target Environment

- Publicly resolvable DNS for the target domain (e.g., rubygems.org).
- Access to DNS query tools.
- No privileged access required.

### Initial Access Requirements

- Internet connectivity for DNS queries.
- No credentials or prior access needed; purely external reconnaissance.

## Detailed Attack Procedures

### Step 1: DNS Reconnaissance and Dangling Record Discovery
procedure: [[procedures/Discover-Dangling-DNS-Records-for-Subdomain-Takeover]]

**Objective**: Enumerate DNS records for the target domain to identify subdomains pointing to unconfigured cloud services like Fastly, which could enable subdomain takeover.

**Instructions**: Begin by querying the DNS records for the target domain and its subdomains using [[commands/dig-query-dns]] to resolve A or CNAME records:

```bash
dig production.s3.rubygems.org
```

Follow up by checking the resolved IP or CNAME against the service provider's configuration. For Fastly, verify if the domain is claimed by attempting to access the subdomain or using provider-specific tools to check service status.

**Expected Output**: DNS response showing a CNAME or A record pointing to Fastly infrastructure (e.g., dualstack.s3-website-us-east-1.amazonaws.com or Fastly IPs) without an active service.

**Success Indicators**:
- DNS record resolves to a cloud provider like Fastly.
- HTTP request to the subdomain returns a provider error page (e.g., Fastly's "Service Not Configured" response).
- No active website or service responds on the subdomain.

## Attack Chain Summary

### Key Achievements

1. Identified a dangling DNS record for production.s3.rubygems.org pointing to unconfigured Fastly.
2. Assessed potential for subdomain takeover, though mitigated by domain control.
3. Demonstrated low-effort reconnaissance leading to vulnerability disclosure.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Determine Physical Locations]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]

---
*Last updated: 2023-10-01T00:00:00Z*
