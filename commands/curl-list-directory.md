---
id: cmd-curl-list-directory
data: 'curl -s http://www.mtn.co.sz/wp-content/uploads/ | html2text -nobs'
tags:
  - recon
  - web
  - directory-listing
type: command
output: |
  Index of /wp-content/uploads/
  Name                    Last modified      Size  Description
  <hr>
  2019/                   01-Jan-2019 00:00    -
  2020/                   01-Jan-2020 00:00    -
  image.jpg               15-Mar-2020 10:30   2.5M
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:10.068Z'
verified: false
validated: true
submitted: true
---
# curl-list-directory

## Command

```bash
curl -s http://www.mtn.co.sz/wp-content/uploads/ | html2text -nobs
```

## Description

This command uses curl to silently fetch the contents of a web directory with enabled listing and pipes the HTML output to html2text for a clean, readable text representation of the file and folder list. It is useful for enumerating exposed directories in reconnaissance phases without needing a graphical browser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, suppresses progress meter | Yes |
| `URL` | Target directory URL (e.g., http://target.com/wp-content/uploads/) | Yes |
| `html2text -nobs` | Converts HTML to text, ignoring body tags and styles | Yes (if piping) |

## Examples

### Basic Usage

```bash
curl -s http://target.com/wp-content/uploads/ | html2text -nobs
```

### Advanced Usage

```bash
curl -s -L http://target.com/wp-content/uploads/2020/ | html2text -nobs > listing.txt
```

This follows redirects (-L) and saves the output to a file.

## Expected Output

A text-based index listing directories and files with names, last modified dates, sizes, and descriptions, indicating successful directory browsing (e.g., no error like 403 Forbidden).

## Related

- [[commands/curl-download-file]]
- [[procedures/Access-WordPress-Uploads-Directory-Listing]]
