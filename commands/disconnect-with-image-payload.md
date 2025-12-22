---
id: cmd-csgo-disconnect-img-001
data: 'disconnect "<img src=''https://i.imgur.com/IbJKM0M.jpg''>"'
tags:
  - xss
  - test
type: command
output: Cat image appears in disconnect popup after running twice for cache bypass
executor: csgo-console
platforms:
  - Windows
  - Game
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.838Z'
verified: false
validated: true
submitted: true
---
# disconnect-with-image-payload

## Command

```bash
# In CS:GO console
disconnect "<img src='https://i.imgur.com/IbJKM0M.jpg'>"
```

## Description

Sends a disconnect message with an HTML image payload to test XSS in the popup_generic.xml, confirming raw HTML parsing by loading an external image.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| payload | HTML string like <img src='url'> | Yes |

## Examples

### Basic Usage

```bash
# In CS:GO console
disconnect "<img src='https://i.imgur.com/IbJKM0M.jpg'>"
```

### Advanced Usage

Run twice to bypass cache:

```bash
disconnect "<img src='https://i.imgur.com/IbJKM0M.jpg'>"
disconnect "<img src='https://i.imgur.com/IbJKM0M.jpg'>"
```

## Expected Output

Disconnect popup displays the cat image from Imgur, verifying XSS.

## Related

- [[commands/sm-testkick-with-rce-payload]]
