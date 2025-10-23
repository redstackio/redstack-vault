---
id: 6e9efe16-04dc-4b3a-ae5e-970fff6b7a4d
name: Enumerate a Web CMS for Usernames and Passwords
type: procedure
verified: true
submitted: true
created_at: '2019-10-09T18:38:08.566896+00:00'
updated_at: '2023-05-26T18:35:53.258433+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
tags:
- '[[authentication]]'
- '[[Cryptography]]'
- '[[Network]]'
commands:
- '[[CEWL Generate a Password List Using a Website''s Content]]'
- '[[Crawl a Web App Recursively]]'
- '[[Grep Search Files for Keywords]]'
- '[[Mutate a Wordlist with Alphanumeric and Special Characters]]'
- '[[WPScan Enumerate WordPress Plugins, Users, Themes and TimThumb]]'
---

# Enumerate a Web CMS for Usernames and Passwords

**Status**: ✓ Verified

## Summary

Many websites reveal usernames and potential passwords in the pages themselves, hidden files, and configuration files. By enumerating a site's content with tools, username and password lists can be generated and used for login brute forcing. 

## Description

# Description

Many websites reveal usernames and potential passwords in the pages themselves, hidden files, and configuration files. By enumerating a site's content with tools, username and password lists can be generated and used for login brute forcing.



# Instructions

1. Recursively download files and folders from a website.





**Command** ([[Crawl a Web App Recursively]]):

```bash
wget --recursive --html-extension --convert-links --restrict-file-names=windows --no-parent http://$_TARGET_IP
```





2. Search the downloaded content for interesting keywords.





**Command** ([[Grep Search Files for Keywords]]):

```bash
grep -C 5 -iR '$_WORD1\|$_WORD2' *
```





3. Generate a password list based on words found on the web app.





**Command** ([[CEWL Generate a Password List Using a Website's Content]]):

```bash
cewl $_TARGET_IP -d $_DEPTH -m $_MAX_SIZE -w $_WORDLIST
```







4. Mutate the password list. In this example, two characters are appended using `?a?a`. For more options, see hashcat's mask documentation[: https://hashcat.net/wiki/doku.php?id=mask_atta](https://hashcat.net/wiki/doku.php?id=mask_attack)ck





**Command** ([[Mutate a Wordlist with Alphanumeric and Special Characters]]):

```bash
hashcat -a 6 --stdout $_WORDLIST ?a?a > $_WORDLIST.mutated
```





5. Identify Potential Usernames



Web apps often disclose usernames in the site's content and code.



Common places to find usernames:

- Footers and Headers

- Blog posts authors and comments

- In the source (HTML, JS, PHP, etc)

If the site uses WordPress, users can enumerate users, plugins, and themes with WpScan





**Command** ([[WPScan Enumerate WordPress Plugins, Users, Themes and TimThumb]]):

```bash
wpscan --url http://$_TARGET_IP --enumerate p,t,u,tt
```



Use the generated wordlists to brute force user/pass combinations in the web app.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]
- [[File and Directory Discovery|T1083 - File and Directory Discovery]]

## Commands Used

- [[CEWL Generate a Password List Using a Website's Content]]
- [[Crawl a Web App Recursively]]
- [[Grep Search Files for Keywords]]
- [[Mutate a Wordlist with Alphanumeric and Special Characters]]
- [[WPScan Enumerate WordPress Plugins, Users, Themes and TimThumb]]

## Tags

- [[authentication]]
- [[Cryptography]]
- [[Network]]


