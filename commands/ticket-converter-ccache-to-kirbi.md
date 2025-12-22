---
type: command
executor: bash
data: python ticket_converter.py $_CCACHE_FILE $_KIRBI_FILE
output: null
created_at: '2023-04-06T03:56:04.791119+00:00'
updated_at: '2023-04-10T20:26:04.568133+00:00'
platforms:
  - Linux
tags:
  - kerberos
  - ticket-conversion
verified: true
validated: true
---

# ticket-converter-ccache-to-kirbi

## Command

```bash
python ticket_converter.py $_CCACHE_FILE $_KIRBI_FILE
```

## Description

Converts a ccache Kerberos ticket file back to kirbi format using ticket_converter.py.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_CCACHE_FILE` | Input ccache file path | Yes |
| `$_KIRBI_FILE` | Output kirbi file path | Yes |

## Examples

### Basic Usage

```bash
python ticket_converter.py velociraptor.ccache velociraptor.kirbi
```

### Advanced Usage

Similar to reverse conversion.

## Expected Output

"Converting ccache => kirbi" and new file created.

## Related

- [[procedures/Forge-and-Use-Golden-Ticket-on-Linux]]
