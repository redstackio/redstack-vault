---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
data: open _build/html/index.html
tags:
  - verification
  - browser
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T03:16:31.327Z'
verified: false
validated: true
submitted: true
---
# open-html-file

## Command

```bash
open _build/html/index.html
```

## Description

Opens the generated documentation HTML file in the default web browser to verify XSS payload execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `_build/html/index.html` | Path to the output HTML file | Yes |

## Examples

### Basic Usage

```bash
open _build/html/index.html  # macOS/Linux with xdg-open
```

### Advanced Usage

```bash
start _build/html/index.html  # Windows
```

## Expected Output

Browser launches and loads the page; injected script executes (e.g., alert dialog appears).

## Related

- [[Related Procedure: Demonstrate-XSS-in-fabric-sdk-py-Doc-Generation]]
