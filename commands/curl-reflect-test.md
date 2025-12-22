---
data: 'curl -s "https://█████?██████=test123" | grep -i "test123"'
tags:
  - web-testing
  - xss
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-05T12:00:00Z'
updated_at: '2025-12-14T03:16:02.395Z'
id: 330a2920-8b53-4f82-8a04-eef1bafcd72f
verified: false
validated: true
submitted: true
---
# curl-reflect-test

## Command

```bash
curl -s "https://█████?██████=test123" | grep -i "test123"
```

## Description

This command tests for input reflection in a web parameter by sending a benign string via curl and grepping the response for matches, indicating unsanitized output suitable for XSS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode to suppress progress meter | Yes |
| URL with parameter | Target endpoint with test value | Yes |
| `grep -i` | Case-insensitive search for the test string | Yes |

## Examples

### Basic Usage

```bash
curl -s "https://example.com?param=test" | grep -i "test"
```

### Advanced Usage

```bash
curl -s -H "User-Agent: Mozilla/5.0" "https://█████?██████=test123" | grep -i "test123" | head -5
```

## Expected Output

If reflection occurs, output like: <input value="test123"> or similar unencoded string in HTML.

## Related

- [[Related Procedure: Identify-Reflected-XSS-Vulnerable-Parameter]]
