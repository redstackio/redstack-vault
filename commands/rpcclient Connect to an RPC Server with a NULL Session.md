---
id: f3dcdc73-110f-4295-96f5-308d2ce272a2
name: rpcclient Connect to an RPC Server with a NULL Session
type: command
executor: ''
data: rpcclient -U "" -N $_TARGET_IP
output: 'root@kali:~# rpcclient -U '''' -N 10.10.10.10

  rpcclient $> '
created_at: '2019-09-18T23:26:06.919115+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# rpcclient Connect to an RPC Server with a NULL Session

```bash
rpcclient -U "" -N $_TARGET_IP
```

## Expected Output

```
root@kali:~# rpcclient -U '' -N 10.10.10.10
rpcclient $> 
```
