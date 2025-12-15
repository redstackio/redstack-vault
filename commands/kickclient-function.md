---
id: cmd-sourcemod-kickclient-001
data: 'KickClient(client, full);'
tags:
  - kick
  - sourcemod
type: command
output: Client disconnected with custom popup message parsed as HTML
executor: sourcemod-plugin
platforms:
  - Windows
  - Game
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.829Z'
verified: false
validated: true
submitted: true
---
# kickclient-function

## Command

```bash
# In SourceMod plugin source, called in command handler
KickClient(client, full);
```

## Description

SourceMod API function to kick a client with a custom message string, used in plugins to deliver XSS payloads without length restrictions; called multiple times for reliability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| client | Target player index | Yes |
| full | Message string including payload | Yes |

## Examples

### Basic Usage

```bash
KickClient(client, "<payload>");
```

### Advanced Usage

Repeat in loop:

```bash
for(int i=0; i<5; i++) KickClient(client, full);
```

## Expected Output

Client receives kick popup with parsed HTML message.

## Related

- [[commands/sm-testkick-with-rce-payload]]
