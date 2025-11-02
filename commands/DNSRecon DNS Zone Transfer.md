---
id: 86aa5503-6bb7-4536-84c2-edb089b20150
name: DNSRecon DNS Zone Transfer
type: command
executor: bash
data: dnsrecon -d $_TARGET_DOMAIN -t axfr
output: 'root@kali:~# dnsrecon -d testsite.com -t axfr

  [*] Testing NS Servers for Zone Transfer

  [*] Checking for Zone Transfer for testsite.com name servers

  [*] Resolving SOA Record

  [+]      SOA nsztm1.testsite.com 192.178.50.100

  [*] Resolving NS Records

  [*] NS Servers found:

  [*]     NS nsztm1.testsite.com 192.178.50.101

  [*]     NS nsztm2.testsite.com 192.178.50.102

  [*] Removing any duplicate NS server IP Addresses...

  [*]

  [*] Trying NS server 192.178.50.101

  [+] 192.178.50.101 Has port 53 TCP Open

  [+] Zone Transfer was successful!!

  [*]      SOA nsztm1.testsite.com 192.178.50.101

  [*]      NS nsztm1.testsite.com 192.178.50.101

  [*]      SRV _sip._tcp.testsite.com www 5060 0 no_ip

  [*]      HINFO Casio fx-700G Windows XP

  [*]      RP robin robinwood

  [*]      AFSDB 1 asfdbbox

  [*]      AFSDB 1 asfdbbox

  [*]      LOC 53 20 56.558 N 1 38 33.526 W 0.00m

  [*]      NAPTR P 2 3 !^.*$!sip:customer-service@testsite.com! . E2U+sip

  [*]      NAPTR P 1 1  email.testsite.com E2U+email'
created_at: '2019-09-20T18:53:20.010961+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[DNSRecon]]'
---

# DNSRecon DNS Zone Transfer

```bash
dnsrecon -d $_TARGET_DOMAIN -t axfr
```

## Expected Output

```
root@kali:~# dnsrecon -d testsite.com -t axfr
[*] Testing NS Servers for Zone Transfer
[*] Checking for Zone Transfer for testsite.com name servers
[*] Resolving SOA Record
[+]      SOA nsztm1.testsite.com 192.178.50.100
[*] Resolving NS Records
[*] NS Servers found:
[*]     NS nsztm1.testsite.com 192.178.50.101
[*]     NS nsztm2.testsite.com 192.178.50.102
[*] Removing any duplicate NS server IP Addresses...
[*]
[*] Trying NS server 192.178.50.101
[+] 192.178.50.101 Has port 53 TCP Open
[+] Zone Transfer was successful!!
[*]      SOA nsztm1.testsite.com 192.178.50.101
[*]      NS nsztm1.testsite.com 192.178.50.101
[*]      SRV _sip._tcp.testsite.com www 5060 0 no_ip
[*]      HINFO Casio fx-700G Windows XP
[*]      RP robin robinwood
[*]      AFSDB 1 asfdbbox
[*]      AFSDB 1 asfdbbox
[*]      LOC 53 20 56.558 N 1 38 33.526 W 0.00m
[*]      NAPTR P 2 3 !^.*$!sip:customer-service@testsite.com! . E2U+sip
[*]      NAPTR P 1 1  email.testsite.com E2U+email
```


