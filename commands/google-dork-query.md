---
data: >-
  echo "site:██████████&filter=0" | xargs -I {} curl -s
  "https://www.google.com/search?q={}"
tags:
  - reconnaissance
  - google-dorking
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 860ba33b-1b36-487b-962c-f9c15f58098b
created_at: '2025-12-13T09:01:26.431Z'
updated_at: '2025-12-13T09:01:26.431Z'
verified: false
validated: true
submitted: true
---
# Google Dork Query

## Command

```bash
echo "site:██████████&filter=0" | xargs -I {} curl -s "https://www.google.com/search?q={}"
```

## Description

This command constructs a Google dork query to search for all indexed pages on a specific site without filters, useful for discovering leaked information like internal URLs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `site:DOMAIN` | Specifies the domain to search | Yes |
| `&filter=0` | Disables result filtering | No |

## Examples

### Basic Usage

```bash
echo "site:example.com&filter=0" | xargs -I {} curl -s "https://www.google.com/search?q={}"
```

### Advanced Usage

```bash
echo "site:example.com inurl:people&filter=0" | xargs -I {} curl -s "https://www.google.com/search?q={}"
```

## Expected Output

HTML output of Google search results page containing links to indexed URLs.

## Related

- [[procedures/Perform-Google-Search-for-Indexed-SSO-URLs]]
- [[tools/Google-Search]]
