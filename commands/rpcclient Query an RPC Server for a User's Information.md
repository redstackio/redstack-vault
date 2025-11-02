---
id: 0037b867-8c16-4e01-a903-7bfe8504b11b
name: rpcclient Query an RPC Server for a User's Information
type: command
executor: ''
data: queryuser $_USER_RID
output: "rpcclient $> queryuser 0x3e8\n\tUser Name   :\troot\n\tFull Name   :\troot\n\
  \tHome Drive  :\t\\\\HOST\\root\n\tDir Drive   :\n\tProfile Path:\t\\\\HOST\\root\\\
  profile\n\tLogon Script:\n\tDescription :\n\tWorkstations:\n\tComment     :\t(null)\n\
  \tRemote Dial :\n\tLogon Time               :\tWed, 31 Dec 1969 19:00:00 EST\n\t\
  Logoff Time              :\tWed, 13 Sep 30828 22:48:05 EDT\n\tKickoff Time     \
  \        :\tWed, 13 Sep 30828 22:48:05 EDT\n\tPassword last set Time   :\tWed, 31\
  \ Dec 1969 19:00:00 EST\n\tPassword can change Time :\tWed, 31 Dec 1969 19:00:00\
  \ EST\n\tPassword must change Time:\tWed, 13 Sep 30828 22:48:05 EDT\n\tunknown_2[0..31]...\n\
  \tuser_rid :\t0x3e8\n\tgroup_rid:\t0x3e9\n\tacb_info :\t0x00000011\n\tfields_present:\t\
  0x00ffffff\n\tlogon_divs:\t168\n\tbad_password_count:\t0x00000000\n\tlogon_count:\t\
  0x00000000\n\tpadding1[0..7]...\n\tlogon_hrs[0..21]..."
created_at: '2019-09-18T22:53:24.467223+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[SET]]'
- '[[dir]]'
- '[[host]]'
- '[[rpcclient]]'
---

# rpcclient Query an RPC Server for a User's Information

```bash
queryuser $_USER_RID
```

## Expected Output

```
rpcclient $> queryuser 0x3e8
	User Name   :	root
	Full Name   :	root
	Home Drive  :	\\HOST\root
	Dir Drive   :
	Profile Path:	\\HOST\root\profile
	Logon Script:
	Description :
	Workstations:
	Comment     :	(null)
	Remote Dial :
	Logon Time               :	Wed, 31 Dec 1969 19:00:00 EST
	Logoff Time              :	Wed, 13 Sep 30828 22:48:05 EDT
	Kickoff Time             :	Wed, 13 Sep 30828 22:48:05 EDT
	Password last set Time   :	Wed, 31 Dec 1969 19:00:00 EST
	Password can change Time :	Wed, 31 Dec 1969 19:00:00 EST
	Password must change Time:	Wed, 13 Sep 30828 22:48:05 EDT
	unknown_2[0..31]...
	user_rid :	0x3e8
	group_rid:	0x3e9
	acb_info :	0x00000011
	fields_present:	0x00ffffff
	logon_divs:	168
	bad_password_count:	0x00000000
	logon_count:	0x00000000
	padding1[0..7]...
	logon_hrs[0..21]...
```


