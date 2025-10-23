---
id: 4ca3ab07-4f4d-4014-99fc-3ea6c899c595
name: Optimize wordlist for hashcat
type: command
executor: bash
data: $ hashcat64.exe -m 1000 -w 4 -O -a 0 -o pathtopotfile pathtohashes pathtodico
  -r myrules.rule --opencl-device-types 1,2
output: null
created_at: '2023-04-06T03:56:04.096803+00:00'
updated_at: '2023-04-10T20:26:22.286747+00:00'
---

# Optimize wordlist for hashcat

```bash
$ hashcat64.exe -m 1000 -w 4 -O -a 0 -o pathtopotfile pathtohashes pathtodico -r myrules.rule --opencl-device-types 1,2
```


