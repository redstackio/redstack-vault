---
data: waybackurls liberapay.com | grep disavow
tags:
  - reconnaissance
  - url-enumeration
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:30.742Z'
id: 8a5848d5-a0d7-4cdd-bd43-6e7c6fdef065
verified: false
validated: true
submitted: true
---
# waybackurls-grep-disavow

## Command

```bash
waybackurls liberapay.com | grep disavow
```

## Description

This command fetches archived URLs for liberapay.com from the Wayback Machine and filters for those containing the 'disavow' keyword, aiding in the discovery of sensitive endpoints vulnerable to unauthorized access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `liberapay.com` | Target domain to query for archived URLs | Yes |
| `disavow` | Search pattern to filter URLs | Yes |

## Examples

### Basic Usage

```bash
waybackurls liberapay.com | grep disavow
```

### Advanced Usage

```bash
waybackurls liberapay.com | grep -i disavow > disavow_urls.txt
```

## Expected Output

A list of URLs from liberapay.com that include the word 'disavow' in their path or parameters, such as https://liberapay.com/account/disavow/email/.

## Related

- [[Related Procedure]]
