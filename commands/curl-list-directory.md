---
data: 'curl https://sdrc.starbucks.com/attachments/ -v'
tags:
  - recon
  - disclosure
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: cd65492a-7a44-4bcc-9778-72a324d1188b
created_at: '2025-12-14T17:25:18.331Z'
updated_at: '2025-12-14T17:25:18.331Z'
verified: false
validated: true
submitted: true
---
# curl-list-directory

## Command

```bash
curl https://sdrc.starbucks.com/attachments/ -v
```

## Description

This command uses curl to access and list contents of an unsecured web directory, useful for identifying exposed files in information disclosure scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `URL` | Target directory path | Yes |
| `-v` | Verbose mode for headers and status | No |
| `-o filename` | Output file for downloads | No |

## Examples

### Basic Usage

```bash
curl https://sdrc.starbucks.com/attachments/ -v
```

### Advanced Usage

```bash
curl https://sdrc.starbucks.com/attachments/sensitive.pdf -o downloaded.pdf
```

## Expected Output

Directory index HTML or plain text listing files (e.g., Index of /attachments/ with file names), with HTTP 200 status and no auth challenge.

## Related

- [[Related Procedure: Exploit-Unsecured-Attachment-Directory-for-Information-Disclosure]]
