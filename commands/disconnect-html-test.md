---
data: 'disconnect "<img src=''https://i.imgur.com/IbJKM0M.jpg''>"'
tags:
  - xss
  - testing
type: command
executor: bash
platforms:
  - Windows
id: 60103a7a-9229-4528-996f-a30c01547136
created_at: '2025-12-11T06:10:15.648Z'
updated_at: '2025-12-11T06:10:15.648Z'
verified: false
validated: true
submitted: true
---
# disconnect-html-test

## Command

```bash
disconnect "<img src='https://i.imgur.com/IbJKM0M.jpg'>"
```

## Description

Sends a custom disconnect message with an embedded image tag to test HTML parsing in the disconnect popup within CS:GO console.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `message` | Contains img tag to load external image | Yes |

## Examples

### Basic Usage

```bash
disconnect "<img src='https://i.imgur.com/IbJKM0M.jpg'>"
```

## Expected Output

Displays the image (cat.png) in the disconnect popup after caching.

## Related

- [[procedures/Test-Local-Disconnect-XSS-Injection]]
