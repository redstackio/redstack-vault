---
id: cmd-1066410-003
data: grep -i 'lnk.clario.co' main.js
tags:
  - recon
  - endpoint
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.476Z'
verified: false
validated: true
submitted: true
---
# grep-endpoint

## Command

```bash
grep -i 'lnk.clario.co' main.js
```

## Description

Locates URL shortening endpoint references in JavaScript code.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Case-insensitive | Yes |
| `'lnk.clario.co'` | Endpoint pattern | Yes |
| `main.js` | File to search | Yes |

## Examples

### Basic Usage

```bash
grep -i 'lnk.clario.co' main.js
```

### Advanced Usage

```bash
grep -i -A 5 'lnk.clario.co' main.js
```

## Expected Output

Code snippets showing endpoint like https://lnk.clario.co/?link=[URLHERE].

## Related

- [[commands/grep-api-key]]
- [[procedures/Identify-URL-Shortening-Endpoint]]
