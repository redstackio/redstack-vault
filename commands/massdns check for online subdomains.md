---
id: 56cd5503-4f77-4ef3-864e-f71867945566
name: massdns check for online subdomains
type: command
executor: ''
data: massdns -r $_DNS_RESOLVERS -t A -o S -w $_OUTPUT_FILE $_HOST_WORDLIST
output: "root@hacker:~# massdns -r resolvers.txt -t A -o S -w massdns.out hosts-wordlist.txt\n\
  Processed queries: 19983\nReceived packets: 15164\nProgress: 100.00% (00 h 00 min\
  \ 03 sec / 00 h 00 min 03 sec)\nCurrent incoming rate: 5059 pps, average: 5040 pps\n\
  Current success rate: 4535 pps, average: 4716 pps\nFinished total: 14187, success:\
  \ 14187 (100.00%)\nMismatched domains: 927 (6.11%), IDs: 50 (0.33%)\nFailures: 0:\
  \ 46.20%, 1: 24.38%, 2: 16.76%, 3: 12.04%, 4: 9.64%, 5: 31.74%, 6: 0.00%, 7: 0.00%,\
  \ 8: 0.00%, 9: 0.00%, 10: 0.00%, 11: 0.00%, 12: 0.00%, 13: 0.00%, 14: 0.00%, 15:\
  \ 0.00%, 16: 0.00%, 17: 0.00%, 18: 0.00%, 19: 0.00%, 20: 0.00%, 21: 0.00%, 22: 0.00%,\
  \ 23: 0.00%, 24: 0.00%, 25: 0.00%, 26: 0.00%, 27: 0.00%, 28: 0.00%, 29: 0.00%, 30:\
  \ 0.00%, 31: 0.00%, 32: 0.00%, 33: 0.00%, 34: 0.00%, 35: 0.00%, 36: 0.00%, 37: 0.00%,\
  \ 38: 0.00%, 39: 0.00%, 40: 0.00%, 41: 0.00%, 42: 0.00%, 43: 0.00%, 44: 0.00%, 45:\
  \ 0.00%, 46: 0.00%, 47: 0.00%, 48: 0.00%, 49: 0.00%, 50: 0.00%, \nResponse: | Success:\
  \               | Total:\nOK:       |           16 (  0.11%) |           17 (  0.11%)\n\
  NXDOMAIN: |        14171 ( 99.89%) |        15147 ( 99.89%)\nSERVFAIL: |       \
  \     0 (  0.00%) |            0 (  0.00%)\nREFUSED:  |            0 (  0.00%) |\
  \            0 (  0.00%)\nFORMERR:  |            0 (  0.00%) |            0 (  0.00%)"
created_at: '2020-06-30T05:00:10.524058+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# massdns check for online subdomains

```bash
massdns -r $_DNS_RESOLVERS -t A -o S -w $_OUTPUT_FILE $_HOST_WORDLIST
```

## Expected Output

```
root@hacker:~# massdns -r resolvers.txt -t A -o S -w massdns.out hosts-wordlist.txt
Processed queries: 19983
Received packets: 15164
Progress: 100.00% (00 h 00 min 03 sec / 00 h 00 min 03 sec)
Current incoming rate: 5059 pps, average: 5040 pps
Current success rate: 4535 pps, average: 4716 pps
Finished total: 14187, success: 14187 (100.00%)
Mismatched domains: 927 (6.11%), IDs: 50 (0.33%)
Failures: 0: 46.20%, 1: 24.38%, 2: 16.76%, 3: 12.04%, 4: 9.64%, 5: 31.74%, 6: 0.00%, 7: 0.00%, 8: 0.00%, 9: 0.00%, 10: 0.00%, 11: 0.00%, 12: 0.00%, 13: 0.00%, 14: 0.00%, 15: 0.00%, 16: 0.00%, 17: 0.00%, 18: 0.00%, 19: 0.00%, 20: 0.00%, 21: 0.00%, 22: 0.00%, 23: 0.00%, 24: 0.00%, 25: 0.00%, 26: 0.00%, 27: 0.00%, 28: 0.00%, 29: 0.00%, 30: 0.00%, 31: 0.00%, 32: 0.00%, 33: 0.00%, 34: 0.00%, 35: 0.00%, 36: 0.00%, 37: 0.00%, 38: 0.00%, 39: 0.00%, 40: 0.00%, 41: 0.00%, 42: 0.00%, 43: 0.00%, 44: 0.00%, 45: 0.00%, 46: 0.00%, 47: 0.00%, 48: 0.00%, 49: 0.00%, 50: 0.00%, 
Response: | Success:               | Total:
OK:       |           16 (  0.11%) |           17 (  0.11%)
NXDOMAIN: |        14171 ( 99.89%) |        15147 ( 99.89%)
SERVFAIL: |            0 (  0.00%) |            0 (  0.00%)
REFUSED:  |            0 (  0.00%) |            0 (  0.00%)
FORMERR:  |            0 (  0.00%) |            0 (  0.00%)
```


