---
id: 4f80a84f-a88f-40b3-99b7-0e06d03ba87c
name: Deploy Beacon
type: command
executor: bash
data: 'beacon> help ssh

  Use: ssh [target:port] [user] [pass]

  Spawn an SSH client and attempt to login to the specified target


  beacon> help ssh-key

  Use: ssh [target:port] [user] [/path/to/key.pem]

  Spawn an SSH client and attempt to login to the specified target


  # beacon''s commands

  upload                    Upload a file

  download                  Download a file

  socks                     Start SOCKS4a server to relay traffic

  sudo                      Run a command via sudo

  rportfwd                  Setup a reverse port forward

  shell                     Execute a command via the shell'
output: null
created_at: '2023-04-06T03:56:16.358332+00:00'
updated_at: '2023-04-10T20:36:20.029042+00:00'
---

# Deploy Beacon

```bash
beacon> help ssh
Use: ssh [target:port] [user] [pass]
Spawn an SSH client and attempt to login to the specified target

beacon> help ssh-key
Use: ssh [target:port] [user] [/path/to/key.pem]
Spawn an SSH client and attempt to login to the specified target

# beacon's commands
upload                    Upload a file
download                  Download a file
socks                     Start SOCKS4a server to relay traffic
sudo                      Run a command via sudo
rportfwd                  Setup a reverse port forward
shell                     Execute a command via the shell
```


