---
type: command
executor: bash
data: cat $KRB5CCNAME
output: null
created_at: '2023-04-06T03:56:04.790581+00:00'
updated_at: '2023-04-10T20:26:04.568133+00:00'
platforms:
  - Linux
tags:
  - kerberos
  - verification
verified: true
validated: true
---

# display-krb5ccname-contents

## Command

```bash
cat $KRB5CCNAME
```

## Description

Displays the raw contents of the Kerberos ccache file for verification that the ticket is properly formatted and present.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$KRB5CCNAME` | Environment variable or direct path to ccache | Yes |

## Examples

### Basic Usage

```bash
cat $KRB5CCNAME
```

### Advanced Usage

Direct path: `cat /tmp/ticket.ccache`

## Expected Output

Binary data dump of the ticket; look for readable strings like principal names or timestamps.

## Related

- [[procedures/Forge-and-Use-Golden-Ticket-on-Linux]]
