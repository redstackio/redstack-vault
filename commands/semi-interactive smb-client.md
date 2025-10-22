---
id: 1bd59c3c-0cf6-45f0-a6e1-fcf04eb80a70
name: semi-interactive smb-client
type: command
executor: bash
data: 'python3 /opt/impacket/examples/smbclient.py username@target-ip

  python3 /opt/impacket/examples/smbclient.py ''username''@target-ip

  python3 /opt/impacket/examples/smbclient.py ''''@target-ip

  '
output: null
created_at: '2020-07-14T18:15:12.612456+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# semi-interactive smb-client

```bash
python3 /opt/impacket/examples/smbclient.py username@target-ip
python3 /opt/impacket/examples/smbclient.py 'username'@target-ip
python3 /opt/impacket/examples/smbclient.py ''@target-ip

```
