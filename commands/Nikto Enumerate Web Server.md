---
id: 0f953868-c26d-4178-b698-fe8e3d22f6e8
name: Nikto Enumerate Web Server
type: command
executor: bash
data: nikto -host http://$_TARGET_IP
output: "root@kali:~# nikto -host http://10.10.10.10\n- Nikto v2.1.6\n---------------------------------------------------------------------------\n\
  + Target IP:          10.10.10.10\n+ Target Hostname:    10.10.10.10\n+ Target Port:\
  \        80\n+ Start Time:         2019-09-13 22:39:46 (GMT-4)\n---------------------------------------------------------------------------\n\
  + Server: Apache/2.4.29 (Ubuntu)\n+ Server leaks inodes via ETags, header found\
  \ with file /, fields: 0x2aa6 0x59277789d6649 \n+ The anti-clickjacking X-Frame-Options\
  \ header is not present.\n+ The X-XSS-Protection header is not defined. This header\
  \ can hint to the user agent to protect against some forms of XSS\n+ The X-Content-Type-Options\
  \ header is not set. This could allow the user agent to render the content of the\
  \ site in a different fashion to the MIME type\n+ No CGI Directories found (use\
  \ '-C all' to force check all possible dirs)\n+ Allowed HTTP Methods: GET, POST,\
  \ OPTIONS, HEAD \n+ OSVDB-3233: /icons/README: Apache default file found.\n+ 7499\
  \ requests: 0 error(s) and 6 item(s) reported on remote host\n+ End Time:      \
  \     2019-09-13 22:40:01 (GMT-4) (15 seconds)\n---------------------------------------------------------------------------\n\
  + 1 host(s) tested"
created_at: '2019-09-14T05:30:22.069179+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Nikto Enumerate Web Server

```bash
nikto -host http://$_TARGET_IP
```

## Expected Output

```
root@kali:~# nikto -host http://10.10.10.10
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.10.10
+ Target Hostname:    10.10.10.10
+ Target Port:        80
+ Start Time:         2019-09-13 22:39:46 (GMT-4)
---------------------------------------------------------------------------
+ Server: Apache/2.4.29 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, fields: 0x2aa6 0x59277789d6649 
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: GET, POST, OPTIONS, HEAD 
+ OSVDB-3233: /icons/README: Apache default file found.
+ 7499 requests: 0 error(s) and 6 item(s) reported on remote host
+ End Time:           2019-09-13 22:40:01 (GMT-4) (15 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```
