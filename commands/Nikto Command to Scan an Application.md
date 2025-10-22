---
id: f3d7ceb0-63a8-4dd4-823e-dfd206e244f3
name: Nikto Command to Scan an Application
type: command
executor: ''
data: nikto -h http://192.168.43.68/vcart/login.php
output: "- Nikto v2.1.6\n---------------------------------------------------------------------------\n\
  + Target IP:          192.168.43.68\n+ Target Hostname:    192.168.43.68\n+ Target\
  \ Port:        80\n+ Start Time:         2020-08-19 21:29:09 (GMT5.5)\n---------------------------------------------------------------------------\n\
  + Server: Apache/2.4.41 (Unix) OpenSSL/1.1.1d PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3\n\
  + Retrieved x-powered-by header: PHP/7.1.32\n+ The anti-clickjacking X-Frame-Options\
  \ header is not present.\n+ The X-XSS-Protection header is not defined. This header\
  \ can hint to the user agent to protect against some forms of XSS\n+ The X-Content-Type-Options\
  \ header is not set. This could allow the user agent to render the content of the\
  \ site in a different fashion to the MIME type\n+ No CGI Directories found (use\
  \ '-C all' to force check all possible dirs)\n+ Allowed HTTP Methods: OPTIONS, HEAD,\
  \ GET, POST, TRACE \n+ Web Server returns a valid response with junk HTTP methods,\
  \ this may cause false positives.\n+ OSVDB-877: HTTP TRACE method is active, suggesting\
  \ the host is vulnerable to XST\n+ OSVDB-44056: /vcart/login.php/sips/sipssys/users/a/admin/user:\
  \ SIPS v0.2.2 allows user account info (including password) to be retrieved remotely.\n\
  + 7539 requests: 0 error(s) and 8 item(s) reported on remote host\n+ End Time: \
  \          2020-08-19 21:29:39 (GMT5.5) (30 seconds)\n---------------------------------------------------------------------------\n\
  + 1 host(s) tested\n\n"
created_at: '2020-08-19T16:08:58.983461+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Nikto Command to Scan an Application

```bash
nikto -h http://192.168.43.68/vcart/login.php
```

## Expected Output

```
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          192.168.43.68
+ Target Hostname:    192.168.43.68
+ Target Port:        80
+ Start Time:         2020-08-19 21:29:09 (GMT5.5)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Unix) OpenSSL/1.1.1d PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3
+ Retrieved x-powered-by header: PHP/7.1.32
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: OPTIONS, HEAD, GET, POST, TRACE 
+ Web Server returns a valid response with junk HTTP methods, this may cause false positives.
+ OSVDB-877: HTTP TRACE method is active, suggesting the host is vulnerable to XST
+ OSVDB-44056: /vcart/login.php/sips/sipssys/users/a/admin/user: SIPS v0.2.2 allows user account info (including password) to be retrieved remotely.
+ 7539 requests: 0 error(s) and 8 item(s) reported on remote host
+ End Time:           2020-08-19 21:29:39 (GMT5.5) (30 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```
