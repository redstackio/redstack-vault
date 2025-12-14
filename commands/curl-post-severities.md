---
id: cmd-curl-severities
data: >-
  curl -X POST https://hackerone.com/ed/severities -H "Content-Type:
  application/json" -H "X-CSRF-Token: token" -H "Cookie: session=your-cookie" -d
  '{"rating":null,"with_metrics":true,"structured_scope_id":null,"metrics":{"attack_vector":"adjacent","attack_complexity":"low","privileges_required":"none","user_interaction":"required","scope":"unchanged","integrity":"low","confidentiality":"low","availability":"low"}}'
tags:
  - testing
  - idor
  - web
type: command
output: 'HTTP/1.1 200 OK {"attack_vector":"adjacent",..."score":5.5,"rating":"medium"}'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:49.871Z'
verified: false
validated: true
submitted: true
---
# curl-post-severities

## Command

```bash
curl -X POST https://hackerone.com/ed/severities -H "Content-Type: application/json" -H "X-CSRF-Token: token" -H "Cookie: session=your-cookie" -d '{"rating":null,"with_metrics":true,"structured_scope_id":null,"metrics":{"attack_vector":"adjacent","attack_complexity":"low","privileges_required":"none","user_interaction":"required","scope":"unchanged","integrity":"low","confidentiality":"low","availability":"low"}}'
```

## Description

This command tests the /severities endpoint for potential IDOR by submitting severity metrics during report creation; it was found to be intended behavior, not exploitable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP POST method | Yes |
| `https://hackerone.com/ed/severities` | Endpoint for program 'ed' severity calculation | Yes |
| `-H "Content-Type: application/json"` | JSON payload format | Yes |
| `-H "X-CSRF-Token: token"` | CSRF protection (present here, unlike apply endpoint) | Yes |
| `-d '{...}'` | JSON body with CVSS-like metrics | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://hackerone.com/ed/severities -H "Content-Type: application/json" -d '{"metrics":{"attack_vector":"network"}}'
```

### Advanced Usage

Include full headers as in data for authenticated testing.

## Expected Output

JSON response with calculated severity, e.g., {"score":5.5,"rating":"medium"}. No unauthorized access.

## Related

- [[Related Procedure: None - Debunked IDOR Test]]
