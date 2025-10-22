---
id: fbbe2a7f-290d-46ed-bde0-4026d913b542
name: GitLab Repository Enumeration and Search
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:25.155487+00:00'
updated_at: '2023-04-10T20:34:07.173940+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
- '[[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]'
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
tags:
- '[[Enumerate repositories files and secrets]]'
- '[[Source Code Management & CI/CD Compromise]]'
commands:
- '[[Add admin using API key]]'
- '[[Add admin using username and password]]'
- '[[Create Personal Access Token using API key for target user in GitLab]]'
- '[[Create Personal Access Token using username and password for target user in GitLab]]'
- '[[Create SSH Key with API Token]]'
- '[[Create SSH Key with Username and Password]]'
- '[[List GitLab snippets by API key]]'
- '[[List GitLab snippets by username and password]]'
- '[[List Personal Access Tokens using API key for target user in GitLab]]'
- '[[List Personal Access Tokens using username and password for target user in GitLab]]'
- '[[List repositories from GitLab using API key]]'
- '[[List repositories from GitLab using username and password]]'
- '[[List runners from GitLab using apikey]]'
- '[[List runners from GitLab using username and password]]'
- '[[List SSH Key with API Token]]'
- '[[List SSH Key with Username and Password]]'
- '[[Remove admin using username and password]]'
- '[[Remove Personal Access Token using username and password for patID in GitLab]]'
- '[[Remove SSH Key with API Token]]'
- '[[Remove SSH Key with Username and Password]]'
- '[[Search for ''some search term'' in GitHub using API key]]'
- '[[Search for ''some search term'' in GitHub using username and password]]'
- '[[Search for ''some search term'' using apikey in GitLab]]'
- '[[Search for ''some search term'' using username and password in GitLab]]'
- '[[Search GitHub for repositories containing ''some search term'']]'
- '[[Search GitLab for repositories containing ''some search term'']]'
---

# GitLab Repository Enumeration and Search

## Summary

GitLab Repository Enumeration and Search is a technique used by attackers to identify and extract sensitive information such as credentials, secrets, and other intellectual property stored in GitLab repositories. Attackers use various GitLab APIs and search functionalities to list repositories, sea

## Description

# Description

GitLab Repository Enumeration and Search is a technique used by attackers to identify and extract sensitive information such as credentials, secrets, and other intellectual property stored in GitLab repositories. Attackers use various GitLab APIs and search functionalities to list repositories, search for files, and identify secrets. This technique can be used to support other attack techniques such as lateral movement, privilege escalation, and data exfiltration. Organizations can use this technique to identify and remediate sensitive information stored in GitLab repositories.

## Requirements

1. Access to GitLab API

1. Valid authentication credentials

1. Access to GitLab repositories

## Defense

1. Implement access controls to limit access to sensitive information in GitLab repositories

1. Implement monitoring and alerting for suspicious activity such as excessive repository searches or file downloads

1. Regularly review and remove sensitive information stored in GitLab repositories

## Objectives

1. Identify sensitive information stored in GitLab repositories

1. Support other attack techniques such as lateral movement, privilege escalation, and data exfiltration

# Instructions

1. To list repositories in GitLab, use the following commands:

**Code**: [[SCMKit.exe -s gitlab -m listrepo -c userName:passw]]

> -s: Specifies the SCM system (in this case, GitLab).
-m: Specifies the method to be used (in this case, listrepo).
-c: Specifies the credentials to be used (either userName:password or apiKey).
-u: Specifies the URL of the GitLab instance.

Example usage:
SCMKit.exe -s gitlab -m listrepo -c userName:password -u https://gitlab.something.local
SCMKit.exe -s gitlab -m listrepo -c apiKey -u https://gitlab.something.local

Note: Replace 'userName', 'password', 'apiKey', and 'https://gitlab.something.local' with your own credentials and GitLab instance URL.

**Command** ([[List repositories from GitLab using username and password]]):

```bash
SCMKit.exe -s gitlab -m listrepo -c userName:password -u https://gitlab.something.local
```

**Command** ([[List repositories from GitLab using API key]]):

```bash
SCMKit.exe -s gitlab -m listrepo -c apiKey -u https://gitlab.something.local
```

2. To search for repositories in a specific SCM system, use the following command:

SCMKit.exe -s <SCM_SYSTEM> -m searchrepo -c <CREDENTIALS> -u <SCM_URL> -o <SEARCH_TERM>

Replace <SCM_SYSTEM> with the name of the SCM system you want to search (e.g. github or gitlab). Replace <CREDENTIALS> with the appropriate credentials for the SCM system (e.g. userName:password or apikey). Replace <SCM_URL> with the URL of the SCM system. Finally, replace <SEARCH_TERM> with the term you want to search for.

**Code**: [[SCMKit.exe -s github -m searchrepo -c userName:pas]]

> This command allows you to search for repositories in a specific SCM system. By specifying the SCM system, credentials, SCM URL, and search term, you can quickly find relevant repositories. This can be useful when trying to find a specific repository in a large SCM system or when trying to find repositories related to a specific topic.

**Command** ([[Search GitHub for repositories containing 'some search term']]):

```bash
SCMKit.exe -s github -m searchrepo -c userName:password -u https://github.something.local -o "some search term"
```

**Command** ([[Search GitLab for repositories containing 'some search term']]):

```bash
SCMKit.exe -s gitlab -m searchrepo -c apikey -u https://gitlab.something.local -o "some search term"
```

3. To use this command, replace the 'some search term' string with the keyword you want to search for. You will also need to replace the 'https://github.something.local' URL with the URL of the SCM system you want to search on. Additionally, you will need to replace the 'userName:password' or 'apikey' with the appropriate credentials for accessing the SCM system.

**Code**: [[SCMKit.exe -s github -m searchcode -c userName:pas]]

> This command uses the SCMKit tool to search for code containing a given keyword in a specific SCM system. The 's' parameter specifies the SCM system to use (in this case, 'github'), and the 'm' parameter specifies the search mode (in this case, 'searchcode'). The 'c' parameter is used to specify the authentication method (either 'userName:password' or 'apikey'), and the 'u' parameter is used to specify the URL of the SCM system to search on. The 'o' parameter is used to specify the search term (the keyword to search for).

**Command** ([[Search for 'some search term' in GitHub using username and password]]):

```bash
SCMKit.exe -s github -m searchcode -c userName:password -u https://github.something.local -o "some search term"
```

**Command** ([[Search for 'some search term' in GitHub using API key]]):

```bash
SCMKit.exe -s github -m searchcode -c apikey -u https://github.something.local -o "some search term"
```

4. To use this command, run the SCMKit.exe tool with the following parameters:
-s: The SCM system to search in (e.g. gitlab)
-m: The search mode (e.g. searchfile)
-c: The authentication method and credentials (e.g. userName:password or apikey)
-u: The URL of the SCM system to search in
-o: The search term to use

**Code**: [[SCMKit.exe -s gitlab -m searchfile -c userName:pas]]

> This command allows you to search for files in repositories within a particular SCM system that contain a given keyword in the file name. The command supports multiple authentication methods, including username and password or an API key. The tool will return a list of all files that match the search term, along with their repository and file path information.

**Command** ([[Search for 'some search term' using username and password in GitLab]]):

```bash
SCMKit.exe -s gitlab -m searchfile -c userName:password -u https://gitlab.something.local -o "some search term"
```

**Command** ([[Search for 'some search term' using apikey in GitLab]]):

```bash
SCMKit.exe -s gitlab -m searchfile -c apikey -u https://gitlab.something.local -o "some search term"
```

5. To list snippets owned by the current user in GitLab, run the following commands:

**Code**: [[SCMKit.exe -s gitlab -m listsnippet -c userName:pa]]

> This command uses SCMKit.exe to access GitLab and list all the snippets owned by the current user. Two different commands are provided, one using a username and password for authentication and the other using an API key. Replace 'https://gitlab.something.local' with the URL of your GitLab instance. The output will be a list of all the snippets owned by the current user.

**Command** ([[List GitLab snippets by username and password]]):

```bash
SCMKit.exe -s gitlab -m listsnippet -c userName:password -u https://gitlab.something.local
```

**Command** ([[List GitLab snippets by API key]]):

```bash
SCMKit.exe -s gitlab -m listsnippet -c apikey -u https://gitlab.something.local
```

6. To list all GitLab runners available to the current user, run the following command in PowerShell:

**Code**: [[SCMKit.exe -s gitlab -m listrunner -c userName:pas]]

> This command uses SCMKit to communicate with GitLab. It specifies the server (-s) as GitLab, the mode (-m) as listrunner, and the credentials (-c) as either userName:password or apikey. The URL (-u) specifies the GitLab instance to connect to. This command will list all runners available to the current user in GitLab.

**Command** ([[List runners from GitLab using username and password]]):

```bash
SCMKit.exe -s gitlab -m listrunner -c userName:password -u https://gitlab.something.local
```

**Command** ([[List runners from GitLab using apikey]]):

```bash
SCMKit.exe -s gitlab -m listrunner -c apikey -u https://gitlab.something.local
```

7. To use this command, replace 'apiKey' with the actual access token being used and 'https://gitlab.something.local' with the URL of your Gitlab instance. This command will return the assigned privileges for the provided access token.

**Code**: [[SCMKit.exe -s gitlab -m privs -c apiKey -u https:/]]

> This command is useful when you need to check the level of access granted to a particular access token in Gitlab. The 'privs' parameter specifies that we want to retrieve the privileges for the access token. The 's' parameter specifies the SCM system we are working with, which in this case is Gitlab. The access token is provided using the 'c' parameter and the URL of the Gitlab instance is provided using the 'u' parameter.

8. To promote a user to admin in a SCM system, run the following commands in the command line:

1. SCMKit.exe -s [SCM system] -m addadmin -c [credential type]:[credential value] -u [SCM system URL] -o [target user name]
2. SCMKit.exe -s [SCM system] -m addadmin -c apikey -u [SCM system URL] -o [target user name]
3. SCMKit.exe -s [SCM system] -m removeadmin -c [credential type]:[credential value] -u [SCM system URL] -o [target user name]

Replace the following parameters:

- [SCM system]: The name of the SCM system (e.g. GitLab, GitHub, Bitbucket)
- [credential type]: The type of credential to use (e.g. userName, apikey)
- [credential value]: The value of the credential to use
- [SCM system URL]: The URL of the SCM system
- [target user name]: The username of the user to promote to admin

**Code**: [[SCMKit.exe -s gitlab -m addadmin -c userName:passw]]

> This command allows you to promote a normal user to an administrative role in a particular SCM system. The command uses SCMKit.exe, a command line tool for managing SCM systems. The command takes in various parameters such as the SCM system name, the credential type and value, the SCM system URL, and the target user name. The command can be run in the command line and should be executed with the necessary parameters replaced.

**Command** ([[Add admin using username and password]]):

```bash
SCMKit.exe -s gitlab -m addadmin -c userName:password -u https://gitlab.something.local -o targetUserName
```

**Command** ([[Add admin using API key]]):

```bash
SCMKit.exe -s gitlab -m addadmin -c apikey -u https://gitlab.something.local -o targetUserName
```

**Command** ([[Remove admin using username and password]]):

```bash
SCMKit.exe -s gitlab -m removeadmin -c userName:password -u https://gitlab.something.local -o targetUserName
```

9. To create an access token, use the 'createpat' command followed by the authentication method and the target user name. To remove an access token, use the 'removepat' command followed by the authentication method and the access token ID. To list all access tokens for a particular user, use the 'listpat' command followed by the authentication method and the target user name.

**Code**: [[SCMKit.exe -s gitlab -m createpat -c userName:pass]]

> The 'createpat' command is used to create an access token for a particular SCM system. The 'removepat' command is used to delete an existing access token. The 'listpat' command is used to list all access tokens for a particular user. The 'c' parameter is used to specify the authentication method, which can be either 'userName:password' or 'apikey'. The 'u' parameter is used to specify the URL of the SCM system. The 'o' parameter is used to specify the target user or access token ID, depending on the command being used.

**Command** ([[Create Personal Access Token using username and password for target user in GitLab]]):

```bash
SCMKit.exe -s gitlab -m createpat -c userName:password -u https://gitlab.something.local -o targetUserName
```

**Command** ([[Create Personal Access Token using API key for target user in GitLab]]):

```bash
SCMKit.exe -s gitlab -m createpat -c apikey -u https://gitlab.something.local -o targetUserName
```

**Command** ([[Remove Personal Access Token using username and password for patID in GitLab]]):

```bash
SCMKit.exe -s gitlab -m removepat -c userName:password -u https://gitlab.something.local -o patID
```

**Command** ([[List Personal Access Tokens using username and password for target user in GitLab]]):

```bash
SCMKit.exe -s gitlab -m listpat -c userName:password -u https://gitlab.something.local -o targetUser
```

**Command** ([[List Personal Access Tokens using API key for target user in GitLab]]):

```bash
SCMKit.exe -s gitlab -m listpat -c apikey -u https://gitlab.something.local -o targetUser
```

10. This command allows you to manage SSH keys to be used in a particular SCM system. Use the 'createsshkey' option to create an SSH key, 'listsshkey' to list all available SSH keys and 'removesshkey' to remove an existing SSH key.

**Code**: [[SCMKit.exe -s gitlab -m createsshkey -c userName:p]]

> The 'createsshkey' command takes the following arguments: 
-c: The authentication credentials to be used. This can either be a username and password combination or an API token.
-u: The URL of the SCM system.
-o: The SSH public key.

The 'listsshkey' command takes the following arguments:
-c: The authentication credentials to be used. This can either be a username and password combination or an API token.
-u: The URL of the SCM system.

The 'removesshkey' command takes the following arguments:
-c: The authentication credentials to be used. This can either be a username and password combination or an API token.
-u: The URL of the SCM system.
-o: The ID of the SSH key to be removed.

**Command** ([[Create SSH Key with Username and Password]]):

```bash
SCMKit.exe -s gitlab -m createsshkey -c userName:password -u https://gitlab.something.local -o "ssh public key"
```

**Command** ([[Create SSH Key with API Token]]):

```bash
SCMKit.exe -s gitlab -m createsshkey -c apiToken -u https://gitlab.something.local -o "ssh public key"
```

**Command** ([[List SSH Key with Username and Password]]):

```bash
SCMKit.exe -s gitlab -m listsshkey -c userName:password -u https://github.something.local
```

**Command** ([[List SSH Key with API Token]]):

```bash
SCMKit.exe -s gitlab -m listsshkey -c apiToken -u https://github.something.local
```

**Command** ([[Remove SSH Key with Username and Password]]):

```bash
SCMKit.exe -s gitlab -m removesshkey -c userName:password -u https://gitlab.something.local -o sshKeyID
```

**Command** ([[Remove SSH Key with API Token]]):

```bash
SCMKit.exe -s gitlab -m removesshkey -c apiToken -u https://gitlab.something.local -o sshKeyID
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]
- [[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]
- [[File and Directory Discovery|T1083 - File and Directory Discovery]]

## Commands Used

- [[Add admin using API key]]
- [[Add admin using username and password]]
- [[Create Personal Access Token using API key for target user in GitLab]]
- [[Create Personal Access Token using username and password for target user in GitLab]]
- [[Create SSH Key with API Token]]
- [[Create SSH Key with Username and Password]]
- [[List GitLab snippets by API key]]
- [[List GitLab snippets by username and password]]
- [[List Personal Access Tokens using API key for target user in GitLab]]
- [[List Personal Access Tokens using username and password for target user in GitLab]]
- [[List repositories from GitLab using API key]]
- [[List repositories from GitLab using username and password]]
- [[List runners from GitLab using apikey]]
- [[List runners from GitLab using username and password]]
- [[List SSH Key with API Token]]
- [[List SSH Key with Username and Password]]
- [[Remove admin using username and password]]
- [[Remove Personal Access Token using username and password for patID in GitLab]]
- [[Remove SSH Key with API Token]]
- [[Remove SSH Key with Username and Password]]
- *...and 6 more*

## Tags

- [[Enumerate repositories files and secrets]]
- [[Source Code Management & CI/CD Compromise]]
