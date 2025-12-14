---
id: ac-domain-takeover-fastly-gitlab-csp
tags:
  - domain-takeover
  - csp-bypass
  - xss
  - fastly
  - gitlab
type: attack_chain
tools:
  - '[[tools/Fastly-Management-Dashboard]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Register-Fastly-Account]]'
  - '[[procedures/Navigate-to-Fastly-Services-Management]]'
  - '[[procedures/Create-New-Fastly-Service]]'
  - '[[procedures/Add-Target-Domain-to-Fastly-Service]]'
  - '[[procedures/Configure-Hosts-in-Fastly-Service]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T04:51:10.681Z'
description: >-
  Multi-stage attack exploiting a domain takeover vulnerability in Fastly's free
  TLS service to claim a subdomain whitelisted in GitLab's CSP, enabling CSP
  bypass and potential client-side attacks like XSS.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Domain Takeover of gl-canary.freetls.fastly.net to Bypass GitLab CSP

Multi-stage attack chain demonstrating a complete workflow to claim a Fastly subdomain whitelisted in GitLab's CSP header, allowing control over resources loaded by GitLab.com and enabling attacks like XSS or CDN abuse.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Account Registration] --> B[Service Management Access]
    B --> C[Service Creation]
    C --> D[Domain Addition]
    D --> E[Host Configuration]
    E --> F[CSP Bypass and Exploitation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Fastly-Management-Dashboard]]

### Target Environment

- Web platform with access to Fastly's free TLS service
- No specific ports required; browser-based access
- Internet connectivity for domain registration and configuration

### Initial Access Requirements

- No prior credentials needed for GitLab; only a free Fastly account
- Public internet access
- Basic understanding of CDN and CSP mechanics

## Detailed Attack Procedures

### Step 1: Account Registration
procedure: [[procedures/Register-Fastly-Account]]

**Objective**: Establish control over a Fastly account to access domain provisioning features.

**Instructions**: Visit the Fastly signup page and complete the registration process to create a new account. This grants access to the free TLS service, which is key for subdomain claiming.

**Expected Output**: Confirmation email and login access to the Fastly dashboard.

**Success Indicators**:
- Account created successfully
- Able to log in to manage.fastly.com

### Step 2: Access Services Management
procedure: [[procedures/Navigate-to-Fastly-Services-Management]]

**Objective**: Reach the interface for creating and managing Fastly services.

**Instructions**: After logging in, navigate directly to the services management page at https://manage.fastly.com/services/all to prepare for service creation.

**Expected Output**: Dashboard displaying available services (initially empty for new accounts).

**Success Indicators**:
- Services page loads without errors
- Option to create new service is visible

### Step 3: Initiate Service Creation
procedure: [[procedures/Create-New-Fastly-Service]]

**Objective**: Set up a new Fastly service as the foundation for domain takeover.

**Instructions**: In the Fastly dashboard, select the option to create a new service, providing basic details like a service name.

**Expected Output**: New service entry created with a unique ID.

**Success Indicators**:
- Service creation confirmation
- Service details page accessible

### Step 4: Add Target Domain
procedure: [[procedures/Add-Target-Domain-to-Fastly-Service]]

**Objective**: Claim the vulnerable subdomain by adding it to the service.

**Instructions**: In the service configuration, add 'gl-canary.global.ssl.fastly.net' as the domain. Fastly's free TLS will automatically provision and control 'gl-canary.freetls.fastly.net'.

**Expected Output**: Domain added and TLS certificate provisioned.

**Success Indicators**:
- Domain status shows as active
- Subdomain resolves to attacker's service

### Step 5: Configure Hosts for Control
procedure: [[procedures/Configure-Hosts-in-Fastly-Service]]

**Objective**: Gain full control over the subdomain to serve malicious content.

**Instructions**: Configure the host settings in the Fastly service to define response behaviors, such as redirecting to malicious scripts or hosting XSS payloads.

**Expected Output**: Custom configurations applied and testable via domain access.

**Success Indicators**:
- Domain serves attacker-controlled content
- GitLab.com loads resources from the subdomain, bypassing CSP

## Attack Chain Summary

### Key Achievements

1. Successful takeover of a CSP-whitelisted subdomain
2. Bypass of GitLab's Content Security Policy restrictions
3. Enablement of client-side attacks like XSS or CDN resource injection

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
