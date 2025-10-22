---
id: 3d7a67e1-d507-43f2-8bb2-3a73724cc7aa
name: masscan portscan list of ips
type: command
executor: bash
data: masscan -iL $_IPS_FILE --rate $_RATE -p$_LOW_PORT-$_HIGH_PORT -oL $_OUTPUT_FILE
output: "root@hacker:~/rs# masscan -iL ips-online.txt --rate 10000 -p80-80 -oL masscan.out\n\
  Starting masscan 1.0.5 (http://bit.ly/14GZzcT) at 2020-06-30 18:00:38 GMT\n -- forced\
  \ options: -sS -Pn -n --randomize-hosts -v --send-eth\nInitiating SYN Stealth Scan\n\
  Scanning 3 hosts [1 port/host]\n\n\nroot@hacker:~/rs# cat masscan.out \n#masscan\n\
  open tcp 80 104.XX.27.XX 1593540039\nopen tcp 80 172.XX.10.XX 1593540039\nopen tcp\
  \ 80 104.XX.26.XX 1593540039\n# end"
created_at: '2020-06-30T18:05:36.049153+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# masscan portscan list of ips

```bash
masscan -iL $_IPS_FILE --rate $_RATE -p$_LOW_PORT-$_HIGH_PORT -oL $_OUTPUT_FILE
```

## Expected Output

```
root@hacker:~/rs# masscan -iL ips-online.txt --rate 10000 -p80-80 -oL masscan.out
Starting masscan 1.0.5 (http://bit.ly/14GZzcT) at 2020-06-30 18:00:38 GMT
 -- forced options: -sS -Pn -n --randomize-hosts -v --send-eth
Initiating SYN Stealth Scan
Scanning 3 hosts [1 port/host]

root@hacker:~/rs# cat masscan.out 
#masscan
open tcp 80 104.XX.27.XX 1593540039
open tcp 80 172.XX.10.XX 1593540039
open tcp 80 104.XX.26.XX 1593540039
# end
```
