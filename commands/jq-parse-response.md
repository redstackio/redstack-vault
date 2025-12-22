---
data: 'jq ''.entities[] | .name'''
tags:
  - parsing
  - json
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 486eed67-c39a-4ad6-acb7-7732dc4ea18c
created_at: '2025-12-13T09:01:26.530Z'
updated_at: '2025-12-13T09:01:26.530Z'
verified: false
validated: true
submitted: true
---
# JQ Parse Response

## Command

```bash
jq '.entities[] | .name'
```

## Description

This command uses jq to parse JSON responses, extracting specific fields like entity names from SAML metadata.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `'.entities[] | .name'` | JQ filter expression | Yes |

## Examples

### Basic Usage

```bash
echo '{"entities": [{"name": "program1"}]}' | jq '.entities[] | .name'
```

### Advanced Usage

```bash
curl -s https://example.com | jq '.status == "private"'
```

## Expected Output

Extracted values, e.g., "program1".

## Related

- [[procedures/Exploit-SAML-Enumeration-Vulnerability]]
- [[procedures/Identify-Target-HackerOne-Programs]]
