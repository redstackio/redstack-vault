---
id: d6a875d3-68f6-43b7-ab46-7ad9783d3bbd
name: fake smb server for uploading and downloading files
type: command
executor: bash
data: 'python3 /opt/impacket/examples/smbserver.py -smb2support files $(pwd)

  '
output: null
created_at: '2020-07-14T18:14:54.427184+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# fake smb server for uploading and downloading files

```bash
python3 /opt/impacket/examples/smbserver.py -smb2support files $(pwd)

```
