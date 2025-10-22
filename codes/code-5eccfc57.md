---
id: 5eccfc57-405c-4690-9c35-b4fe37a56bba
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:06.582947+00:00'
updated_at: '2023-04-10T20:26:30.727457+00:00'
---

# Code Snippet 5eccfc57

**Language**: ps1

```ps1
# For the pfx
echo AAAAAQAAAAAEE[...]Qla6 | base64 -d > EncryptedPfx.bin
# For the private key
echo f7404c7f[...]aabd8b | xxd -r -p > dkmKey.bin 
```
