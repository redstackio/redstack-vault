---
data: >-
  jq '.data.user.causes[] | {entityName: .entityName, causeCategory:
  .causeCategory}' response.json
tags:
  - json
  - parse
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:32:02.034Z'
id: e3a8bf91-2d57-4856-8b3c-e66b01cb9f57
verified: false
validated: true
submitted: true
---
# jq-parse-causes

## Command

```bash
jq '.data.user.causes[] | {entityName: .entityName, causeCategory: .causeCategory}' response.json
```

## Description

Parses JSON API response to extract user causes array for analysis in information disclosure scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `.data.user.causes[]` | JSONPath to causes array | Yes |
| `{entityName: .entityName, ...}` | Select fields | Yes |
| `response.json` | Input file | Yes |

## Examples

### Basic Usage

```bash
jq '.data.user.causes[] | .entityName' response.json
```

### Advanced Usage

Filter by category: ```bash
jq '.data.user.causes[] | select(.causeCategory == "EDUCATION")' response.json
```

## Expected Output

Array of objects: {"entityName": "Cause1", "causeCategory": "EDUCATION"}

## Related

- [[Related Procedure]]
