---
id: cmd-uuid-001
data: 'curl https://_domainkey.launchpad.37signals.com/.htaccess -o htaccess.txt'
tags:
  - reconnaissance
  - information-disclosure
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:18.096Z'
verified: false
validated: true
submitted: true
---
# curl-retrieve-htaccess

## Command

```bash
curl https://_domainkey.launchpad.37signals.com/.htaccess -o htaccess.txt
```

## Description

This command uses curl to download the publicly accessible .htaccess file from a specified subdomain, revealing Apache configuration details for reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target endpoint for .htaccess | Yes |
| -o | Output file name | Yes |

## Examples

### Basic Usage

```bash
curl https://example.com/.htaccess -o config.txt
```

### Advanced Usage

```bash
curl -v https://_domainkey.launchpad.37signals.com/.htaccess -o htaccess.txt
```

## Expected Output

A saved text file (htaccess.txt) containing Apache directives, such as Options +ExecCGI and Rewrite rules, without HTTP errors.

## Related

- [[Related Procedure: Retrieve-Public-Htaccess-Configuration-File]]
