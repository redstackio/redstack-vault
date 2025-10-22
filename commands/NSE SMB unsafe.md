---
id: 494c1e7d-e22b-4027-aaee-273cac07b7c8
name: NSE SMB unsafe
type: command
executor: bash
data: 'nmap --script=smb-* -p139,445 --script-args=unsafe=1 $ip

  '
output: null
created_at: '2020-07-14T18:15:19.609201+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# NSE SMB unsafe

```bash
nmap --script=smb-* -p139,445 --script-args=unsafe=1 $ip

```
