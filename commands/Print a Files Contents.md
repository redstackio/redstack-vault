---
id: 0e16fb39-5813-4634-b63c-18b2a238d899
name: Print a Files Contents
type: command
executor: bash
data: cat $_FILE
output: "root@00b5b1279bcc:~# cat secrets.txt \nT0ps3cr3t1nf0rma710n"
created_at: '2020-03-10T03:42:55.676980+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Print a Files Contents

```bash
cat $_FILE
```

## Expected Output

```
root@00b5b1279bcc:~# cat secrets.txt 
T0ps3cr3t1nf0rma710n
```
