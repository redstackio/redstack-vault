---
id: 2be10a40-866c-4b93-8977-a6e8cb6e7164
name: Nikto Enumerate Web Server with Burp Proxy
type: command
executor: bash
data: nikto -host http://$_TARGET_IP -useproxy 127.0.0.1:8080
output: "root@kali:~# nikto -host http://10.10.10.10 -useproxy 127.0.0.1:8080\n- Nikto\
  \ v2.1.6\n---------------------------------------------------------------------------\n\
  + Target IP:          10.10.10.10\n+ Target Hostname:    10.10.10.10\n+ Target Port:\
  \        80\n+ Proxy:              127.0.0.1:8080\n+ Start Time:         2019-09-14\
  \ 00:01:21 (GMT-4)\n---------------------------------------------------------------------------\n\
  + Server: Apache/2.4.29 (Ubuntu)\n+ Server leaks inodes via ETags, header found\
  \ with file /, fields: 0x2aa6 0x59277789d6649 \n+ The anti-clickjacking X-Frame-Options\
  \ header is not present.\n+ The X-XSS-Protection header is not defined. This header\
  \ can hint to the user agent to protect against some forms of XSS\n+ The X-Content-Type-Options\
  \ header is not set. This could allow the user agent to render the content of the\
  \ site in a different fashion to the MIME type\n+ No CGI Directories found (use\
  \ '-C all' to force check all possible dirs)\n+ Allowed HTTP Methods: GET, POST,\
  \ OPTIONS, HEAD (May be proxy's methods, not server's)\n+ OSVDB-3092: /_vti_bin/_vti_aut/author.dll?method=list+documents%3a3%2e0%2e2%2e1706&service%5fname=&listHiddenDocs=true&listExplorerDocs=true&listRecurse=false&listFiles=true&listFolders=true&listLinkInfo=true&listIncludeParent=true&listDerivedT=false&listBorders=false:\
  \ We seem to have authoring access to the FrontPage web.\n+ OSVDB-3092: /_vti_bin/_vti_aut/author.exe?method=list+documents%3a3%2e0%2e2%2e1706&service%5fname=&listHiddenDocs=true&listExplorerDocs=true&listRecurse=false&listFiles=true&listFolders=true&listLinkInfo=true&listIncludeParent=true&listDerivedT=false&listBorders=false:\
  \ We seem to have authoring access to the FrontPage web.\n+ OSVDB-3233: /icons/README:\
  \ Apache default file found.\n+ 7502 requests: 2 error(s) and 8 item(s) reported\
  \ on remote host\n+ End Time:           2019-09-14 00:20:39 (GMT-4) (1158 seconds)\n\
  ---------------------------------------------------------------------------\n+ 1\
  \ host(s) tested"
created_at: '2019-09-14T05:30:22.071354+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Nikto Enumerate Web Server with Burp Proxy

```bash
nikto -host http://$_TARGET_IP -useproxy 127.0.0.1:8080
```

## Expected Output

```
root@kali:~# nikto -host http://10.10.10.10 -useproxy 127.0.0.1:8080
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.10.10
+ Target Hostname:    10.10.10.10
+ Target Port:        80
+ Proxy:              127.0.0.1:8080
+ Start Time:         2019-09-14 00:01:21 (GMT-4)
---------------------------------------------------------------------------
+ Server: Apache/2.4.29 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, fields: 0x2aa6 0x59277789d6649 
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: GET, POST, OPTIONS, HEAD (May be proxy's methods, not server's)
+ OSVDB-3092: /_vti_bin/_vti_aut/author.dll?method=list+documents%3a3%2e0%2e2%2e1706&service%5fname=&listHiddenDocs=true&listExplorerDocs=true&listRecurse=false&listFiles=true&listFolders=true&listLinkInfo=true&listIncludeParent=true&listDerivedT=false&listBorders=false: We seem to have authoring access to the FrontPage web.
+ OSVDB-3092: /_vti_bin/_vti_aut/author.exe?method=list+documents%3a3%2e0%2e2%2e1706&service%5fname=&listHiddenDocs=true&listExplorerDocs=true&listRecurse=false&listFiles=true&listFolders=true&listLinkInfo=true&listIncludeParent=true&listDerivedT=false&listBorders=false: We seem to have authoring access to the FrontPage web.
+ OSVDB-3233: /icons/README: Apache default file found.
+ 7502 requests: 2 error(s) and 8 item(s) reported on remote host
+ End Time:           2019-09-14 00:20:39 (GMT-4) (1158 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```


