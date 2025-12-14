---
id: cmd-uuid-002
data: >-
  curl -s https://ip-ranges.amazonaws.com/ip-ranges.json | jq '.prefixes[] |
  select(.ip_prefix=="$1")'
tags:
  - aws
  - ip-validation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:31.183Z'
verified: false
validated: true
submitted: true
---
# curl-aws-ip-check

## Command

```bash
curl -s https://ip-ranges.amazonaws.com/ip-ranges.json | jq '.prefixes[] | select(.ip_prefix=="54.68.0.0/15")'
```

## Description

Fetches AWS IP ranges and filters for a specific prefix to validate if an IP belongs to AWS and its region, aiding in analysis of dangling cloud resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent curl | No |
| `jq filter` | JSON query for prefix | Yes |
| `$1` | IP prefix to check | Yes |

## Examples

### Basic Usage

```bash
curl -s https://ip-ranges.amazonaws.com/ip-ranges.json | jq '.prefixes[] | select(.ip_prefix=="54.68.0.0/15")'
```

### Advanced Usage

```bash
curl -s https://ip-ranges.amazonaws.com/ip-ranges.json | jq '.prefixes[] | select(.region=="us-west-2")'
```

## Expected Output

JSON object with region us-west-2, confirming AWS ownership.

## Related

- [[Related Procedure: Analyze-Dangling-DNS-Records-for-Takeover-Potential]]
