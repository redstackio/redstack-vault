---
id: 89ed8f32-a9f4-44d7-ab34-36779f3959dc
name: wifi cheatsheet
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:34.169339+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# wifi cheatsheet



**Command** ([[wget a an entire file]]):

```bash
wget --limit-rate=200k --no-clobber --convert-links --random-wait -r -p -E -e robots=off -U mozilla [url]

```







**Command** ([[status your devices]]):

```bash
airmon-ng

```







**Command** ([[kill wpa stuff which i guess conflicts, kills all wlan*]]):

```bash
airmon-ng check kill

```







**Command** ([[put your device in monitor mode]]):

```bash
airmon-ng start wlan1

```







**Command** ([[verify you have a monitor mode device]]):

```bash
ifconfig

```







**Command** ([[dump some probs]]):

```bash
airodump-ng wlan1mon -w logfile --beacons

```







**Command** ([[see just the client beacons]]):

```bash
cat sb2-01.csv| cut -d',' -f7 | sort

```







**Command** ([[stop monitor mode]]):

```bash
airmon-ng stop wlan1mon

```






