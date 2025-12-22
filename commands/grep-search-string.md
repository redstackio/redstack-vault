---
data: grep 'getGrabUser'
tags:
  - search
  - recon
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: f462a011-9fb4-4be0-a388-05820e5f8b76
created_at: '2025-12-11T06:10:22.693Z'
updated_at: '2025-12-11T06:10:22.693Z'
verified: false
validated: true
submitted: true
---
# grep-search-string

## Command

```bash
grep 'getGrabUser'
```

## Description

Searches for the string 'getGrabUser' in text content, such as downloaded web pages, to identify exposed JavaScript methods in web-based investigations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `'getGrabUser'` | The search string to find | Yes |
| file/input | Optional file or piped input | No |

## Examples

### Basic Usage

```bash
grep 'getGrabUser' page_content.txt
```

### Advanced Usage

```bash
curl https://help.grab.com/ | grep 'getGrabUser'
```

## Expected Output

JavaScript code snippets containing 'getGrabUser', such as initGrabUser or setGrabUser functions.

## Related

- [[procedures/Exploit-iOS-Version-via-Web-Content-Search]]
