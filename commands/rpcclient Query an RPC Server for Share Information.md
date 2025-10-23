---
id: 9d7f0bf4-c9c2-48d4-b8e8-17c7b604944d
name: rpcclient Query an RPC Server for Share Information
type: command
executor: ''
data: netsharegetinfo $_SHARE_NAME
output: "rpcclient $> netsharegetinfo tmp\nnetname: tmp\n\tremark:\tstaging\n\tpath:\t\
  C:\\inetpub\n\tpassword:\n\ttype:\t0x0\n\tperms:\t0\n\tmax_uses:\t-1\n\tnum_uses:\t\
  1\nrevision: 1\ntype: 0x8004: SEC_DESC_DACL_PRESENT SEC_DESC_SELF_RELATIVE\nDACL\n\
  \tACL\tNum ACEs:\t1\trevision:\t2\n\t---\n\tACE\n\t\ttype: ACCESS ALLOWED (0) flags:\
  \ 0x00\n\t\tSpecific bits: 0x1ff\n\t\tPermissions: 0x101f01ff: Generic all access\
  \ SYNCHRONIZE_ACCESS WRITE_OWNER_ACCESS WRITE_DAC_ACCESS READ_CONTROL_ACCESS DELETE_ACCESS\n\
  \t\tSID: S-1-1-0"
created_at: '2019-09-18T22:53:24.473873+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# rpcclient Query an RPC Server for Share Information

```bash
netsharegetinfo $_SHARE_NAME
```

## Expected Output

```
rpcclient $> netsharegetinfo tmp
netname: tmp
	remark:	staging
	path:	C:\inetpub
	password:
	type:	0x0
	perms:	0
	max_uses:	-1
	num_uses:	1
revision: 1
type: 0x8004: SEC_DESC_DACL_PRESENT SEC_DESC_SELF_RELATIVE
DACL
	ACL	Num ACEs:	1	revision:	2
	---
	ACE
		type: ACCESS ALLOWED (0) flags: 0x00
		Specific bits: 0x1ff
		Permissions: 0x101f01ff: Generic all access SYNCHRONIZE_ACCESS WRITE_OWNER_ACCESS WRITE_DAC_ACCESS READ_CONTROL_ACCESS DELETE_ACCESS
		SID: S-1-1-0
```


