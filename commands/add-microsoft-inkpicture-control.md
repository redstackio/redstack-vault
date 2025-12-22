---
id: 0f76f2c0-fd31-4d40-a0e7-f477fe884437
type: command
executor: ms-word
data: Insert > More Controls > Microsoft InkPicture Control
output: null
created_at: '2023-04-06T03:56:23.729774+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - office
  - activex
  - macro
verified: true
validated: true
---

# add-microsoft-inkpicture-control

## Command

Navigate to: Insert > More Controls > Microsoft InkPicture Control

## Description

This GUI command adds the Microsoft InkPicture ActiveX control to a Word document, enabling interactive drawing functionality that can trigger associated events like Painted for malicious purposes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Insert Tab | Access the Insert ribbon in Word | Yes |
| More Controls | Dropdown menu to select ActiveX controls | Yes |
| Microsoft InkPicture Control | Specific control for ink/drawing input | Yes |

## Examples

### Basic Usage

1. Open Word and create or open a .docm document.
2. Go to Insert tab.
3. Click "Object" > "Create from File" or directly "More Controls" if available in legacy toolbars.
4. Select "Microsoft InkPicture Control 1.0".

### Advanced Usage

Position the control via drag-and-drop after insertion, then access VBA editor (Alt+F11) to attach events.

## Expected Output

The control embeds as an interactive rectangle in the document. Users can draw inside it with mouse or stylus, firing events upon completion.

## Related

- [[procedures/ActiveX-Based-Autorun-Macro-with-InkPicture-Control-and-Painted-Event]]
