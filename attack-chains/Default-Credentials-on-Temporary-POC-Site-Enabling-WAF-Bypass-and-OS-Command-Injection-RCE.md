---
id: ac-starbucks-default-creds-rce-881548
tags:
  - default-credentials
  - waf-bypass
  - os-command-injection
  - rce
  - web
type: attack_chain
tools: []
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
  - >-
    [[procedures/Discover-and-Access-Temporary-POC-Site-with-Default-Credentials]]
  - '[[procedures/Bypass-WAF-via-Authenticated-Access-with-Default-Credentials]]'
  - '[[procedures/Exploit-OS-Command-Injection-for-RCE]]'
step_count: 3
techniques:
  - '[[Default Accounts]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:36.760Z'
description: >-
  A multi-stage attack exploiting default credentials on a staging site to
  bypass WAF protections and achieve remote code execution via OS command
  injection.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Default Accounts]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
---
# Default Credentials on Temporary POC Site Enabling WAF Bypass and OS Command Injection RCE

Multi-stage attack chain demonstrating exploitation of a temporary proof-of-concept staging site configured with unchanged default credentials, leading to WAF bypass and remote code execution through OS command injection.

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
    A[Discover POC Site] --> B[Authenticate with Defaults]
    B --> C[Inject OS Commands]
    C --> D[RCE Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser for initial access
- Command-line tools like curl for injection testing

### Target Environment

- Web platform with staging environments
- Accessible via public internet
- Services: HTTP/HTTPS on standard ports (80/443)

### Initial Access Requirements

- No prior credentials needed; defaults like admin/admin assumed
- Network position: External attacker with internet access
- Prior access: None required

## Detailed Attack Procedures

### Step 1: Discover Temporary POC Site
procedure: [[procedures/Discover-and-Access-Temporary-POC-Site-with-Default-Credentials]]

**Objective**: Identify and gain initial foothold on the vulnerable staging site using default credentials.

**Instructions**: Use reconnaissance techniques to enumerate subdomains or staging environments associated with the target domain, such as starbucks.com.cn. Focus on identifiers like 'stg' or 'poc' in subdomain names. Once identified, attempt login with common default credentials (e.g., admin/admin).

**Expected Output**: Successful login to the dashboard or admin panel of alipoc.stg.starbucks.com.cn.

**Success Indicators**:
- Access granted without custom credentials
- Site responds with authenticated session

### Step 2: Bypass WAF via Authenticated Access
procedure: [[procedures/Bypass-WAF-via-Authenticated-Access-with-Default-Credentials]]

**Objective**: Leverage legitimate authentication to circumvent WAF rules that block unauthenticated malicious requests.

**Instructions**: After logging in with default credentials, navigate to protected endpoints within the application. The authenticated session token allows requests that would otherwise be filtered by the WAF.

**Expected Output**: Access to application features without WAF interference, enabling further exploitation.

**Success Indicators**:
- Requests to sensitive endpoints succeed
- No WAF blocks or alerts triggered

### Step 3: Exploit OS Command Injection
procedure: [[procedures/Exploit-OS-Command-Injection-for-RCE]]

**Objective**: Inject and execute arbitrary OS commands on the server to achieve remote code execution.

**Instructions**: In an authenticated session, locate input fields vulnerable to command injection (e.g., search or diagnostic forms). Test with payloads like `; id` appended to inputs. Escalate to full RCE by executing commands such as downloading and running payloads.

For example, use a browser or curl to submit a vulnerable form:

```bash
curl -X POST 'https://alipoc.stg.starbucks.com.cn/vulnerable-endpoint' \
  -H 'Cookie: session=authenticated_token' \
  -d 'input=ping -c 1 127.0.0.1; id'
```

**Expected Output**: Server executes the injected command, returning output like user ID or network ping results.

**Success Indicators**:
- Command output reflected in response
- Arbitrary code runs on server

## Attack Chain Summary

### Key Achievements

1. Unauthorized access to staging environment via defaults
2. Successful WAF evasion through authenticated path
3. Remote code execution on the web server

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Default Accounts]]
- [[Exploit Public-Facing Application]]
- [[Unix Shell]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
