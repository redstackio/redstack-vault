---
id: 396a2460-1bfe-4fa6-8751-cecd6ea0a511
name: Metasploit Search Module Names and Descriptions
type: command
executor: metasploit
data: search $_STRING
output: "msf5 > search eternalblue\n\nMatching Modules\n================\n\n   # \
  \ Name                                           Disclosure Date  Rank     Check\
  \  Description\n   -  ----                                           ---------------\
  \  ----     -----  -----------\n   0  auxiliary/admin/smb/ms17_010_command     \
  \      2017-03-14       normal   No     MS17-010 EternalRomance/EternalSynergy/EternalChampion\
  \ SMB Remote Windows Command Execution\n   1  auxiliary/scanner/smb/smb_ms17_010\
  \                              normal   No     MS17-010 SMB RCE Detection\n   2\
  \  exploit/windows/smb/ms17_010_eternalblue       2017-03-14       average  Yes\
  \    MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption\n   3  exploit/windows/smb/ms17_010_eternalblue_win8\
  \  2017-03-14       average  No     MS17-010 EternalBlue SMB Remote Windows Kernel\
  \ Pool Corruption for Win8+\n   4  exploit/windows/smb/ms17_010_psexec         \
  \   2017-03-14       normal   Yes    MS17-010 EternalRomance/EternalSynergy/EternalChampion\
  \ SMB Remote Windows Code Execution\n   5  exploit/windows/smb/smb_doublepulsar_rce\
  \       2017-04-14       great    Yes    SMB DOUBLEPULSAR Remote Code Execution"
created_at: '2020-07-08T22:56:24.136406+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Metasploit Search Module Names and Descriptions

```metasploit
search $_STRING
```

## Expected Output

```
msf5 > search eternalblue

Matching Modules
================

   #  Name                                           Disclosure Date  Rank     Check  Description
   -  ----                                           ---------------  ----     -----  -----------
   0  auxiliary/admin/smb/ms17_010_command           2017-03-14       normal   No     MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Command Execution
   1  auxiliary/scanner/smb/smb_ms17_010                              normal   No     MS17-010 SMB RCE Detection
   2  exploit/windows/smb/ms17_010_eternalblue       2017-03-14       average  Yes    MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption
   3  exploit/windows/smb/ms17_010_eternalblue_win8  2017-03-14       average  No     MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption for Win8+
   4  exploit/windows/smb/ms17_010_psexec            2017-03-14       normal   Yes    MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Code Execution
   5  exploit/windows/smb/smb_doublepulsar_rce       2017-04-14       great    Yes    SMB DOUBLEPULSAR Remote Code Execution
```


