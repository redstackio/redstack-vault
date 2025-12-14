---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - domain-takeover
  - dns
  - github-pages
  - acquisition
  - phishing
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Research-Company-Acquisitions-for-Domain-Takeover]]'
  - '[[procedures/Identify-Dangling-GitHub-Pages-DNS]]'
  - '[[procedures/Claim-Domain-via-GitHub-Repository-Creation]]'
step_count: 3
techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:26.486Z'
description: >-
  A multi-stage attack exploiting a dangling DNS record for obviousengine.com, a
  domain from a Snapchat acquisition, to achieve full domain takeover via
  unclaimed GitHub Pages.
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Exploit Public-Facing Application]]'
---
# Domain Takeover of Snapchat Acquisition Domain via Dangling GitHub Pages DNS

Multi-stage attack chain demonstrating a complete domain takeover workflow by exploiting abandoned DNS records from a company acquisition.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Research Acquisitions] --> B[Discovery: Identify Dangling DNS]
    B --> C[Exploitation: Claim Domain via GitHub]
    C --> D[Objective: Full Domain Control]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser for research and verification
- GitHub account for claiming the repository

### Target Environment

- Public DNS resolution
- Access to Crunchbase or similar acquisition databases
- GitHub platform availability

### Initial Access Requirements

- No prior credentials needed
- Internet access for research and GitHub operations
- No specific network position required

## Detailed Attack Procedures

### Step 1: Research Company Acquisitions
procedure: [[procedures/Research-Company-Acquisitions-for-Domain-Takeover]]

**Objective**: Identify potentially abandoned domains from recent acquisitions that may have dangling DNS records.

**Instructions**: Use a search engine or database like Crunchbase to query acquisitions by the target company (e.g., Snapchat). Focus on acquired entities with custom domains. For example, search for "Snapchat acquisitions" and review company profiles for domain names like obviousengine.com.

**Expected Output**: List of acquired companies and their associated domains, such as obviousengine.com linked to Obvious Engineering.

**Success Indicators**:
- Acquired domains identified
- Links to company overviews confirmed (e.g., https://www.crunchbase.com/organization/obvious-engineering)

### Step 2: Identify Dangling DNS Records
procedure: [[procedures/Identify-Dangling-GitHub-Pages-DNS]]

**Objective**: Verify if the target domain resolves to an unclaimed or default service, indicating vulnerability to takeover.

**Instructions**: Visit the domain (e.g., obviousengine.com) in a web browser. Check for indicators of dangling records, such as a default GitHub Pages 404 page or unclaimed repository message, suggesting DNS points to username.github.io without an active repo.

**Expected Output**: Browser displays a GitHub Pages default page, confirming the DNS CNAME points to an unused GitHub-hosted site.

**Success Indicators**:
- Domain resolves but shows unclaimed GitHub content
- No custom content from the original owner

### Step 3: Claim Domain via GitHub
procedure: [[procedures/Claim-Domain-via-GitHub-Repository-Creation]]

**Objective**: Take control of the domain by creating and configuring a GitHub repository to hijack the DNS pointer.

**Instructions**: Log in to GitHub and create a new repository named exactly after the domain (e.g., obviousengine.com). Enable GitHub Pages in the repository settings, add a CNAME file with the domain name, and push an index.html file with custom content to verify control. Update DNS if needed, but in this case, the existing CNAME allows immediate hijacking.

**Expected Output**: The domain now resolves to the custom content hosted on the new GitHub Pages site.

**Success Indicators**:
- Custom page loads when visiting the domain
- Full control confirmed for hosting arbitrary content

## Attack Chain Summary

### Key Achievements

1. Identified vulnerable domain from acquisition research
2. Confirmed dangling DNS to unclaimed GitHub Pages
3. Achieved domain takeover, enabling phishing or malware hosting

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
