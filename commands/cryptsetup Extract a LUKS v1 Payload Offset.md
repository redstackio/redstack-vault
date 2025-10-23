---
id: c5319306-ca0c-43b6-b32f-f8b8b566ba74
name: cryptsetup Extract a LUKS v1 Payload Offset
type: command
executor: bash
data: cryptsetup luksDump $_FILE.img
output: "root@kali:~# cryptsetup luksDump backup.img\nLUKS header information for\
  \ backup.img\n\nVersion:       \t1\nCipher name:   \taes\nCipher mode:   \txts-plain64\n\
  Hash spec:     \tsha256\nPayload offset:\t4096\nMK bits:       \t256\nMK digest:\
  \     \t9a 35 ab 3d b2 fe 09 d6 5a 92 bd 01 50 35 a6 ab dc ea 01 47 \nMK salt: \
  \      \t36 e8 8d 00 2f b0 3c 1f de 4d 9d 7b a6 9c 59 25 \n               \t7a e7\
  \ 1d d7 89 3d 9c ab ef b6 09 8c a8 7b 87 13 \nMK iterations: \t176409\nUUID:   \
  \       \td931ebb1-5edc-4453-8ab1-3d23bb85b38e"
created_at: '2019-10-17T20:33:28.982295+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# cryptsetup Extract a LUKS v1 Payload Offset

```bash
cryptsetup luksDump $_FILE.img
```

## Expected Output

```
root@kali:~# cryptsetup luksDump backup.img
LUKS header information for backup.img

Version:       	1
Cipher name:   	aes
Cipher mode:   	xts-plain64
Hash spec:     	sha256
Payload offset:	4096
MK bits:       	256
MK digest:     	9a 35 ab 3d b2 fe 09 d6 5a 92 bd 01 50 35 a6 ab dc ea 01 47 
MK salt:       	36 e8 8d 00 2f b0 3c 1f de 4d 9d 7b a6 9c 59 25 
               	7a e7 1d d7 89 3d 9c ab ef b6 09 8c a8 7b 87 13 
MK iterations: 	176409
UUID:          	d931ebb1-5edc-4453-8ab1-3d23bb85b38e
```


