---
id: cmd-wordpress-login-curl
data: >-
  curl --cookie-jar "$cookiejar" --data
  "log=$username&pwd=$password&wp-submit=Log+In&redirect_to=%2f&testcookie=1"
  "$target/wp-login.php" >/dev/null 2>&1
tags:
  - wordpress
  - authentication
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:11.377Z'
verified: false
validated: true
submitted: true
---
# wordpress-login-curl

## Command

```bash
curl --cookie-jar "$cookiejar" --data "log=$username&pwd=$password&wp-submit=Log+In&redirect_to=%2f&testcookie=1" "$target/wp-login.php" >/dev/null 2>&1
```

## Description

This command authenticates to WordPress via POST to wp-login.php, saving session cookies to a jar file for authenticated requests. Used in exploitation chains requiring subscriber access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--cookie-jar "$cookiejar"` | Path to file for storing session cookies | Yes |
| `--data "log=$username"` | Username for login | Yes |
| `--data "pwd=$password"` | Password for login | Yes |
| `--data "wp-submit=Log+In"` | Form submit button value | Yes |
| `--data "redirect_to=%2f"` | Post-login redirect to root | Yes |
| `--data "testcookie=1"` | Enable cookie testing | Yes |
| `$target/wp-login.php` | Target login endpoint URL | Yes |
| `>/dev/null 2>&1` | Suppress output and errors | No |

## Examples

### Basic Usage

```bash
curl --cookie-jar cookies.txt --data "log=user&pwd=pass&wp-submit=Log+In&redirect_to=%2f&testcookie=1" "https://example.com/wp-login.php" >/dev/null 2>&1
```

### Advanced Usage

```bash
cookiejar=$(mktemp) && curl --cookie-jar "$cookiejar" --data "log=subscriber&pwd=secret&wp-submit=Log+In&redirect_to=%2f&testcookie=1" "$target/wp-login.php" >/dev/null 2>&1
```

## Expected Output

No visible output (suppressed); successful login indicated by populated cookie jar with wp-settings-time, wordpress_logged_in cookies.

## Related

- [[Related Procedure|procedures/wordpress-authenticate-subscriber]]
