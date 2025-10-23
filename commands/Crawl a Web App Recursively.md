---
id: dc7a7074-a036-4c7b-b8b8-e282ffae95ce
name: Crawl a Web App Recursively
type: command
executor: bash
data: wget --recursive --html-extension --convert-links --restrict-file-names=windows
  --no-parent http://$_TARGET_IP
output: "root@kali:~# wget --recursive --html-extension --convert-links --restrict-file-names=windows\
  \ --no-parent http://10.10.10.10/\n\n--2019-10-09 14:23:57--  http://10.10.10.10/\
  \  \nConnecting to 10.10.10.10:80... connected.    \nHTTP request sent, awaiting\
  \ response... 200 OK\nLength: 8028 (7.8K) [text/html]                          \
  \                                                                              \
  \               \nSaving to: ‘10.10.10.10/index.html’\n\n10.10.10.10/index.html\
  \               100%[==============>]   7.84K  --.-KB/s    in 0.002s \n        \
  \                                                                              \
  \                                                                \n2019-10-09 14:23:57\
  \ (4.83 MB/s) - ‘10.10.10.10/index.html’ saved [8028/8028]        \n...\n...\nFINISHED\
  \ --2019-10-09 14:24:24--\nTotal wall clock time: 7.5s\nDownloaded: 85 files, 2.2M\
  \ in 1.0s (2.12 MB/s)\nConverting links in 10.10.10.10/index.html... 40-0\nConverting\
  \ links in 10.10.10.10/gallery.html... 127-0\nConverting links in 10.10.10.10/css/style.css...\
  \ 70-0\nConverted links in 3 files in 0.002 seconds."
created_at: '2019-10-09T18:38:08.462994+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Crawl a Web App Recursively

```bash
wget --recursive --html-extension --convert-links --restrict-file-names=windows --no-parent http://$_TARGET_IP
```

## Expected Output

```
root@kali:~# wget --recursive --html-extension --convert-links --restrict-file-names=windows --no-parent http://10.10.10.10/

--2019-10-09 14:23:57--  http://10.10.10.10/  
Connecting to 10.10.10.10:80... connected.    
HTTP request sent, awaiting response... 200 OK
Length: 8028 (7.8K) [text/html]                                                                                                                       
Saving to: ‘10.10.10.10/index.html’

10.10.10.10/index.html               100%[==============>]   7.84K  --.-KB/s    in 0.002s 
                                                                                                                                                      
2019-10-09 14:23:57 (4.83 MB/s) - ‘10.10.10.10/index.html’ saved [8028/8028]        
...
...
FINISHED --2019-10-09 14:24:24--
Total wall clock time: 7.5s
Downloaded: 85 files, 2.2M in 1.0s (2.12 MB/s)
Converting links in 10.10.10.10/index.html... 40-0
Converting links in 10.10.10.10/gallery.html... 127-0
Converting links in 10.10.10.10/css/style.css... 70-0
Converted links in 3 files in 0.002 seconds.
```


