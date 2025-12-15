---
id: cmd-uuid-001
data: dig TXT _dmarc.paragonie.com
tags:
  - dns
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows (with dig)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.780Z'
verified: false
validated: true
submitted: true
---
# dig-dmarc-query

## Command

```bash
dig TXT _dmarc.paragonie.com
```

## Description

This command uses the dig utility to query DNS TXT records for the _dmarc subdomain, checking for DMARC policy presence. It's useful for verifying email authentication configurations during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| TXT | Specifies TXT record type | Yes |
| _dmarc.paragonie.com | The subdomain to query | Yes |

## Examples

### Basic Usage

```bash
dig TXT _dmarc.paragonie.com
```

### Advanced Usage

```bash
dig +short TXT _dmarc.paragonie.com
```

## Expected Output

If no record: ;; ANSWER SECTION: (empty). If present: _dmarc.paragonie.com. 3600 IN TXT "v=DMARC1; p=reject;".

## Related

- [[Related Procedure: Check-for-DMARC-Record]]
