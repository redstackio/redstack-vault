---
data: 'curl -s http://target.com/wp-content/debug.log | head -50'
tags:
  - reconnaissance
  - information-disclosure
type: command
output: Log file contents with server paths visible in error messages
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 7ab3e54c-78be-40dc-bdd6-dafd3c4259e4
created_at: '2025-12-14T17:26:26.853Z'
updated_at: '2025-12-14T17:26:26.853Z'
verified: false
validated: true
submitted: true
---
# curl-access-debug-log

## Command

```bash
curl -s http://target.com/wp-content/debug.log | head -50
```

## Description

This command uses curl to silently fetch the first 50 lines of a WordPress debug.log file from a target URL, useful for disclosing server paths in reconnaissance scenarios where the file is publicly exposed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, suppresses progress meter and error messages | Yes |
| `http://target.com/wp-content/debug.log` | URL of the exposed debug.log file; replace target.com with the actual domain | Yes |
| `\| head -50` | Pipes output to head to limit to 50 lines for quick review | No |

## Examples

### Basic Usage

```bash
curl -s http://wonderdynamics.com/wp-content/debug.log
```

Fetches the entire debug.log file without limiting lines.

### Advanced Usage

```bash
curl -s http://target.com/wp-content/debug.log | grep -i 'path' \| head -10
```

Filters for path-related entries in the log.

## Expected Output

HTTP response body containing log entries, e.g.:
```
[01-Oct-2023 12:00:00 UTC] PHP Warning: include(/var/www/html/wp-content/plugins/plugin/file.php): Failed opening in /var/www/html/wp-includes/functions.php on line 456
```
This reveals the server path /var/www/html/. If the file is protected, expect 403 Forbidden or 404 Not Found.

## Related

- [[Related Procedure: Access-Exposed-WordPress-Debug-Log]]
