---
id: 62855e89-86e6-4e57-8e08-395f62703c5b
name: rpcclient Query an RPC Server for SMB Shares
type: command
executor: ''
data: netshareenumall
output: "rpcclient $> netshareenumall\nnetname: print$\n\tremark:\tPrinter Drivers\n\
  \tpath:\tC:\\var\\lib\\samba\\printers\n\tpassword:\nnetname: opt\n\tremark:\n\t\
  path:\tC:\\tmp\n\tpassword:\nnetname: IPC$\n\tremark:\tIPC Service (host server\
  \ (Samba 3.0.20-Debian))\n\tpath:\tC:\\tmp\n\tpassword:\nnetname: ADMIN$\n\tremark:\t\
  IPC Service (host server (Samba 3.0.20-Debian))\n\tpath:\tC:\\tmp\n\tpassword:\n"
created_at: '2019-09-18T22:53:24.472705+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# rpcclient Query an RPC Server for SMB Shares

```bash
netshareenumall
```

## Expected Output

```
rpcclient $> netshareenumall
netname: print$
	remark:	Printer Drivers
	path:	C:\var\lib\samba\printers
	password:
netname: opt
	remark:
	path:	C:\tmp
	password:
netname: IPC$
	remark:	IPC Service (host server (Samba 3.0.20-Debian))
	path:	C:\tmp
	password:
netname: ADMIN$
	remark:	IPC Service (host server (Samba 3.0.20-Debian))
	path:	C:\tmp
	password:

```


