---
data: curl -V
tags:
  - version-check
type: command
executor: bash
platforms:
  - Linux
  - Windows
id: 780657de-8b12-4472-91b7-84a705aaa798
created_at: '2025-12-13T09:01:21.764Z'
updated_at: '2025-12-13T09:01:21.764Z'
verified: false
validated: true
submitted: true
---
# curl-version-check

## Command

```bash
curl -V
```

## Description

Checks the installed version of cURL to verify if it's affected by the vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-V` | Display version information | Yes |

## Examples

### Basic Usage

```bash
curl -V
```

## Expected Output

cURL version information, including version number, protocols, and features.

## Related

- [[procedures/Create-Test-Request-with-Conflicting-Headers]]
