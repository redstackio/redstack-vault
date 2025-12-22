---
tags:
  - authorization-bypass
  - akamai
  - sso
  - dns-recon
  - ssl-inspection
  - dod
  - confidential-data
type: attack_chain
tools:
  - '[[tools/dig]]'
  - '[[tools/openssl]]'
  - '[[tools/perl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Attempt-Initial-Access-to-Application-URL]]'
  - '[[procedures/DNS-Lookup-to-Identify-Origin-IP-Behind-Akamai]]'
  - '[[procedures/Verify-Origin-IP-Using-SSL-Certificate-Inspection]]'
  - '[[procedures/Direct-Access-to-Origin-Server-Bypassing-SSO]]'
  - '[[procedures/Navigate-and-Exfiltrate-Sensitive-Documents]]'
step_count: 5
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:57.328Z'
description: >-
  Multi-stage attack chain exploiting an authorization bypass by directly
  accessing the origin IP of a U.S. Department of Defense application,
  circumventing Akamai load balancer and SSO authentication to access
  confidential aircraft and missile documents.
skill_level: intermediate
impact_level: high
id: ff34ca4e-15e3-412d-a625-a6898ee1765b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Authorization Bypass on DoD Application via Direct Origin IP Access Bypassing Akamai SSO

Multi-stage attack chain demonstrating a complete attack workflow to bypass authorization on a U.S. Department of Defense application hosted behind Akamai, allowing unauthenticated access to confidential documents.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access Attempt] --> B[DNS Reconnaissance]
    B --> C[Certificate Verification]
    C --> D[Origin IP Access]
    D --> E[Data Exfiltration]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/dig]]
- [[tools/openssl]]
- [[tools/perl]]

### Target Environment

- Web platform with Akamai load balancer
- HTTPS service on port 443
- .NET/ASP.NET application with SSO enforcement
- Network access to perform DNS queries and direct IP connections

### Initial Access Requirements

- No credentials required
- Public internet access to the target domain
- No prior access needed beyond DNS resolution

## Detailed Attack Procedures

### Step 1: Attempt Initial Access to Application URL
procedure: [[procedures/Attempt-Initial-Access-to-Application-URL]]

**Objective**: Verify that the application URL enforces SSO authentication via redirect.

**Instructions**: Open a web browser and navigate to the target application URL https://███.

**Expected Output**: Redirect to https://█████████/pool/sso/authenticate/l/2?m=GET&r=t&u=https%3A%2F%2F████████%2F for SSO login.

**Success Indicators**:
- Redirect to SSO authentication page observed
- Access denied without authentication

### Step 2: DNS Lookup to Identify Origin IP Behind Akamai
procedure: [[procedures/DNS-Lookup-to-Identify-Origin-IP-Behind-Akamai]]

**Objective**: Trace the CNAME chain to reveal the Akamai edge server and identify the potential origin IP.

**Instructions**: Use [[commands/dig-dns-lookup-for-origin-ip]] to query the A record of the target domain:

```bash
dig A ████
```

**Expected Output**: ANSWER SECTION showing CNAME chain like ███. 2386 IN CNAME █████. and A record pointing to Akamai edge server.

**Success Indicators**:
- CNAME chain to Akamai identified
- Potential origin IP candidates noted from further tracing

### Step 3: Verify Origin IP Using SSL Certificate Inspection
procedure: [[procedures/Verify-Origin-IP-Using-SSL-Certificate-Inspection]]

**Objective**: Confirm the suspected origin IP hosts the target domain by inspecting the SSL certificate's DNS names.

**Instructions**: Execute [[commands/openssl-inspect-ssl-certificate-for-dns-names]] to connect to the IP and extract certificate details:

```bash
true | openssl s_client -connect ██████:443 2>/dev/null | openssl x509 -noout -text | perl -l -0777 -ne '@names=/\bDNS:([^\s,]+)/g; print join("\n", sort @names);'
```

**Expected Output**: List of DNS names from the certificate, including █████████ confirming the match.

**Success Indicators**:
- Target domain appears in Subject Alternative Names (SAN)
- Certificate matches the application's domain

### Step 4: Direct Access to Origin Server Bypassing SSO
procedure: [[procedures/Direct-Access-to-Origin-Server-Bypassing-SSO]]

**Objective**: Bypass Akamai and SSO by connecting directly to the origin IP, gaining authenticated access without login.

**Instructions**: In a web browser, directly navigate to https://█████ using the verified origin IP.

**Expected Output**: Application loads without SSO redirect, presenting authenticated user interface.

**Success Indicators**:
- No authentication prompt
- Access to protected pages granted

### Step 5: Navigate and Exfiltrate Sensitive Documents
procedure: [[procedures/Navigate-and-Exfiltrate-Sensitive-Documents]]

**Objective**: Search, view, and download confidential documents related to aircraft and missile issues.

**Instructions**: Use the sidebar to navigate to /Guest/MessageSearch.aspx for searching messages, then /Guest/MessagesDetails.aspx for viewing details, and download attached documents.

**Expected Output**: Access to search results, message details, and downloadable files containing sensitive data.

**Success Indicators**:
- Confidential documents viewed and downloaded
- No access restrictions encountered

## Attack Chain Summary

### Key Achievements

1. Bypassed Akamai load balancer and SSO authentication
2. Identified and verified origin IP through DNS and SSL inspection
3. Gained unauthenticated access to protected DoD application
4. Exfiltrated confidential aircraft and missile documents

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

---

*Last updated: 2023-10-01T00:00:00Z*
