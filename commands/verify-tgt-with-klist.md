---
type: command
executor: bash
data: klist
tags:
  - kerberos
  - verification
platforms:
  - Linux
verified: true
validated: true
---

# verify-tgt-with-klist

## Command

```bash
klist
```

## Description

This command lists cached Kerberos tickets, allowing verification of TGT validity, expiration, and associated principals.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Displays default ticket cache | N/A |

## Examples

### Basic Usage

```bash
klist
```

### Advanced Usage

```bash
klist -c /tmp/krb5cc_1000
```

## Expected Output

Ticket cache: FILE:/tmp/krb5cc_1000
Default principal: tgwynn@LAB.ROPNOP.COM

Valid starting     Expires            Principal
10/01/23 12:00:00  10/02/23 12:00:00  krbtgt/LAB.ROPNOP.COM@LAB.ROPNOP.COM

Kerberos 5 Ticket..., kvno 5

Shows active TGT details.

## Related

- [[procedures/OverPass-the-Hash-with-Impacket]]
- [[commands/obtain-tgt-with-kinit]]
