---
id: 222b1101-1084-4344-baf5-15f5409a3e2f
name: Git Download and Install nps_payload
type: command
executor: bash
data: 'git clone https://github.com/trustedsec/nps_payload.git

  cd nps_payload && pip install -r requirements.txt'
output: 'root@kali:~# git clone https://github.com/trustedsec/nps_payload.git

  Cloning into ''nps_payload''...

  remote: Enumerating objects: 31, done.

  remote: Total 31 (delta 0), reused 0 (delta 0), pack-reused 31

  Unpacking objects: 100% (31/31), done.

  root@kali:~# cd nps_payload && pip install -r requirements.txt

  Requirement already satisfied: netifaces in /usr/local/lib/python2.7/dist-packages
  (from -r requirements.txt (line 1)) (0.10.9)

  Requirement already satisfied: pexpect in /usr/lib/python2.7/dist-packages (from
  -r requirements.txt (line 2)) (4.6.0)'
created_at: '2019-11-14T23:38:41.520291+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Git Download and Install nps_payload

```bash
git clone https://github.com/trustedsec/nps_payload.git
cd nps_payload && pip install -r requirements.txt
```

## Expected Output

```
root@kali:~# git clone https://github.com/trustedsec/nps_payload.git
Cloning into 'nps_payload'...
remote: Enumerating objects: 31, done.
remote: Total 31 (delta 0), reused 0 (delta 0), pack-reused 31
Unpacking objects: 100% (31/31), done.
root@kali:~# cd nps_payload && pip install -r requirements.txt
Requirement already satisfied: netifaces in /usr/local/lib/python2.7/dist-packages (from -r requirements.txt (line 1)) (0.10.9)
Requirement already satisfied: pexpect in /usr/lib/python2.7/dist-packages (from -r requirements.txt (line 2)) (4.6.0)
```
