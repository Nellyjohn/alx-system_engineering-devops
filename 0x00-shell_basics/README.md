# **Shell, Basics**


# **About `Bash` projects**

Unless stated, all your projects will be auto-corrected with Ubuntu 20.04 LTS.

!(https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/205/image.jpg)


## **Resources**

### **Read or watch:**

* [What Is “The Shell”?](http://linuxcommand.org/lc3_lts0010.php)

* [Navigation](http://linuxcommand.org/lc3_lts0020.php)

* [Looking Around](http://linuxcommand.org/lc3_lts0030.php)

* [A Guided Tour](http://linuxcommand.org/lc3_lts0040.php)

* [Manipulating Files](http://linuxcommand.org/lc3_lts0050.php)

* [Working With Commands](http://linuxcommand.org/lc3_lts0060.php)

* [Reading Man pages](http://linuxcommand.org/lc3_man_pages/man1.html)

* [Keyboard shortcuts for Bash](https://www.howtogeek.com/181/keyboard-shortcuts-for-bash-command-shell-for-ubuntu-debian-suse-redhat-linux-etc/)

* [LTS](https://wiki.ubuntu.com/LTS)

* [Shebang](https://en.wikipedia.org/wiki/Shebang_%28Unix%29)

**man or help:**

* `cd`

* `ls`

* `pwd`

* `less`

* `file`

* `ln`

* `cp`

* `mv`

* `rm`

* `mkdir`

* `type`

* `which`

* `help`

* `man`


# **Learning Objectives**

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/?fbclid=IwAR2K5_BGPVo0QjJXkOIIqNsqcXK4lTskPWJvA0asKQIGtCPWaQBdKmj1Ztg), **without the help of Google:**


## **General**

* What does RTFM mean?
* What is a Shebang

## **What is the Shell**

* What is the shell

* What is the difference between a terminal and a shell

* What is the shell prompt

* How to use the history (the basics)


## **Navigation**

* What do the commands or built-ins `cd`, `pwd`, `ls` do

* How to navigate the filesystem

* What are the . and .. directories

* What is the working directory, how to print it and how to change it

* What is the root directory

* What is the home directory, and how to go there

* What is the difference between the root directory and the home directory of the user root

* What are the characteristics of hidden files and how to list them

* What does the command `cd -` do


## **Looking Around**

* What do the commands `ls`, `less`, `file` do

* How do you use options and arguments with commands

* Understand the ls long format and how to display it

* [A Guided Tour](http://linuxcommand.org/lc3_lts0040.php)

* What does the `ln` command do

* What do you find in the most common/important directories

* What is a symbolic link

* What is a hard link

* What is the difference between a hard link and a symbolic link


## **Manipulating Files**

* What do the commands `cp`, `mv`, `rm`, `mkdir` do

* What are wildcards and how do they work

* How to use wildcards


## **Working with Commands**

* What do `type`, `which`, `help`, `man` commands do

* What are the different kinds of commands

* What is an alias

* When do you use the command help instead of man


## **Reading Man Pages**

* How to read a man page

* What are man page sections

* What are the section numbers for User commands, System calls and Library functions


## **Keyboard Shortcuts for Bash**

* Common shortcuts for Bash


## **LTS**

* What does `LTS` mean?


## **Copyright - Plagiarism**

* You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.

* You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.

* You are not allowed to publish any content of this project.

* Any form of plagiarism is strictly forbidden and will result in removal from the program.


# **Requirements**

## **General**

* Allowed editors: `vi`, `vim`, `emacs`
* All your scripts will be tested on Ubuntu 20.04 LTS
* All your scripts should be exactly two lines long (`$ wc -l file` should print 2)
* All your files should end with a new line ([why?](https://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789))
* The first line of all your files should be exactly `#!/bin/bash`
* A `README.md` file at the root of the repo, containing a description of the repository
* A `README.md` file, at the root of the folder of this project, describing what each script is doing
* You are not allowed to use backticks, &&, || or ;
All your scripts must be executable. To make your file executable, use the chmod command: chmod u+x file. Later, we’ll learn more about how to utilize this command.

# **More Info**

*Example of line count and first line*

julien@ubuntu:/tmp$ wc -l 12-file_type 
2 12-file_type
julien@ubuntu:/tmp$ head -n 1 12-file_type 
*#!/bin/bash*
julien@ubuntu:/tmp$ 
In order to test your scripts, you will need to use this command: chmod u+x file. We will see later what does chmod mean and do, but you can have a look at man chmod if you are curious.

Example

julien@ubuntu:/tmp$ ls
12-file_type
lll
julien@ubuntu:/tmp$ ls -la lll
-rw-rw-r-- 1 julien julien 15 Sep 19 21:05 lll
julien@ubuntu:/tmp$ cat lll
#!/bin/bash
ls
julien@ubuntu:/tmp$ ls -l lll
-rw-rw-r-- 1 julien julien 15 Sep 19 21:05 lll
julien@ubuntu:/tmp$ chmod u+x lll # you do not have to understand this yet
julien@ubuntu:/tmp$ ls -l lll
-rwxrw-r-- 1 julien julien 15 Sep 19 21:05 lll
julien@ubuntu:/tmp$ ./lll
12-file_type
lll
julien@ubuntu:/tmp$
