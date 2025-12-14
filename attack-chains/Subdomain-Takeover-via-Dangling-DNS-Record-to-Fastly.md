---
tags:
  - subdomain-takeover
  - dns
  - fastly
  - misconfiguration
type: attack_chain
tools:
  - '[[tools/host]]'
tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - DNS
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Detect-Subdomain-Takeover-via-HTTP-Access]]'
  - '[[procedures/Confirm-Subdomain-Takeover-via-DNS-Lookup]]'
step_count: 2
techniques:
  - '[[Hardware]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:10.603Z'
description: >-
  Discovery and confirmation of a subdomain takeover vulnerability due to a
  dangling DNS record pointing to unregistered Fastly infrastructure, allowing
  potential attacker control over the subdomain.
skill_level: intermediate
impact_level: high
id: 7b585210-a313-4aa6-817d-39d22cd7fb38
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Hardware]]'
  - '[[Exploit Public-Facing Application]]'
---
# Subdomain Takeover via Dangling DNS Record to Fastly

Multi-stage attack chain demonstrating the discovery of a subdomain takeover vulnerability through HTTP access and DNS verification, targeting a dangling record on Fastly infrastructure.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[HTTP Access Check] --> B[DNS Lookup Confirmation]
    B --> C[Potential Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/host]]

### Target Environment

- Web platform with DNS resolution
- Access to public internet for HTTP and DNS queries
- No specific services or ports required beyond standard HTTP (80) and DNS (53)

### Initial Access Requirements

- No credentials needed
- Public network access
- No prior access required

## Detailed Attack Procedures

### Step 1: HTTP Access Check
procedure: [[procedures/Detect-Subdomain-Takeover-via-HTTP-Access]]

**Objective**: Access the suspected subdomain to identify error responses indicating unregistered infrastructure.

**Instructions**: Use a web browser or curl to visit the subdomain URL and observe the response for provider-specific errors.

For example, using a browser or [[commands/curl-http-access]]:

```bash
curl -i http://genghis-cdn.shopify.io/
```

**Expected Output**: A Fastly error page stating 'Fastly error: unknown domain: genghis-cdn.shopify.io. Please check that this domain has been added to a service.'

**Success Indicators**:
- Receipt of a provider error page (e.g., Fastly unknown domain error)
- No legitimate content served from the subdomain

### Step 2: DNS Lookup Confirmation
procedure: [[procedures/Confirm-Subdomain-Takeover-via-DNS-Lookup]]

**Objective**: Verify the DNS resolution to confirm the dangling record points to the provider's infrastructure without active registration.

**Instructions**: Execute a DNS lookup using [[commands/host-dns-lookup]] to resolve the subdomain and check for CNAME aliases to the provider.

```bash
host genghis-cdn.shopify.io
```

**Expected Output**: Resolution showing aliases like 'genghis-cdn.shopify.io is an alias for shopify-e.map.fastly.net' and IP address such as 151.101.60.108.

**Success Indicators**:
- CNAME points to provider infrastructure (e.g., Fastly)
- No active service tied to the record, confirming takeover potential

## Attack Chain Summary

### Key Achievements

1. Identified unregistered subdomain via HTTP error
2. Confirmed dangling DNS record pointing to Fastly
3. Demonstrated potential for attacker to claim and control the subdomain for impersonation or malicious hosting

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Hardware]] Gather Victim Host Information: DNS
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
