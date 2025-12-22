---
id: a6ceffe7-f643-4643-9469-b2e7be8c961d
name: google-dorks-search-files-by-extension
type: command
executor: browser
data: 'site:domain.com ext:php,asp,aspx,jsp,jspa,txt,swf'
output: null
created_at: '2023-04-06T03:56:25.426110+00:00'
updated_at: '2023-04-10T20:25:37.761328+00:00'
platforms:
  - Web
tags:
  - reconnaissance
  - file-discovery
verified: true
validated: true
---

# google-dorks-search-files-by-extension

## Command

Enter this query directly into the Google search bar:

```text
site:domain.com ext:php,asp,aspx,jsp,jspa,txt,swf
```

## Description

This Google Dork searches for files with web scripting or text extensions on the target domain, potentially exposing source code, configs, or backups.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| domain.com | The target domain | Yes |
| ext:php,asp,... | Comma-separated extensions | Yes |

## Examples

### Basic Usage

```text
site:example.com ext:php,txt
```

Targets PHP and TXT files.

### Advanced Usage

With filetype:

```text
site:example.com ext:php filetype:txt
```

Refines to text-based PHP.

## Expected Output

Links to files, e.g.:

- example.com/config.php
- backup.txt

Attempt direct access.

## Related

- [[procedures/Subdomain-Enumeration-with-Google-Dorks]]
- [[commands/google-dorks-search-pdf-files]]
