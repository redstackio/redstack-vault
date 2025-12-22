---
type: code
language: sql
verified: true
tags:
  - mysql-injection
  - blind-sqli
  - like-payload
platforms:
  - Web
validated: true
---

# MySQL-LIKE-Customer-Code-Query-Payload

## Code

```sql
SELECT cust_code FROM customer WHERE cust_name LIKE 'k__l';
```

## Description

This SQL code snippet is a payload for blind SQL injection attacks targeting customer databases. It queries the 'cust_code' from the 'customer' table where the 'cust_name' matches a specific pattern using the LIKE operator. The pattern 'k__l' matches names starting with 'k', followed by any two characters, and ending with 'l'. In a blind injection context, this is embedded in a conditional subquery to infer matches without direct output, enabling data exfiltration one pattern at a time.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'k__l' | LIKE pattern for customer name matching (wildcards: _ for single char, % for multiple) | 'k__l' (matches 'kail', 'keel'), 'a%' (names starting with 'a') |

## Usage

Inject this as a subquery in a vulnerable web parameter, e.g., `search=pattern' AND (SELECT cust_code FROM customer WHERE cust_name LIKE 'k__l') IS NOT NULL --`. Use in boolean blind SQLi by observing response changes or time-based delays. Ideal for targeted extraction when partial name knowledge is available, such as from reconnaissance.

## Detection

- Monitor application logs for LIKE patterns with wildcards in query parameters.
- WAF rules to flag subqueries or conditional SQL in inputs.
- Database audit logs showing unusual SELECTs on customer tables with LIKE filters.
- Anomalous response times or error rates from iterative requests.

## Related

- [[procedures/MySQL-Blind-SQL-Injection-for-Customer-Code-Extraction-Using-LIKE]]
