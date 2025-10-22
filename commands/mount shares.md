---
id: 23844244-bd04-45e5-9f7a-482caeaf6420
name: mount shares
type: command
executor: bash
data: 'mount -o hard,nolock target-ip:/home folder

  mount -t cifs -o user=username,domain=domainname //target-ip/share /mnt/folder

  '
output: null
created_at: '2020-07-14T18:15:01.391259+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# mount shares

```bash
mount -o hard,nolock target-ip:/home folder
mount -t cifs -o user=username,domain=domainname //target-ip/share /mnt/folder

```
