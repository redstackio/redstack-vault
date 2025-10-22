---
id: d389f7c0-2d89-4c22-a8df-0fdfe650d5ea
name: dd Extract a LUKS v1 Hash
type: command
executor: bash
data: dd if=$_FILE.img of=$_HASH bs=512 count=$_OFFSET
output: 'root@kali:~# dd if=backup.img of=hash bs=512 count=4097

  4097+0 records in

  4097+0 records out

  2097664 bytes (2.1 MB, 2.0 MiB) copied, 0.0162948 s, 129 MB/s'
created_at: '2019-10-17T20:33:28.986999+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# dd Extract a LUKS v1 Hash

```bash
dd if=$_FILE.img of=$_HASH bs=512 count=$_OFFSET
```

## Expected Output

```
root@kali:~# dd if=backup.img of=hash bs=512 count=4097
4097+0 records in
4097+0 records out
2097664 bytes (2.1 MB, 2.0 MiB) copied, 0.0162948 s, 129 MB/s
```
