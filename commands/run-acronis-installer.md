---
id: acronis-silent-install
data: AcronisTrueImage2021.exe /SILENT
tags:
  - installer
  - trigger
type: command
output: Installation completed.
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:52.196Z'
verified: false
validated: true
submitted: true
---
# run-acronis-installer

## Command

```cmd
AcronisTrueImage2021.exe /SILENT
```

## Description

Runs the Acronis True Image 2021 installer in silent mode to trigger the Scheduler2 Service startup without user interaction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /SILENT | No UI, automated install | Yes |

## Examples

### Basic Usage

```cmd
AcronisTrueImage2021.exe /SILENT
```

### With Log

```cmd
AcronisTrueImage2021.exe /SILENT /LOG install.log
```

## Expected Output

Silent completion; check logs for success.

## Related

- [[tools/Acronis-True-Image-2021-Installer]]
- [[procedures/Install-Acronis-True-Image-to-Trigger-Service]]
