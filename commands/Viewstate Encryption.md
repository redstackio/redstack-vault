---
id: 2f970fa2-3b87-42af-9611-7f7a981e01b9
name: Viewstate Encryption
type: command
executor: bash
data: AspDotNetWrapper.exe --keypath MachineKeys.txt --encrypteddata <real viewstate
  value> --purpose=viewstate --modifier=<modifier value> –macdecode
output: null
created_at: '2023-04-06T03:55:51.754444+00:00'
updated_at: '2023-04-10T20:21:10.233434+00:00'
---

# Viewstate Encryption

```bash
AspDotNetWrapper.exe --keypath MachineKeys.txt --encrypteddata <real viewstate value> --purpose=viewstate --modifier=<modifier value> –macdecode
```
