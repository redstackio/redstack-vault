---
id: 7ed0212e-fd55-461a-a3db-9bd9af74aed6
name: mysql-injection-payload-base64-load-file-php
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:34.767542+00:00'
updated_at: '2023-04-10T20:22:51.271599+00:00'
platforms:
  - Linux
  - Web
tags:
  - mysql-injection
  - file-read
  - payload
  - encoding
validated: true
---

# mysql-injection-payload-base64-load-file-php

## Code

```sql
UNION ALL SELECT TO_base64(LOAD_FILE('/var/www/html/index.php'));
```

## Description

This payload uses SQL injection to load the contents of a PHP file (e.g., index.php) and encode it in base64 using TO_BASE64, preventing issues with special characters or quotes that could break the injection. It combines with UNION ALL to merge results into the application's output.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| '/var/www/html/index.php' | Path to the target file; common for web source code extraction | '/var/www/html/wp-config.php' |

## Usage

Inject as part of a full payload, e.g., id=1 UNION ALL SELECT TO_BASE64(LOAD_FILE('/var/www/html/index.php')). Retrieve the base64 string from the response and decode it offline (e.g., echo 'string' | base64 -d). Ideal for exfiltrating source code without truncation.

## Detection

- Logs revealing TO_BASE64 combined with LOAD_FILE.
- Unusual base64 strings in application responses or database queries.
- File access anomalies on web directories readable by MySQL.
- Injection detection via pattern matching on UNION and base64 functions.

## Related

- [[procedures/mysql-file-content-extraction-via-injection]]
- [[commands/mysql-select-load-file]]
