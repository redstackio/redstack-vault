---
type: command
executor: bash
data: python asnlookup.py --help
output: null
platforms:
  - Linux
tags:
  - reconnaissance
  - tool-setup
verified: true
validated: true
---

# asnlookup-show-help

## Command

```bash
python asnlookup.py --help
```

## Description

Displays the help menu for the asnlookup tool, listing available options, flags, and usage syntax. Use this to verify installation and understand command parameters before running lookups.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--help` or `-h` | Show the help message and exit | No |

## Examples

### Basic Usage

```bash
python asnlookup.py --help
```

This outputs the tool's synopsis, options like `-o` for organization, and version info.

## Expected Output

```
usage: asnlookup.py [-h] -o ORGANIZATION

optional arguments:
  -h, --help            show this help message and exit
  -o ORGANIZATION, --organization ORGANIZATION
                        Organization name to lookup
```

No errors indicate the tool is ready for use.

## Related

- [[procedures/Find-Company-ASN-Using-Asnlookup]]
- [[commands/asnlookup-lookup-asn-for-organization]]
