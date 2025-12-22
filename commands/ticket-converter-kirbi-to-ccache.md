---
type: command
executor: bash
data: python ticket_converter.py $_KIRBI_FILE $_CCACHE_FILE
output: null
created_at: '2023-04-06T03:56:04.791109+00:00'
updated_at: '2023-04-10T20:26:04.568133+00:00'
platforms:
  - Linux
tags:
  - kerberos
  - ticket-conversion
verified: true
validated: true
---

# ticket-converter-kirbi-to-ccache

## Command

```bash
python ticket_converter.py $_KIRBI_FILE $_CCACHE_FILE
```

## Description

Converts a kirbi Kerberos ticket file to ccache format using ticket_converter.py script.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_KIRBI_FILE` | Input kirbi file path | Yes |
| `$_CCACHE_FILE` | Output ccache file path | Yes |

## Examples

### Basic Usage

```bash
python ticket_converter.py velociraptor.kirbi velociraptor.ccache
```

### Advanced Usage

Full paths: `python ticket_converter.py /path/to/input.kirbi /path/to/output.ccache`

## Expected Output

"Converting kirbi => ccache" and new file created.

## Related

- [[procedures/Forge-and-Use-Golden-Ticket-on-Linux]]
