---
id: a7afca96-dafc-4c4d-b133-863a4dd3c708
name: ssh
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:35.262945+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# ssh

**Command** ([[create ssh-key]]):

```bash
ssh-keygen

```

**Command** ([[add public-key to authorized_keys]]):

```bash
cat rsa.pub >> authorized_keys

```

**Command** ([[set permission on private-key]]):

```bash
chmod 600 id_rsa

```

**Command** ([[login via ssh-key]]):

```bash
ssh -i id_rsa username@target-ip

```

**Command** ([[login with older ciphers]]):

```bash
ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -c aes128-cbc username@target-ip

```

**Command** ([[start tool after ssh login]]):

```bash
ssh username@target-ip -o "ProxyCommand=ncat --proxy-type http --proxy target-ip:proxy-port 127.0.0.1 22"

```

**Command** ([[ssh port forwarding]]):

```bash
ssh -N -L 80:127.0.0.1:80 username@target-ip

```

**Command** ([[dynamic ssh port forward]]):

```bash
ssh -N -D 9050 username@target-ip

```
