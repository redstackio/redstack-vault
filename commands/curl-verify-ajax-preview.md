---
id: cmd-curl-verify-001
data: >-
  curl -s -i 'https://www.drivegrab.com/wp-admin/admin-ajax.php' --data
  'action=frm_forms_preview'
tags:
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:09.993Z'
verified: false
validated: true
submitted: true
---
# curl-verify-ajax-preview

## Command

```bash
curl -s -i 'https://www.drivegrab.com/wp-admin/admin-ajax.php' --data 'action=frm_forms_preview'
```

## Description

Verifies the accessibility of the Formidable Pro AJAX preview endpoint by sending a POST request to render the default form.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, suppresses progress meter | Yes |
| `-i` | Include response headers | Yes |
| `--data` | POST data with action parameter | Yes |
| `action` | Set to 'frm_forms_preview' for preview | Yes |

## Examples

### Basic Usage

```bash
curl -s -i 'https://target.com/wp-admin/admin-ajax.php' --data 'action=frm_forms_preview'
```

### Advanced Usage

```bash
curl -s -i -X POST 'https://target.com/wp-admin/admin-ajax.php' --data 'action=frm_forms_preview&form_id=1'
```

## Expected Output

HTTP/1.1 200 OK headers followed by HTML containing the default contact form elements.

## Related

- [[Related Procedure: Verify-Formidable-Forms-Preview-Endpoint]]
