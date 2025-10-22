---
id: d4dcdf46-e644-4098-bbc1-047c1e08272d
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:23.038198+00:00'
updated_at: '2023-04-10T20:25:15.142740+00:00'
---

# Code Snippet d4dcdf46

**Language**: Powershell

```powershell
# get the binary
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip 

# log into the service
./ngrok authtoken 3U[REDACTED_TOKEN]Hm

# deploy a port forwarding for 4433
./ngrok http 4433
./ngrok tcp 4433
```
