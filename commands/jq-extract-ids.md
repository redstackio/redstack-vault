---
data: 'jq ''.data[] | .id'' api_response.json'
tags:
  - json
  - parsing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.552Z'
id: ba97fd66-adda-46fd-b24a-d545921b5ceb
verified: false
validated: true
submitted: true
---
# jq-extract-ids

## Command

```bash
jq '.data[] | .id' api_response.json
```

## Description

Parses JSON API response to extract ID fields from data arrays, isolating leaked identifiers for IDOR use.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Query | JMESPath-like filter for .id | Yes |
| `api_response.json` | Input JSON file | Yes |

## Examples

### Basic Usage

```bash
jq '.data[] | .id' api_response.json
```

### Advanced Usage

```bash
jq '.data[] | select(.type == "report") | .id' api_response.json
```

## Expected Output

List of IDs, e.g., 12345
67890, ready for insertion into API calls.
