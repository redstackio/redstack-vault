---
id: proc-follow-redirect-internal-access-187520
tags:
  - ssrf
  - basic-auth
  - internal
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/simulate-ssrf-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:31:30.695Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Credentials In Files]]'
---
# Follow-Redirect-to-Access-Internal-Endpoint-with-Basic-Auth

## Summary

This procedure exploits the SSRF by having WordPress follow the redirect and send a full HTTP request to the private endpoint, including injected basic auth headers, potentially compromising internal services.

## Description

The WordPress scraper blindly follows the 302, issuing a GET to the private URL with preserved headers like Authorization (from basic auth in Location). This bypasses filters and allows access to services on ports like 12345 or 11211 (Memcached). User-Agent identifies it as Press This. Expected outcome: Internal data access or service manipulation.

## Requirements

1. Successful redirect from previous step
2. Internal network monitoring or service logs
3. Target internal service details (IP, port, expected creds)

## Defense

Defensive measures and detection strategies:

- Firewall rules blocking web server outbound to private IPs
- Validate all outgoing requests from app servers
- Alert on User-Agent matching Press This in internal logs

## Objectives

1. Achieve SSRF to arbitrary private resources
2. Inject credentials for unauthorized access
3. Exfiltrate or interact with internal data

## Instructions

### Step 1: Simulate the SSRF Request

**Context**: Replicate the request WordPress sends post-redirect.

**Command** ([[commands/simulate-ssrf-request]]):
```bash
curl -v -H "Host: 192.168.0.1:12345" -H "Authorization: Basic YWRtaW46YWRtaW4=" -H "User-Agent: Press This (WordPress/4.7-RC1)" -H "Accept: */*" http://192.168.0.1:12345/
```

> Mimics the exact request; use from WordPress server context. Expected output: Response from internal service, e.g., 200 OK with data.

### Step 2: Monitor Internal Impact

**Context**: Check logs on target internal service for the incoming request.

**Command** ([[commands/monitor-internal-logs]]):
```bash
tail -f /var/log/internal-service/access.log | grep "Press This"
```

> Looks for the SSRF hit. Expected output: Log entry with Authorization header and GET /.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Credentials In Files]] Unsecured Credentials: Credentials in Files (adapted for header injection)

### Sub-Techniques

- None

## Commands Used

- [[commands/simulate-ssrf-request]]
- [[commands/monitor-internal-logs]]

## Tools Used

- None

## Tags

- [[ssrf]]
- [[basic-auth]]
- [[internal]]
