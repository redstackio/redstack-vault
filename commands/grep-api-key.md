---
id: cmd-1066410-002
data: grep -i 'AIzaSy' main.js
tags:
  - recon
  - search
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.479Z'
verified: false
validated: true
submitted: true
---
# grep-api-key

## Command

```bash
grep -i 'AIzaSy' main.js
```

## Description

Searches a JavaScript file for Google API keys by pattern matching the common prefix.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Case-insensitive search | Yes |
| `'AIzaSy'` | Search pattern | Yes |
| `main.js` | Input file | Yes |

## Examples

### Basic Usage

```bash
grep -i 'AIzaSy' main.js
```

### Advanced Usage

```bash
grep -i -n 'AIzaSy' main.js
```

## Expected Output

Lines containing API keys, e.g., AIzaSyAw-SpLHVTIP3IFEIkckCuEmIhnUrY9OrQ.

## Related

- [[commands/curl-download-js]]
- [[procedures/Discover-Leaked-Firebase-API-Key]]
