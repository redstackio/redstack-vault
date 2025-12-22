---
id: 99854bf0-860c-4fbf-ba46-c1ba6d7eed1d
name: browser-enter-irc-url
type: command
executor: browser
data: 'irc://$_IRC_SERVER'
output: null
created_at: '2023-04-06T03:56:17.452056+00:00'
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

# browser-enter-irc-url

## Command

In the browser address bar, enter:

```text
irc://$_IRC_SERVER
```

## Description

This invokes the IRC protocol handler to connect to an IRC server, launching an external client for potential C2 or data exfil.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_IRC_SERVER | IRC server address (e.g., irc.server.com) | Yes |

## Examples

### Basic Usage

```text
irc://irc.example.com
```

### Advanced Usage

```text
irc://irc.example.com:6667
```

## Expected Output

IRC client launches and connects, showing a connection message. Success: Prompt for nickname/channel.

## Related

- [[procedures/Browser-Escape-via-Unassociated-Protocols]]
