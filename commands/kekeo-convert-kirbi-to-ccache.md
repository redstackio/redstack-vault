---
type: command
executor: bash
data: 'misc::convert ccache $_KIRBI_FILE'
output: null
created_at: '2023-04-06T03:56:04.790403+00:00'
updated_at: '2023-04-10T20:26:04.568133+00:00'
platforms:
  - Linux
tags:
  - kerberos
  - ticket-conversion
verified: true
validated: true
---

# kekeo-convert-kirbi-to-ccache

## Command

```bash
misc::convert ccache $_KIRBI_FILE
```

## Description

This Kekeo command converts a Windows kirbi-format Kerberos ticket to Linux-compatible ccache format, enabling use on non-Windows systems.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `ccache` | Specifies output format as ccache | Yes |
| `$_KIRBI_FILE` | Path to input kirbi file (e.g., ticket.kirbi) | Yes |

## Examples

### Basic Usage

```bash
misc::convert ccache admin.kirbi
```

### Advanced Usage

Run within Kekeo interactive mode after launching kekeo.exe.

## Expected Output

Conversion success message, e.g., "CCache exported to admin.ccache". No errors if file is valid.

## Related

- [[procedures/Forge-and-Use-Golden-Ticket-on-Linux]]
- [[tools/kekeo]]
