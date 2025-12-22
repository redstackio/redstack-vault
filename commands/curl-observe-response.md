---
data: 'curl http://proxy.target.com/ -v'
tags:
  - http
  - monitoring
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 72f7a45c-236b-400b-a9a9-51555a892d55
created_at: '2025-12-13T09:01:22.536Z'
updated_at: '2025-12-13T09:01:22.536Z'
verified: false
validated: true
submitted: true
---
# curl-observe-response

## Command

```bash
curl http://proxy.target.com/ -v
```

## Description

This command uses curl in verbose mode to observe HTTP responses and detect signs of request desynchronization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output | Yes |

## Examples

### Basic Usage

```bash
curl http://target.com/ -v
```

### Advanced Usage

```bash
curl http://target.com/ -v -H "Custom-Header: value"
```

## Expected Output

Verbose output showing request and response headers, potentially indicating smuggling.

## Related

- [[procedures/Observe-Request-Desynchronization-in-Node.js]]
