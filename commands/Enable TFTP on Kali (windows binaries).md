---
id: 39323b73-b1e1-47ce-9ef7-163b51190cf6
name: Enable TFTP on Kali (windows binaries)
type: command
executor: bash
data: 'ln -s /usr/share/windows-binaries/ /tftp

  atfpd --daemon --port 69 /tftp

  '
output: null
created_at: '2020-07-14T18:14:33.482249+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Enable TFTP on Kali (windows binaries)

```bash
ln -s /usr/share/windows-binaries/ /tftp
atfpd --daemon --port 69 /tftp

```


