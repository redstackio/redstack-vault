---
id: 081577dd-2d07-4144-8c22-27a265c13b86
name: Connect to MSSQL server using sqsh and python
type: command
executor: bash
data: 'sqsh -S 192.168.1.X -U sa -P superPassword

  python mssqlclient.py WORKGROUP/Administrator:password@192.168.1X -port 46758'
output: null
created_at: '2023-04-06T03:56:33.953478+00:00'
updated_at: '2023-04-10T20:22:46.090384+00:00'
---

# Connect to MSSQL server using sqsh and python

```bash
sqsh -S 192.168.1.X -U sa -P superPassword
python mssqlclient.py WORKGROUP/Administrator:password@192.168.1X -port 46758
```
