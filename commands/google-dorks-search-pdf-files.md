---
id: 7d5157a9-348c-4764-8a05-2fd38ba2c766
name: google-dorks-search-pdf-files
type: command
executor: browser
data: 'site:domain.com filetype:pdf'
output: null
created_at: '2023-04-06T03:56:25.425923+00:00'
updated_at: '2023-04-10T20:25:37.761328+00:00'
platforms:
  - Web
tags:
  - reconnaissance
  - file-discovery
verified: true
validated: true
---

# google-dorks-search-pdf-files

## Command

Enter this query directly into the Google search bar:

```text
site:domain.com filetype:pdf
```

## Description

This Google Dork searches for PDF files hosted on the target domain and its subdomains, useful for finding documents that may leak sensitive information like policies or credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| domain.com | The target domain | Yes |
| filetype:pdf | Restricts to PDF files | Yes |

## Examples

### Basic Usage

```text
site:example.com filetype:pdf
```

Lists all indexed PDFs.

### Advanced Usage

Combine with date range:

```text
site:example.com filetype:pdf after:2023-01-01
```

Focuses on recent PDFs.

## Expected Output

Results with PDF links and snippets, e.g.:

- example.com/docs/policy.pdf - "Internal policy document..."

Download and analyze for intel.

## Related

- [[procedures/Subdomain-Enumeration-with-Google-Dorks]]
- [[commands/google-dorks-search-files-by-extension]]
