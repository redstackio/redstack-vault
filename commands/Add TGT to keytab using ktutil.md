---
id: 769abee5-6506-487b-8350-2f0b057ed0e6
name: Add TGT to keytab using ktutil
type: command
executor: bash
data: ktutil -k ~/mykeys add -p tgwynn@LAB.ROPNOP.COM -e arcfour-hma-md5 -w 1a59bd44fe5bec39c44c8cd3524dee
  --hex -V 5
output: null
created_at: '2023-04-06T03:56:05.111593+00:00'
updated_at: '2023-04-10T20:25:57.396165+00:00'
---

# Add TGT to keytab using ktutil

```bash
ktutil -k ~/mykeys add -p tgwynn@LAB.ROPNOP.COM -e arcfour-hma-md5 -w 1a59bd44fe5bec39c44c8cd3524dee --hex -V 5
```


