---
id: ce4665b8-3c5e-43c6-91f4-0541dbedf75c
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:04.096740+00:00'
updated_at: '2023-04-10T20:26:22.228237+00:00'
---

# Code Snippet ce4665b8

**Language**: Powershell

```powershell
# Basic wordlist
# (-O) will Optimize for 32 characters or less passwords
# (-w 4) will set the workload to "Insane" 
$ hashcat64.exe -m 1000 -w 4 -O -a 0 -o pathtopotfile pathtohashes pathtodico -r myrules.rule --opencl-device-types 1,2

# Generate a custom mask based on a wordlist
$ git clone https://github.com/iphelix/pack/blob/master/README
$ python2 statsgen.py ../hashcat.potfile -o hashcat.mask
$ python2 maskgen.py hashcat.mask --targettime 3600 --optindex -q -o hashcat_1H.hcmask
```
