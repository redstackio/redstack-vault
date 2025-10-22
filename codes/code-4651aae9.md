---
id: 4651aae9-f5e6-476b-b9c6-ca5a368b6b1b
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:24.983731+00:00'
updated_at: '2023-04-10T20:25:31.246275+00:00'
---

# Code Snippet 4651aae9

**Language**: Powershell

```powershell
/bin/sh -i
python3 -c 'import pty; pty.spawn("/bin/sh")'
python3 -c "__import__('pty').spawn('/bin/bash')"
python3 -c "__import__('subprocess').call(['/bin/bash'])"
perl -e 'exec "/bin/sh";'
perl: exec "/bin/sh";
perl -e 'print `/bin/bash`'
ruby: exec "/bin/sh"
lua: os.execute('/bin/sh')
```
