# Learning Python Repository

Welcome to my Learning Python repository! This repository is dedicated to documenting my journey as I learn and explore the Python programming language. Here, you'll find various resources, notes, and projects that I'll be working on during my learning experience.

## Table of Contents

- [About](#about)
- [Getting Started](#getting-started)
- [Resources](#resources)
- [Projects](#projects)
- [Progress](#progress)
- [Contact](#contact)

## About

Hello there, I'm Emin Fidan, a passionate advocate for international education. My background in student recruitment and marketing tech led me to dive into learning Python. Wondering why? Well, the tech landscape is rapidly evolving, and Python's versatility caught my attention.

## Getting Started

If you're new to Python, this section can serve as a guide to help you set up your development environment. Include instructions on how to install Python, set up a virtual environment, and anything else that can help other beginners get started.

## Resources

List the resources you're using to learn Python. These could include online tutorials, books, video courses, and more. Adding brief descriptions or comments about each resource can be helpful.



:pill: - [Python Official Documentation](https://docs.python.org/): The official Python documentation is a comprehensive resource for learning the language.

:rocket: - [Python Developer](https://roadmap.sh/python) Step by step guide to becoming a Python developer in 2023

 :calendar: - [Learn Python tracks](https://hyperskill.org/categories/1) Start your journey in development with Python by gaining a foundational understanding of the language's basics and main concepts.

### Getting & Creating Projects

| Command | Description |
| ------- | ----------- |
| `git init` | Initialize a local Git repository |
| `git clone ssh://git@github.com/[username]/[repository-name].git` | Create a local copy of a remote repository |

### Basic Snapshotting

| Command | Description |
| ------- | ----------- |
| `git status` | ตรวจสอบสถานะของไฟล์ |
| `git add [file-name.txt]` | เพิ่มไฟล์ไปใน staging area |
| `git add -A` | เพิ่มไฟล์ใหม่และไฟล์ที่แก้ไขทั้งหมดไปใน staging area |
| `git commit -m "[commit message]"` | เขียนเพื่อบอกว่าได้ทำอะไรในไฟล์ ก่อนจะส่งขึ้น server Commit changes |
| `git rm -r [file-name.txt]` | ลบไฟล์ที่ไม่ต้องการออก Remove a file (or folder) |

### Branching & Merging

| Command | Description |
| ------- | ----------- |
| `git branch` | List branches (the asterisk denotes the current branch) |
| `git branch -a` | List all branches (local and remote) |
| `git branch [branch name]` | Create a new branch |
| `git branch -d [branch name]` | Delete a branch |
| `git push origin --delete [branch name]` | Delete a remote branch |
| `git checkout -b [branch name]` | Create a new branch and switch to it |
| `git checkout -b [branch name] origin/[branch name]` | Clone a remote branch and switch to it |
| git[old branch name] [new branch name]` | Rename a local branch |
| `git checkout [branch name]` | Switch to a branch |
| `git checkout -` | Switch to the branch last checked out |
| `git checkout -- [file-name.txt]` | Discard changes to a file |
| `git merge [branch name]` | Merge a branch into the active branch |
| `git merge [source branch] [target branch]` | Merge a branch into a target branch |
| `git stash` | Stash changes in a dirty working directory |
| `git stash clear` | Remove all stashed entries |

### Sharing & Updating Projects

| Command | Description |
| ------- | ----------- |
| `git push origin [branch name]` | Push a branch to your remote repository |
| `git push -u origin [branch name]` | Push changes to remote repository (and remember the branch) |
| `git push` | Push changes to remote repository (remembered branch) |
| `git push origin --delete [branch name]` | Delete a remote branch |
| `git pull` | Update local repository to the newest commit |
| `git pull origin [branch name]` | Pull changes from remote repository |
| `git remote add origin ssh://git@github.com/[username]/[repository-name].git` | Add a remote repository |
| `git remote set-url origin ssh://git@github.com/[username]/[repository-name].git` | Set a repository's origin branch to SSH |

### Inspection & Comparison

| Command | Description |
| ------- | ----------- |
| `git log` | View changes |
| `git log --summary` | View changes (detailed) |
| `git log --oneline` | View changes (briefly) |
| `git diff [source branch] [target branch]` | Preview changes before merging |
