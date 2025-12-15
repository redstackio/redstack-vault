---
id: cmd-wget-apk-001
data: 'wget https://devbuilds.uber.com/path/to/development-app.apk -O uber-dev.apk'
tags:
  - download
  - recon
type: command
output: saved 12345678/12345678 bytes
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:43.032Z'
verified: false
validated: true
submitted: true
---
# wget-download-apk

## Command

```bash
wget https://devbuilds.uber.com/path/to/development-app.apk -O uber-dev.apk
```

## Description

Downloads an APK file from a public development build server URL using wget, saving it locally for analysis. Useful for retrieving exposed mobile app artifacts during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | The full HTTPS URL to the APK file | Yes |
| -O | Output filename for the downloaded file | No (defaults to remote name) |

## Examples

### Basic Usage

```bash
wget https://devbuilds.uber.com/app.apk -O app.apk
```

### Advanced Usage

```bash
wget --user-agent="Mozilla/5.0" https://devbuilds.uber.com/app.apk -O app.apk --timeout=30
```

## Expected Output

Progress bar showing download percentage, followed by "saved [size]/[size] bytes" on success. Errors include connection failures or 404 if URL invalid.

## Related

- [[commands/curl-download]]
- [[procedures/Download-APK-from-Development-Build-Server]]
