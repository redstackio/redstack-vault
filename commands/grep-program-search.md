---
data: grep -i "program\|membership\|visibility" profile.html
tags:
  - recon
  - parsing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.572Z'
id: e31d5bd0-a9ba-4756-8c4e-55d399df0aa9
verified: false
validated: true
submitted: true
---
# grep-program-search

## Command

```bash
grep -i "program\|membership\|visibility" profile.html
```

## Description

Searches HTML output for keywords related to programs and visibility, helping identify disclosed memberships in a case-insensitive manner.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Ignore case | Yes |
| Pattern | Regex for program-related terms | Yes |
| `profile.html` | Input file | Yes |

## Examples

### Basic Usage

```bash
grep -i "program" profile.html
```

### Advanced Usage

```bash
grep -i -n "program\|membership" profile.html
```

## Expected Output

Lines from the file matching the pattern, such as '<div class="program-membership">Private Program X</div>', indicating leaked data.
