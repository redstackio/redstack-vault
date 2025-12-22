---
data: >-
  curl -s https://daily.owncloud.com/enterprise-stable8/enterprise/apps/ |
  html2text
tags:
  - reconnaissance
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:56.128Z'
id: 8e45658e-431b-4b79-b1ed-f8b7c9be1354
verified: false
validated: true
submitted: true
---
# curl-directory-listing-access

## Command

```bash
curl -s https://daily.owncloud.com/enterprise-stable8/enterprise/apps/ | html2text
```

## Description

This command uses curl to silently fetch the contents of a web directory listing endpoint and pipes the output to html2text for readable formatting. It is used to discover and enumerate files in a vulnerable directory on a web server like Apache hosting ownCloud, aiding in information disclosure during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, suppresses progress meter | Yes |
| `URL` | Target directory URL (e.g., https://example.com/path/) | Yes |
| `\| html2text` | Converts HTML output to plain text for easier reading | No |

## Examples

### Basic Usage

```bash
curl -s https://daily.owncloud.com/enterprise-stable8/enterprise/apps/
```

### Advanced Usage

```bash
curl -s -O https://daily.owncloud.com/enterprise-stable8/enterprise/apps/readme.md
```

Downloads a specific file from the listing.

## Expected Output

A text-based directory index showing files and folders, e.g.,:

Index of /enterprise/apps/

Name                    Last modified      Size  Description
---------------------- ------------------ ----- ----------
readme.md               2023-01-01 12:00   2k    
app1/                   2023-01-01 12:00   -     

## Related

- [[Related Procedure|procedures/Access-Directory-Listing-for-Information-Disclosure]]
