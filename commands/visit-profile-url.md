---
data: 'curl https://username.imgur.com/'
tags:
  - web
  - access
type: command
executor: bash
platforms:
  - Web
id: 82dd20e0-ce44-4c29-a982-e972be5ae292
created_at: '2025-12-14T00:11:25.388Z'
updated_at: '2025-12-14T00:11:25.388Z'
verified: false
validated: true
submitted: true
---
# Visit Profile URL

## Command

```bash
curl https://username.imgur.com/
```

## Description

This command accesses a URL like an Imgur profile to trigger stored content, such as XSS payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | The target profile URL | Yes |

## Examples

### Basic Usage

```bash
curl https://username.imgur.com/
```

### Advanced Usage

```bash
curl -A "Mozilla/5.0" https://username.imgur.com/
```

## Expected Output

HTML response of the profile page, potentially triggering scripts.

## Related

- [[procedures/Trigger-Stored-XSS-on-Imgur-Profile]]
