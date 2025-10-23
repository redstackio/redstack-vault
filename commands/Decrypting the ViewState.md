---
id: 21a4766e-6bca-47c1-98c4-ccc92aa0ed22
name: Decrypting the ViewState
type: command
executor: bash
data: $ AspDotNetWrapper.exe --keypath MachineKeys.txt --encrypteddata <real viewstate
  value> --purpose=viewstate --modifier=<modifier value> –macdecode
output: null
created_at: '2023-04-06T03:55:52.537056+00:00'
updated_at: '2023-04-06T03:55:52.543704+00:00'
---

# Decrypting the ViewState

```bash
$ AspDotNetWrapper.exe --keypath MachineKeys.txt --encrypteddata <real viewstate value> --purpose=viewstate --modifier=<modifier value> –macdecode
```


