---
id: 5a83e245-fc3e-4827-9a51-86ae571f2e04
name: Whatweb Identify a Web Server's Technology
type: command
executor: bash
data: whatweb http://$_TARGET_IP
output: 'root@kali:~# whatweb http://10.10.10.10

  http://10.10.10.10 [200 OK] Apache[2.2.8], Country[RESERVED][ZZ], HTTPServer[Ubuntu
  Linux][Apache/2.2.8 (Ubuntu) DAV/2], IP[10.10.10.10], PHP[5.2.4-2ubuntu5.10], Title[Host
  - Linux], WebDAV[2], X-Powered-By[PHP/5.2.4-2ubuntu5.10]'
created_at: '2019-09-13T22:29:10.949912+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Whatweb Identify a Web Server's Technology

```bash
whatweb http://$_TARGET_IP
```

## Expected Output

```
root@kali:~# whatweb http://10.10.10.10
http://10.10.10.10 [200 OK] Apache[2.2.8], Country[RESERVED][ZZ], HTTPServer[Ubuntu Linux][Apache/2.2.8 (Ubuntu) DAV/2], IP[10.10.10.10], PHP[5.2.4-2ubuntu5.10], Title[Host - Linux], WebDAV[2], X-Powered-By[PHP/5.2.4-2ubuntu5.10]
```
