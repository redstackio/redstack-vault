---
id: bd75191a-1749-4e96-b241-59715c5fe2b5
name: Linux
type: cheatsheet
verified: false
created_at: '2020-07-14T18:21:26.328718+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Linux

**Code**: [[
for u in `cat hosts.txt`; do
  echo -n "[*] user:]]

**Code**: [[
function start_sshtunnel() {
  ssh -A -t -p22 -L ]]

**Code**: [[
# .bash_profile PATH=$PATH:/home/james/ export PA]]

# Linux Enumeration

**Command** ([[List open files]]):

```bash
lsof

```

**Command** ([[without kernel]]):

```bash
lsof -b

```

**Command** ([[PIDs only]]):

```bash
lsof -t

```

**Command** ([[by user]]):

```bash
lsof -u username1,username2

```

**Command** ([[omit user]]):

```bash
lsof -u ^username3

```

**Command** ([[List network files]]):

```bash
lsof -i

```

**Command** ([[IPv4]]):

```bash
lsof -i4

```

**Command** ([[IPv6]]):

```bash
lsof -i6

```

**Command** ([[by protocol]]):

```bash
lsof -i TCP
lsof -i UDP

```

**Command** ([[List open network files by service]]):

```bash
lsof -i TCP:https

```

**Command** ([[by port]]):

```bash
lsof -i TCP:8443
lsof -i TCP:10-1024

```

**Command** ([[list PIDs]]):

```bash
lsof -t -i

```

**Command** ([[no port conversion]]):

```bash
lsof -i -P

```

**Command** ([[no name conversion]]):

```bash
lsof -i -n

```

**Command** ([[listening]]):

```bash
lsof -nP -i TCP -s TCP:LISTEN

```

**Command** ([[connections]]):

```bash
lsof -i | awk '{print $8}' | sort | uniq -c | grep 'TCP\|UDP'

```

**Command** ([[established]]):

```bash
lsof -i -nP | grep ESTABLISHED | awk '{print $1, $9}' | sort -u

```

**Command** ([[active]]):

```bash
lsof -nP -iTCP -sTCP:ESTABLISHED | grep HTTPS

```

**Command** ([[List files by PID]]):

```bash
lsof -p 5432,8484

```

**Command** ([[include PPID]]):

```bash
lsof -R

```

**Command** ([[include PPID by PID]]):

```bash
lsof -p 5432 -R

```

**Command** ([[List PIDs that opened file]]):

```bash
lsof -t /path/to/file

```

**Command** ([[List files by Process Name]]):

```bash
lsof -c firefox

```

**Command** ([[List files in directory]]):

```bash
lsof +D DirectoryName

```

**Command** ([[List files with subdirectories]]):

```bash
lsof +d DirectoryName

```

**Command** ([[List NFS use]]):

```bash
lsof -N

```

**Command** ([[List IPC]]):

```bash
lsof -U

```

**Command** ([[by PID]]):

```bash
lsof -U -a -p 8484

```

**Command** ([[Kill processes of specific user]]):

```bash
sudo kill -9 `lsof -t -u username1`

```
