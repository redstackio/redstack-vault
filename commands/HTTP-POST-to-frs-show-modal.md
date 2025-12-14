---
id: cmd-uuid-3
data: |-
  POST /wp-admin/admin-ajax.php?action=frs_show_modal HTTP/1.1

  post_id=zzz
tags:
  - csrf
  - test
  - http
type: command
output: |-
  HTTP/1.1 200 OK

  0 (for non-logged-in or post-plugin removal)
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:15.538Z'
verified: false
validated: true
submitted: true
---
# HTTP POST to frs_show_modal

## Command

```http
POST /wp-admin/admin-ajax.php?action=frs_show_modal HTTP/1.1

post_id=zzz
```

## Description

HTTP request to test the frs_show_modal endpoint, verifying CSRF or plugin status.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| action | frs_show_modal | Yes |
| post_id | Test value like zzz | Yes |

## Examples

### Basic Usage

Use curl: curl -X POST -d 'post_id=zzz&action=frs_show_modal' https://target/wp-admin/admin-ajax.php

### Advanced Usage

With cookies for auth simulation.

## Expected Output

200 OK with response body indicating access or denial.

## Related

- [[Related Procedure: Test-AJAX-Functions-for-CSRF-Vulnerability]]
