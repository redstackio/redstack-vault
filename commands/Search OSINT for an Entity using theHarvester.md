---
id: 6d0c3d49-cc9d-4cc0-b55c-043ea5ceef80
name: Search OSINT for an Entity using theHarvester
type: command
executor: bash
data: theHarvester -d $_DOMAIN -l 50 -b google -f $_OUTPUT.txt
output: "theHarvester -d cisco.com -l 50 -b google -f results.txt   \n\n*******************************************************************\n\
  *                                                                 *\n* | |_| |__\
  \   ___    /\\  /\\__ _ _ ____   _____  ___| |_ ___ _ __  *\n* | __| '_ \\ / _ \\\
  \  / /_/ / _` | '__\\ \\ / / _ \\/ __| __/ _ \\ '__| *\n* | |_| | | |  __/ / __\
  \  / (_| | |   \\ V /  __/\\__ \\ ||  __/ |    *\n*  \\__|_| |_|\\___| \\/ /_/ \\\
  __,_|_|    \\_/ \\___||___/\\__\\___|_|    *\n*                                \
  \                                 *\n* theHarvester Ver. 3.0.6                 \
  \                        *\n* Coded by Christian Martorella                    \
  \               *\n* Edge-Security Research                                    \
  \      *\n* cmartorella@edge-security.com                                   *\n\
  *******************************************************************\n\n\nfound supported\
  \ engines\n[-] Starting harvesting process for domain: cisco.com\n\n[-] Searching\
  \ in Google:\n        Searching 0 results...\n\nHarvesting results\nNo IP addresses\
  \ found\n\n\n[+] Emails found:\n------------------\nbeerswithtalos@cisco.com\n \n\
  [+] Hosts found in search engines:\n------------------------------------\n\nTotal\
  \ hosts: 4\n\n[-] Resolving hostnames IPs... \n \nnewsroom.cisco.com:173.36.124.49\n\
  sleepytime.cisco.com:empty\ntools.cisco.com:72.163.4.38\nwww.cisco.com:23.49.134.110\n\
  NEW REPORTING BEGINS:\nNEW REPORTING FINISHED!\n[+] Saving files...\nFiles saved!\n"
created_at: '2019-09-11T23:44:59.284519+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Search OSINT for an Entity using theHarvester

```bash
theHarvester -d $_DOMAIN -l 50 -b google -f $_OUTPUT.txt
```

## Expected Output

```
theHarvester -d cisco.com -l 50 -b google -f results.txt   

*******************************************************************
*                                                                 *
* | |_| |__   ___    /\  /\__ _ _ ____   _____  ___| |_ ___ _ __  *
* | __| '_ \ / _ \  / /_/ / _` | '__\ \ / / _ \/ __| __/ _ \ '__| *
* | |_| | | |  __/ / __  / (_| | |   \ V /  __/\__ \ ||  __/ |    *
*  \__|_| |_|\___| \/ /_/ \__,_|_|    \_/ \___||___/\__\___|_|    *
*                                                                 *
* theHarvester Ver. 3.0.6                                         *
* Coded by Christian Martorella                                   *
* Edge-Security Research                                          *
* cmartorella@edge-security.com                                   *
*******************************************************************


found supported engines
[-] Starting harvesting process for domain: cisco.com

[-] Searching in Google:
        Searching 0 results...

Harvesting results
No IP addresses found


[+] Emails found:
------------------
beerswithtalos@cisco.com
 
[+] Hosts found in search engines:
------------------------------------

Total hosts: 4

[-] Resolving hostnames IPs... 
 
newsroom.cisco.com:173.36.124.49
sleepytime.cisco.com:empty
tools.cisco.com:72.163.4.38
www.cisco.com:23.49.134.110
NEW REPORTING BEGINS:
NEW REPORTING FINISHED!
[+] Saving files...
Files saved!

```


