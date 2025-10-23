---
id: a49ecb1e-697b-4fb7-885e-78b24e560d86
name: Disable systemd-resolved and update resolv.conf
type: command
executor: bash
data: 'systemctl disable systemd-resolved

  systemctl stop systemd-resolved

  rm /etc/resolv.conf

  echo "nameserver 8.8.8.8" >  /etc/resolv.conf

  echo "nameserver 8.8.4.4" >>  /etc/resolv.conf'
output: null
created_at: '2023-04-06T03:56:16.301513+00:00'
updated_at: '2023-04-10T20:36:21.464920+00:00'
---

# Disable systemd-resolved and update resolv.conf

```bash
systemctl disable systemd-resolved
systemctl stop systemd-resolved
rm /etc/resolv.conf
echo "nameserver 8.8.8.8" >  /etc/resolv.conf
echo "nameserver 8.8.4.4" >>  /etc/resolv.conf
```


