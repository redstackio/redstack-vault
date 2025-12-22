---
data: >-
  function Send-NetworkData {

  [CmdletBinding()]

  param (

  [Parameter(Mandatory)][string]$Computer,

  [Parameter(Mandatory)][ValidateRange(1, 65535)][Int16]$Port,

  [Parameter(ValueFromPipeline)]string[]$Data,

  [System.Text.Encoding]$Encoding = [System.Text.Encoding]::ASCII,

  [TimeSpan]$Timeout = [System.Threading.Timeout]::InfiniteTimeSpan)


  begin {

  $Client = New-Object -TypeName System.Net.Sockets.TcpClient

  $Client.Connect($Computer, $Port)

  $Stream = $Client.GetStream()

  $Writer = New-Object -Type System.IO.StreamWriter -ArgumentList $Stream,
  $Encoding, $Client.SendBufferSize, $true

  }

  process {

  foreach ($Line in $Data) {

  $Writer.WriteLine($Line)

  }

  }

  end {

  $Writer.Flush()

  $Writer.Dispose()

  $Client.Client.Shutdown('Send')

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

  $Stream.Dispose()

  $Client.Dispose()

  }

  }
tags:
  - tcp
  - network-send
  - http-raw
type: command
executor: powershell
platforms:
  - Windows
id: 214ad614-9e1e-4dfa-a23f-773ca25a5026
created_at: '2025-12-14T05:32:10.002Z'
updated_at: '2025-12-14T05:32:10.002Z'
verified: false
validated: true
submitted: true
---
# Send-NetworkData-TCP-Function

## Command

```powershell
function Send-NetworkData { ... } # Full function definition as above
```

## Description

Custom PowerShell function to establish TCP connection, send raw data (e.g., HTTP POST), and read response. Used for low-level HTTP simulation in uploads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $Computer | Target IP/hostname | Yes |
| $Port | Target port (e.g., 80) | Yes |
| $Data | Input data array (piped POST body) | Yes |
| $Encoding | Encoding (default ASCII) | No |
| $Timeout | Read timeout (default infinite) | No |

## Examples

### Basic Usage

```powershell
echo "GET / HTTP/1.1`nHost: example.com" | Send-NetworkData -Computer example.com -Port 80
```

### Advanced Usage

```powershell
# With timeout
... | Send-NetworkData -Computer $ip -Port 80 -Timeout (New-TimeSpan -Seconds 10)
```

## Expected Output

Server response string accumulated in $Result and outputted to console.

## Related

- [[commands/powershell-script-for-mass-file-upload-dos]]
- [[procedures/test-unauthenticated-file-upload-to-login-cgi]]
