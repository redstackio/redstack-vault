---
data: 'cat attack5.txt | curl telnet://localhost:8082/ --output -'
tags:
  - exploit
type: command
executor: bash
platforms:
  - Linux
id: cf0ee827-82c7-4735-8bee-42f0335f7e6e
created_at: '2025-12-13T09:01:22.323Z'
updated_at: '2025-12-13T09:01:22.323Z'
verified: false
validated: true
submitted: true
---
# Cat Pipe to Curl

## Command

```bash
cat attack5.txt | curl telnet://localhost:8082/ --output -
```

## Description

Sends the contents of attack5.txt to the server via curl using telnet protocol.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--output -` | Output to stdout | Yes |
| `telnet://localhost:8082/` | Target URL | Yes |

## Examples

### Basic Usage

```bash
cat attack5.txt | curl telnet://localhost:8082/ --output -
```

## Expected Output

Two HTTP responses: one for original and one for smuggled request.

## Related

- [[procedures/Execute-Request-Smuggling-Attack]]
