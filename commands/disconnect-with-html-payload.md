---
data: 'disconnect "<img src=''https://i.imgur.com/IbJKM0M.jpg''>"'
tags:
  - csgo
  - xss
type: command
executor: bash
platforms:
  - Windows
  - 'CS:GO'
id: a945e776-dd73-4c55-b5ef-db23d7b914e4
created_at: '2025-12-14T00:11:25.214Z'
updated_at: '2025-12-14T00:11:25.214Z'
verified: false
validated: true
submitted: true
---
# Disconnect with HTML Payload

## Command

```bash
disconnect "<img src='https://i.imgur.com/IbJKM0M.jpg'>"
```

## Description

Sends a custom disconnect message with an embedded image to test HTML parsing in the disconnect popup within CS:GO client.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `disconnect message` | Contains img tag to load external image | Yes |

## Examples

### Basic Usage

```bash
disconnect "<img src='https://i.imgur.com/IbJKM0M.jpg'>"
```

## Expected Output

Displays the image (cat.png) in the disconnect popup after caching.

## Related

- [[procedures/Test-Local-HTML-Injection-in-Disconnect-Messages]]
