---
id: c4d12e5a-1cca-4a2c-94ca-4bd5f2afcd9c
name: smbclient-download-files-recursively
type: command
executor: bash
data: |-
  smb: \$_SHARE_NAME\> RECURSE ON
  smb: \$_SHARE_NAME\> PROMPT OFF
  smb: \$_SHARE_NAME\> mget *
output: >-
  smb: \Bob\> RECURSE ON

  smb: \Bob\> PROMPT OFF

  smb: \Bob\> mget *

  NT_STATUS_SHARING_VIOLATION opening remote file \Bob\NTUSER.DAT

  NT_STATUS_SHARING_VIOLATION opening remote file \Bob\ntuser.dat.LOG1

  NT_STATUS_SHARING_VIOLATION opening remote file \Bob\ntuser.dat.LOG2

  getting file \Bob\NTUSER.DAT{6cced2f1-6e01-11de-8bed-001e0bcd1824}.TM.blf of
  size 65536 as NTUSER.DAT{6cced2f1-6e01-11de-8bed-001e0bcd1824}.TM.blf (7999.9
  KiloBytes/sec) (average 8000.0 KiloBytes/sec)

  getting file
  \Bob\NTUSER.DAT{6cced2f1-6e01-11de-8bed-001e0bcd1824}.TMContainer00000000000000000001.regtrans-ms
  of size 524288 as
  NTUSER.DAT{6cced2f1-6e01-11de-8bed-001e0bcd1824}.TMContainer00000000000000000001.regtrans-ms
  (25599.9 KiloBytes/sec) (average 20571.4 KiloBytes/sec)

  getting file
  \Bob\NTUSER.DAT{6cced2f1-6e01-11de-8bed-001e0bcd1824}.TMContainer00000000000000000002.regtrans-ms
  of size 524288 as
  NTUSER.DAT{6cced2f1-6e01-11de-8bed-001e0bcd1824}.TMContainer00000000000000000002.regtrans-ms
  (51199.5 KiloBytes/sec) (average 28631.6 KiloBytes/sec)

  getting file \Bob\ntuser.ini of size 20 as ntuser.ini (9.8 KiloBytes/sec)
  (average 27200.5 KiloBytes/sec)
created_at: '2019-09-18T01:44:02.128880+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - smb
  - file-download
verified: true
validated: true
---

# smbclient-download-files-recursively

## Command

```bash
smb: \$_SHARE_NAME\> RECURSE ON
smb: \$_SHARE_NAME\> PROMPT OFF
smb: \$_SHARE_NAME\> mget *
```

## Description

This sequence of smbclient subcommands enables recursive file downloading from an SMB share. Run these inside an established smbclient session to bulk-transfer all files and directories without manual confirmation for each item. Ideal for data exfiltration in scenarios with large shares.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SHARE_NAME | The mounted SMB share path (e.g., \Users\bob) | Yes |
| RECURSE ON | Enables recursive traversal into subdirectories | Built-in |
| PROMPT OFF | Disables interactive prompts for file transfers | Built-in |
| mget * | Downloads all files (*) recursively | Built-in |

## Examples

### Basic Usage

```bash
smb: \Users\> RECURSE ON
smb: \Users\> PROMPT OFF
smb: \Users\> mget *
```

### Advanced Usage

```bash
smb: \Users\bob\> RECURSE ON
smb: \Users\bob\> PROMPT OFF
smb: \Users\bob\> mget documents *
```
(Targets a specific subfolder and file pattern for selective download.)

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

The output indicates successful configuration, skips locked files with violations, and shows transfer progress with speeds and averages. All downloaded files appear in the local directory.

## Related

- [[commands/smbclient-connect-to-smb-share-with-ntlm]]
- [[procedures/Recursively-Download-Files-From-SMB-Share]]
