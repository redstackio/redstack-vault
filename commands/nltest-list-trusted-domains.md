---
type: command
executor: cmd
data: nltest /trusted_domains
tags:
  - active-directory
  - discovery
platforms:
  - Windows
verified: true
validated: true
---

# nltest-list-trusted-domains

## Command

```cmd
nltest /trusted_domains
```

## Description

This command uses the nltest utility to list all trusted domains for the current Active Directory domain. It is a quick reconnaissance tool for identifying potential lateral movement paths by revealing interconnected domains.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /trusted_domains | Switch to enumerate trusted domains | Yes |

## Examples

### Basic Usage

```cmd
nltest /trusted_domains
```

### Usage with Output Redirection

```cmd
nltest /trusted_domains > trusted_domains.txt
```

## Expected Output

```
Trusted DC Connection Status Status = 0 0x0 NERR_Success

The command completed successfully

Trusted domains list:
\DOMAIN1.LOCAL
\DOMAIN2.LOCAL
```

A successful run lists trusted domain names. Errors like "Status = 1355 0x54B ERROR_NO_TRUST_SAM_ACCOUNT" indicate no trusts or access issues.

## Related

- [[procedures/Domain-Trust-Enumeration]]
- [[codes/powershell-get-all-trust-relationships]]
