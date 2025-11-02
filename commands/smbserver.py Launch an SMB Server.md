---
id: 362264f8-f7b9-4e37-8f2c-ca640b45ccac
name: smbserver.py Launch an SMB Server
type: command
executor: bash
data: smbserver.py $_SHARE $_PATH
output: 'smbserver.py share /tmp

  Impacket v0.9.20-dev - Copyright 2019 SecureAuth Corporation


  [*] Config file parsed

  [*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0

  [*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0

  [*] Config file parsed

  [*] Config file parsed

  [*] Config file parsed'
created_at: '2019-10-29T22:25:12.709431+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Impacket]]'
---

# smbserver.py Launch an SMB Server

```bash
smbserver.py $_SHARE $_PATH
```

## Expected Output

```
smbserver.py share /tmp
Impacket v0.9.20-dev - Copyright 2019 SecureAuth Corporation

[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed
[*] Config file parsed
```


