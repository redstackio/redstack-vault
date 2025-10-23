---
id: 23ee6634-7da7-4795-9886-62025207e609
name: Launch a Python 3 Web Server
type: command
executor: bash
data: python3 -m http.server $_PORT
output: 'root@kali:~# python3 -m http.server 80

  Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...'
created_at: '2019-10-29T22:25:12.708225+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Launch a Python 3 Web Server

```bash
python3 -m http.server $_PORT
```

## Expected Output

```
root@kali:~# python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
```


