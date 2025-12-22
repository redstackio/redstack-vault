---
data: >-
  curl "http://www.urbandictionary.com/define.php?term=$TERM" | grep -i
  "normalized"
tags:
  - web
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:47.453Z'
id: c15bdfde-94ac-4a9c-8d2c-8dc1f96c3826
verified: false
validated: true
submitted: true
---
# curl-fetch-urbandictionary

## Command

```bash
curl "http://www.urbandictionary.com/define.php?term=$TERM" | grep -i "normalized"
```

## Description

Fetches the Urban Dictionary define page for a given term and greps for the reflected 'normalized' property to inspect for XSS potential. Use $TERM as a variable for the search term.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$TERM` | The search term to test (e.g., 'test') | Yes |

## Examples

### Basic Usage

```bash
TERM=test; curl "http://www.urbandictionary.com/define.php?term=$TERM" | grep -i "normalized"
```

### Advanced Usage

```bash
TERM=lol; curl "http://www.urbandictionary.com/define.php?term=$TERM" -s | grep -A5 -B5 "normalized"
```

## Expected Output

Lines showing JavaScript like: Page.globals.normalized = "test";

## Related

- [[Related Procedure]]
