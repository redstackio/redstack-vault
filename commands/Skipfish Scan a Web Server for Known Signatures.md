---
id: 93d6310f-1dd7-43e3-8862-ea857b29c071
name: Skipfish Scan a Web Server for Known Signatures
type: command
executor: bash
data: skipfish -m 5 -o results -LY -S /usr/share/skipfish/dictionaries/complete.wl
  http://$_TARGET_IP
output: "root@kali:~# skipfish -m 5 -o results -LY -S /usr/share/skipfish/dictionaries/complete.wl\
  \ http://10.10.10.10\n\nWelcome to skipfish. Here are some useful tips:\n\n1) To\
  \ abort the scan at any time, press Ctrl-C. A partial report will be written\n \
  \  to the specified location. To view a list of currently scanned URLs, you can\n\
  \   press space at any time during the scan.\n\n2) Watch the number requests per\
  \ second shown on the main screen. If this figure\n   drops below 100-200, the scan\
  \ will likely take a very long time.\n\n3) The scanner does not auto-limit the scope\
  \ of the scan; on complex sites, you\n   may need to specify locations to exclude,\
  \ or limit brute-force steps.\n\n4) There are several new releases of the scanner\
  \ every month. If you run into\n   trouble, check for a newer version first, let\
  \ the author know next.\n\nMore info: http://code.google.com/p/skipfish/wiki/KnownIssues\n\
  \nPress any key to continue (or wait 60 seconds)... \n\nskipfish version 2.10b by\
  \ lcamtuf@google.com\n\n  - 10.10.10.10 -\n\nScan statistics:\n\n      Scan time\
  \ : 0:00:56.394\n  HTTP requests : 121816 (2160.0/s), 58613 kB in, 23370 kB out\
  \ (1453.7 kB/s)  \n    Compression : 96 kB in, 690 kB out (75.5% gain)    \n   \
  \ HTTP faults : 0 net errors, 0 proto errors, 0 retried, 0 drops\n TCP handshakes\
  \ : 1376 total (88.5 req/conn)  \n     TCP faults : 0 failures, 0 timeouts, 12 purged\n\
  \ External links : 52 skipped\n   Reqs pending : 0           \n\nDatabase statistics:\n\
  \n         Pivots : 277 total, 277 done (100.00%)    \n    In progress : 0 pending,\
  \ 0 init, 0 attacks, 0 dict       \n  Missing nodes : 12 spotted\n     Node types\
  \ : 1 serv, 19 dir, 253 file, 0 pinfo, 4 unkn, 0 par, 0 valll\n   Issues found :\
  \ 46 info, 0 warn, 0 low, 0 medium, 0 high impact\n      Dict size : 2215 words\
  \ (0 new), 109 extensions, 0 candidates\n     Signatures : 77 total\n        \n\
  [+] Copying static resources...\n[+] Sorting and annotating crawl nodes: 277\n[+]\
  \ Looking for duplicate entries: 277\n[+] Counting unique nodes: 44\n[+] Saving\
  \ pivot data for third-party tools...\n[+] Writing scan description...\n[+] Writing\
  \ crawl tree: 277\n[+] Generating summary views...\n[+] Report saved to 'results/index.html'\
  \ [0x7a2d8863].\n[+] This was a great day for science!"
created_at: '2019-09-14T05:30:22.077322+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Skipfish Scan a Web Server for Known Signatures

```bash
skipfish -m 5 -o results -LY -S /usr/share/skipfish/dictionaries/complete.wl http://$_TARGET_IP
```

## Expected Output

```
root@kali:~# skipfish -m 5 -o results -LY -S /usr/share/skipfish/dictionaries/complete.wl http://10.10.10.10

Welcome to skipfish. Here are some useful tips:

1) To abort the scan at any time, press Ctrl-C. A partial report will be written
   to the specified location. To view a list of currently scanned URLs, you can
   press space at any time during the scan.

2) Watch the number requests per second shown on the main screen. If this figure
   drops below 100-200, the scan will likely take a very long time.

3) The scanner does not auto-limit the scope of the scan; on complex sites, you
   may need to specify locations to exclude, or limit brute-force steps.

4) There are several new releases of the scanner every month. If you run into
   trouble, check for a newer version first, let the author know next.

More info: http://code.google.com/p/skipfish/wiki/KnownIssues

Press any key to continue (or wait 60 seconds)... 

skipfish version 2.10b by lcamtuf@google.com

  - 10.10.10.10 -

Scan statistics:

      Scan time : 0:00:56.394
  HTTP requests : 121816 (2160.0/s), 58613 kB in, 23370 kB out (1453.7 kB/s)  
    Compression : 96 kB in, 690 kB out (75.5% gain)    
    HTTP faults : 0 net errors, 0 proto errors, 0 retried, 0 drops
 TCP handshakes : 1376 total (88.5 req/conn)  
     TCP faults : 0 failures, 0 timeouts, 12 purged
 External links : 52 skipped
   Reqs pending : 0           

Database statistics:

         Pivots : 277 total, 277 done (100.00%)    
    In progress : 0 pending, 0 init, 0 attacks, 0 dict       
  Missing nodes : 12 spotted
     Node types : 1 serv, 19 dir, 253 file, 0 pinfo, 4 unkn, 0 par, 0 valll
   Issues found : 46 info, 0 warn, 0 low, 0 medium, 0 high impact
      Dict size : 2215 words (0 new), 109 extensions, 0 candidates
     Signatures : 77 total
        
[+] Copying static resources...
[+] Sorting and annotating crawl nodes: 277
[+] Looking for duplicate entries: 277
[+] Counting unique nodes: 44
[+] Saving pivot data for third-party tools...
[+] Writing scan description...
[+] Writing crawl tree: 277
[+] Generating summary views...
[+] Report saved to 'results/index.html' [0x7a2d8863].
[+] This was a great day for science!
```


