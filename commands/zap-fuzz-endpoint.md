---
id: cmd-zap-fuzz-001
data: >-
  # In OWASP ZAP: Right-click endpoint > Attack > Fuzzer > Configure payloads
  for 10,000 runs on 'mobiles' field
tags:
  - fuzzing
  - web-scanner
type: command
output: null
executor: gui
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:39.591Z'
verified: false
validated: true
submitted: true
---
# zap-fuzz-endpoint

## Command

```bash
# GUI-based in OWASP ZAP
# 1. Proxy traffic and capture POST /driver_invitations
# 2. History tab > Right-click > Attack > Fuzzer
# 3. Add payload: Repeat phone number 10,000 times in JSON 'mobiles'
# 4. Start Fuzzer with 5-10 threads
```

## Description

Configures and runs fuzzing in OWASP ZAP to send high-volume requests to a web endpoint, ideal for discovering rate limit weaknesses in APIs like Uber's referrals.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Payload Position | JSON body field (e.g., 'mobiles') | Yes |
| Number of Runs | Total requests (e.g., 10000) | Yes |
| Threads | Parallelism (5-10) | No |
| Payload Type | Fixed string repeat (phone number) | Yes |

## Examples

### Basic Usage

```bash
# ZAP GUI: Fuzzer > Start with default settings
```

### Advanced Usage

```bash
# Custom payload file with repeated JSON snippets
# Load from file for varied fuzzing
```

## Expected Output

ZAP fuzz results table showing 10,000 entries with HTTP 200 codes, no errors.

## Related

- [[commands/send-uber-invitation-post]]
- [[procedures/Queue-SMS-Invitations-via-Endpoint-Fuzzing]]
