---
id: ac-uuid-001
name: Client Certificate Reuse on Redirects for Unauthorized Access via Curl
tags:
  - curl
  - tls
  - client-certificate
  - redirect
  - authentication-abuse
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Lateral Movement]]'
verified: false
platforms:
  - Linux
  - Windows
  - macOS
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Configure-Target-Site-with-Client-Cert-Auth]]'
  - '[[procedures/Prepare-Client-Certificate-and-Key]]'
  - '[[procedures/Setup-Attacker-Controlled-Redirect-Site]]'
  - '[[procedures/Execute-Curl-with-Certificate-Reuse]]'
  - '[[procedures/Observe-Unauthorized-Access]]'
step_count: 5
techniques:
  - '[[Valid Accounts]]'
  - '[[Private Keys]]'
updated_at: '2025-12-14T17:30:58.739Z'
description: >-
  An attack chain exploiting curl's reuse of client certificates during
  redirects to access protected resources on a target site using victim
  credentials.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Private Keys]]'
---
# Client Certificate Reuse on Redirects for Unauthorized Access via Curl

Multi-stage attack chain demonstrating exploitation of curl's client certificate reuse during redirects to gain unauthorized access to protected resources.

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
    A[Setup Target Authentication] --> B[Prepare Victim Credentials]
    B --> C[Configure Attacker Redirect]
    C --> D[Execute Curl with Redirect Follow]
    D --> E[Access Protected Resource]

    style A fill:#e74c3c
    style B fill:#e74c3c
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Web server requiring client certificate authentication (e.g., HTTPS on port 443)
- Attacker-controlled web server for redirects
- Linux, Windows, or macOS host for executing curl

### Initial Access Requirements

- Victim's client certificate and private key (client.crt and client.key)
- Network access to both attacker site and target site
- No prior access to target needed, but certificate must be valid for target

## Detailed Attack Procedures

### Step 1: Configure Target Site
procedure: [[procedures/Configure-Target-Site-with-Client-Cert-Auth]]

**Objective**: Set up the target site to require client certificate authentication for protected resources.

**Instructions**: Configure the target web server (e.g., Apache or Nginx) to enforce mutual TLS authentication for accessing sensitive endpoints like /secretfile.

**Expected Output**: Target site rejects unauthenticated requests and prompts for client cert.

**Success Indicators**:
- Test access without cert fails with 401/403
- Access with valid cert succeeds

### Step 2: Prepare Client Certificate
procedure: [[procedures/Prepare-Client-Certificate-and-Key]]

**Objective**: Obtain or generate a valid client certificate and private key for the victim.

**Instructions**: Use existing cert/key files or generate self-signed ones valid for the target site.

**Expected Output**: client.crt and client.key files ready for use.

**Success Indicators**:
- Files exist and are readable
- Cert validates against target CA if applicable

### Step 3: Setup Attacker Redirect
procedure: [[procedures/Setup-Attacker-Controlled-Redirect-Site]]

**Objective**: Create an attacker-controlled site that redirects to the target's protected resource.

**Instructions**: Host a simple web server on evilsite.tld that returns a 302 redirect to https://targetsite.tld/secretfile.

**Expected Output**: Visiting https://evilsite.tld/something redirects to target.

**Success Indicators**:
- Redirect response (HTTP 302) with Location header points to target/secretfile
- No authentication required on attacker site

### Step 4: Execute Curl Attack
procedure: [[procedures/Execute-Curl-with-Certificate-Reuse]]

**Objective**: Use curl to follow the redirect and reuse the client certificate on the target site.

**Instructions**: Run the curl command with -L to follow redirects, providing the cert and key:

using [[commands/curl-follow-redirect-with-cert]]:

```bash
curl -L --cert client.crt --key client.key https://evilsite.tld/something
```

**Expected Output**: Content of /secretfile from target site is retrieved and displayed.

**Success Indicators**:
- Curl output shows protected content
- No additional auth prompts

### Step 5: Observe Access
procedure: [[procedures/Observe-Unauthorized-Access]]

**Objective**: Verify that the victim's certificate was used to access the target without direct interaction.

**Instructions**: Inspect the curl output for the secret content, confirming authentication succeeded via reuse.

**Expected Output**: Sensitive data from target site visible in response.

**Success Indicators**:
- Unauthorized access confirmed
- No private key compromise needed

## Attack Chain Summary

### Key Achievements

1. Demonstrated certificate reuse across hosts during redirects
2. Gained access to protected resources using victim's credentials
3. Highlighted risks in applications that follow untrusted redirects with auth

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Private Keys]] Private Keys

### MITRE ATT&CK Tactics

- [[Lateral Movement]] Lateral Movement

---

*Last updated: 2023-10-01T12:00:00Z*
