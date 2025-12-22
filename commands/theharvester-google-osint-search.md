---
type: command
executor: bash
data: theHarvester -d $_DOMAIN -l 50 -b google -f $_OUTPUT_FILE
output: |
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
platforms:
  - Linux
tags:
  - osint
  - reconnaissance
verified: true
validated: true
---

# theharvester-google-osint-search

## Command

```bash
theHarvester -d $_DOMAIN -l 50 -b google -f $_OUTPUT_FILE
```

## Description

This command uses theHarvester to perform an OSINT search on Google for a target domain, limiting to 50 results and saving output to an XML file. It gathers emails, hosts, and related public data passively.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain to search (e.g., cisco.com) | Yes |
| -l 50 | Limit number of results from each source | No (default 500) |
| -b google | Backend search engine to use | Yes |
| -f $_OUTPUT_FILE | Output filename for XML report (e.g., results.txt) | Yes |

## Examples

### Basic Usage

```bash
theHarvester -d example.com -l 50 -b google -f osint_results.txt
```

### Advanced Usage

```bash
theHarvester -d example.com -l 100 -b google -f detailed_results.txt --timeout 10
```

## Expected Output

Console shows progress and summary, with results saved to file. Example for cisco.com:

```
*******************************************************************
*                                                                 *
* | |_| |__   ___    /\/ /\__ _ _ ____   _____  ___| |_ ___ _ __  *
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

The XML file contains structured data for parsing.

## Related

- [[tools/theHarvester]]
