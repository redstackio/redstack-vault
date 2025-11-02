---
id: ea246435-e5d3-4c05-a1b7-f364dacfe2a0
name: amass enumerate company properties
type: command
executor: ''
data: amass intel -org $_COMPANY_NAME
output: 'root@kali ~# amass intel -org google

  6432, GOOGLE-FIBER - Google Fiber Inc.

  15169, GOOGLE - Google LLC

  16550, GOOGLE-PRIVATE-CLOUD - Google LLC

  16591, GOOGLE-FIBER - Google Fiber Inc.

  19448, GOOGLE-FIBER - Google Fiber Inc.

  19527, GOOGLE-2 - Google LLC

  22577, ADMOB-US - Google LLC

  22859, GOOGLE - Google LLC

  24424, CNNIC-GOOGLECN-AP Beijing Gu Xiang Information Technology Co.

  26684, AS-MEEBO - Google LLC

  26910, LINKUS - Google Access LLC

  36039, GOOGLE - Google LLC

  36040, YOUTUBE - Google LLC

  36384, GOOGLE-IT - Google LLC

  36385, GOOGLE-IT - Google LLC

  36492, GOOGLEWIFI - Google

  36987, google-as

  40873, AS-METAWEB-2 - Google LLC

  41264, GOOGLE-IT-RO-ISP

  45566, GOOGLE-CORP-APAC-AS-AP AS number for Google Corporate Network in APAC

  394507, GOOGLE - Google LLC

  394639, GOOGLE - Google LLC

  394699, GOOGLE-ACCESS-NYC - Google Access LLC

  395973, GOOGLE-2 - Google LLC

  396982, GOOGLE-PRIVATE-CLOUD - Google LLC

  '
created_at: '2020-06-29T16:27:45.186511+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[amass]]'
---

# amass enumerate company properties

```bash
amass intel -org $_COMPANY_NAME
```

## Expected Output

```
root@kali ~# amass intel -org google
6432, GOOGLE-FIBER - Google Fiber Inc.
15169, GOOGLE - Google LLC
16550, GOOGLE-PRIVATE-CLOUD - Google LLC
16591, GOOGLE-FIBER - Google Fiber Inc.
19448, GOOGLE-FIBER - Google Fiber Inc.
19527, GOOGLE-2 - Google LLC
22577, ADMOB-US - Google LLC
22859, GOOGLE - Google LLC
24424, CNNIC-GOOGLECN-AP Beijing Gu Xiang Information Technology Co.
26684, AS-MEEBO - Google LLC
26910, LINKUS - Google Access LLC
36039, GOOGLE - Google LLC
36040, YOUTUBE - Google LLC
36384, GOOGLE-IT - Google LLC
36385, GOOGLE-IT - Google LLC
36492, GOOGLEWIFI - Google
36987, google-as
40873, AS-METAWEB-2 - Google LLC
41264, GOOGLE-IT-RO-ISP
45566, GOOGLE-CORP-APAC-AS-AP AS number for Google Corporate Network in APAC
394507, GOOGLE - Google LLC
394639, GOOGLE - Google LLC
394699, GOOGLE-ACCESS-NYC - Google Access LLC
395973, GOOGLE-2 - Google LLC
396982, GOOGLE-PRIVATE-CLOUD - Google LLC

```


