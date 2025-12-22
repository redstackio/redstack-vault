---
data: 'http://google.com:1234567890'
tags:
  - dos
  - post-fix
type: command
output: 'May still cause issues, but longer than 10 digits blocked'
executor: text
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.148Z'
id: d16baac3-241b-49e7-8b32-69c690f2ae9f
verified: false
validated: true
submitted: true
---
# post-fix-10-digit-url

## Command

```text
http://google.com:1234567890
```

## Description

Post-fix test with 10-digit port that may still trigger partial DoS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| port | 10-digit port | Yes |
| domain | google.com | Yes |

## Examples

### Basic Usage

```text
http://google.com:1234567890
```

## Expected Output

Posts successfully but may cause rendering issues.

## Related

- [[Related Procedure]]
