---
id: uuid-for-grep-command
data: grep -r "AIza\|mapbox" decompiled_dir/res/values/strings.xml
tags:
  - search
  - strings
  - android
type: command
output: >
  decompiled_dir/res/values/strings.xml:<string
  name="google_maps_key">AIzaSyD_example_key</string>
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.118Z'
verified: false
validated: true
submitted: true
---
# grep-search-strings

## Command

```bash
grep -r "AIza\|mapbox" decompiled_dir/res/values/strings.xml
```

## Description

Recursively searches for patterns indicative of API keys (e.g., Google 'AIza' prefix or MapBox tokens) in decompiled XML files to identify hardcoded credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-r` | Recursive search | Yes |
| `"AIza\|mapbox"` | Regex pattern for key prefixes | Yes |
| `decompiled_dir/res/values/strings.xml` | Path to search | Yes |

## Examples

### Basic Usage

```bash
grep -r "AIza" strings.xml
```

### Advanced Usage

```bash
grep -i -r "key\|token" decompiled_dir/
```

## Expected Output

Matching lines from the file, such as XML string elements containing potential keys.

## Related

- [[Related Procedure: Search-for-Hardcoded-API-Keys-in-Decompiled-Files]]
