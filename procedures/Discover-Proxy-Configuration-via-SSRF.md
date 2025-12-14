---
id: proc-discover-proxy-pac
tags:
  - ssrf
  - configuration
  - proxysg
type: procedure
tools:
  - '[[tools/nc-netcat]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/echo-nc-ssrf-trigger]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T04:39:10.077Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Discover-Proxy-Configuration-via-SSRF

## Summary

Use SSRF to retrieve the Proxy Auto-Configuration (PAC) file, exposing internal proxy settings.

## Description

Targeting /proxy_pac_file via SSRF returns the PAC content, revealing ProxySG proxies on port 8080 for HTTP/HTTPS/FTP.

## Requirements

1. SSRF confirmed
2. Knowledge of PAC file path

## Defense

Defensive measures and detection strategies:

- Restrict PAC file access to internal only
- Authenticate proxy config endpoints

## Objectives

1. Exfiltrate PAC file
2. Identify proxy details
3. Enable proxy chaining

## Instructions

### Step 1: Request PAC File

**Context**: Craft SSRF to internal PAC endpoint.

**Command** ([[commands/echo-nc-ssrf-trigger]]):
```bash
echo -ne "GET http://internal-host/proxy_pac_file HTTP/1.1\\r\\n\\r\\n" | nc target-ip 80
```

> Returns PAC script with proxy configs.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/echo-nc-ssrf-trigger]]

## Tools Used

- [[tools/nc-netcat]]

## Tags

- [[ssrf]]
- [[configuration]]
- [[proxysg]]
