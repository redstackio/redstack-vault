---
id: 7601438d-e1e1-4576-b8c5-cee537d4962c
name: browser-irc-join-channel
type: command
executor: browser
data: 'irc://$_IRC_SERVER/$_CHANNEL'
output: null
created_at: '2023-04-06T03:56:17.452167+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Windows
  - Browser
tags:
  - protocol-handler
  - browser-escape
  - irc
verified: true
validated: true
---

# browser-irc-join-channel

## Command

In the browser address bar, enter:

```text
irc://$_IRC_SERVER/$_CHANNEL
```

## Description

This extends the IRC connection to directly join a channel, facilitating communication in an escaped session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_IRC_SERVER | IRC server address | Yes |
| $_CHANNEL | Channel name (e.g., #channel) | Yes |

## Examples

### Basic Usage

```text
irc://irc.example.com/#channel
```

### Advanced Usage

```text
irc://irc.example.com/#secret-channel?key=pass
```

## Expected Output

IRC client joins the channel, displaying join confirmation and messages. Success: Channel chat visible.

## Related

- [[procedures/Browser-Escape-via-Unassociated-Protocols]]
