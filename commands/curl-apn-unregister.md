---
data: >-
  curl -X POST https://irccloud.com/apn-unregister -H "Cookie:
  session=1.eaf395c450d6ad52023804d9846b7376" -d
  "device_id=your_device_id&session=1.eaf395c450d6ad52023804d9846b7376"
tags:
  - network
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:39.722Z'
id: 6beb5de4-e387-49df-87c9-04aaa71d2419
verified: false
validated: true
submitted: true
---
# curl-apn-unregister

## Command

```bash
curl -X POST https://irccloud.com/apn-unregister -H "Cookie: session=1.eaf395c450d6ad52023804d9846b7376" -d "device_id=your_device_id&session=1.eaf395c450d6ad52023804d9846b7376"
```

## Description

This command simulates the IRCCloud iOS app's logout request to the /apn-unregister endpoint, testing if the session is invalidated. It sends a POST with device and session parameters, expecting a success response without session destruction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `-H "Cookie: ..."` | Includes the session cookie for authentication | Yes |
| `-d "device_id=...&session=..."` | Payload with device ID and session token | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://irccloud.com/apn-unregister -H "Cookie: session=example_session" -d "device_id=dev123&session=example_session"
```

### Advanced Usage

```bash
curl -X POST https://irccloud.com/apn-unregister -H "Cookie: session=example_session" -H "User-Agent: IRCCloud-iOS/1.0" -d "device_id=dev123&session=example_session" --verbose
```

## Expected Output

HTTP/1.1 200 OK followed by {"_reqid":0,"success":true}. The session cookie remains valid for reuse, indicating the vulnerability.

## Related

- [[Related Procedure: Demonstrate-IRCCloud-Logout-Session-Failure]]
