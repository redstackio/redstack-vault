---
data: 'curl -s "https://hackerone.com/{user-handle}" > profile.html'
tags:
  - recon
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.576Z'
id: b9553f1d-1898-45b7-8250-1e773d2fc68e
verified: false
validated: true
submitted: true
---
# curl-fetch-profile

## Command

```bash
curl -s "https://hackerone.com/{user-handle}" > profile.html
```

## Description

Fetches the HTML content of a HackerOne user profile silently and saves it to a file for offline analysis, useful for inspecting privacy-bypassing elements without browser interference.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, suppresses progress meter | Yes |
| URL | Target profile URL with {user-handle} placeholder | Yes |
| `> profile.html` | Redirect output to file | Yes |

## Examples

### Basic Usage

```bash
curl -s "https://hackerone.com/john_doe" > profile.html
```

### Advanced Usage

```bash
curl -s -H "User-Agent: Mozilla/5.0" "https://hackerone.com/john_doe" > profile.html
```

## Expected Output

A local file 'profile.html' containing the full page source, ready for grep or manual inspection to reveal program memberships.
