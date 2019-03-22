# 我的Git指南

* git init
	- 创建一个仓库（将当前目录变成git可以管理的仓库）
  
-------------------

* git add 添加文件到暂存区
  - 表示当前目录，添加目录所有文件
  - `xxx.txt`   `xxx.cpp`  添加指定文件
  
-------------------
                                                                               
* git commit –m <message>
  - 提交暂存器内容到仓库，不加m参数进入编辑器编写message
  
-------------------         

* git push -u origin master (–f)
  - origin：表示远程仓库，`https://github.com/用户名/远程仓库名.git`
  -	master：表示本地分支
  -	-u：第一次push时把本地和远程关联起来，之后可省-u参数
  -	-f：表示强制将本地内容推送到指定远程仓库，将覆盖远程仓库
    
-------------------
                                                                               
* git diff
  - 查看修改内容
        
-------------------        
        
* git diff HEAD -- readme.txt
  - 查看工作区和版本库最新版本的区别

-------------------

* git log –pretty=oneline
  - 查看历史记录，-pretty=oneline简化输出
  - 1094abd…：commit_id（版本号）

-------------------

* git reset --hard HEAD^
  - 回退上一个版本，HEAD^^（上两个版本），HEAD~100（上一百个版本）
  - --hard 1094a（commit_id），回退到指定版本
  
-------------------  
  
* git reset HEAD <file>
  - 把暂存区的修改撤销（unstage），重新放回工作区
  - git reset 命令可以回退版本，也可把暂存区的修改退回工作区，用HEAD时，表示最新版本

-------------------

* git checkout -- file
  - 撤销提交，回到最近一次add或commit时的状态（感觉本质是从版本库更新回工作区）

-------------------

* git reflog
  - 记录每一次执行的命令

-------------------

* git remote add origin `https://github.com/<用户名>/<远程仓库名>.git`
  - 关联一个本地仓库到远程仓库
  - origin：远程仓库在本地的名字
	
**关联远程仓库另一种方法**
	
> * 用gitbash输入命令 ssh-keygen –t rsa –C “`youremail@example.com`”	
> * 一路回车，会生成 .ssh文件夹，id_rsa私钥，id_res.pub公钥
> * 在github中的setting里add ssh key填上任意title，粘上id_res.pub的内容
> * git remote add origin `git@github.com:<用户名>/<远程仓库名>.git`
> * git push –u origin master
> * 第一次push会有ssh警告，输入yes即可

-------------------  
  
* git remote –v
  - 查看远程仓库信息

-------------------

* git rm <file>
  - 从版本库删除文件，需commit才生效
  - 误删时使用git checkout替换工作区版本

-------------------

* git clone `https://github.com/<用户名>/<远程仓库名>.git`
  - 从远程仓库克隆到本地
  - 支持ssh协议和https协议

-------------------

* git branch
  - 查看所有分支，当前分支会有一个 * 标记

-------------------

* git checkout –b dev
  - 创建dev分支并从master切换到dev
  - 等价git branch dev（创建）    git checkout dev（切换）
* git branch –D dev
  - 强制删除未合并的分支dev

-------------------

* git merge dev
  - 把dev分支的内容合并到（当前）master分支上

-------------------

* git log --graph --pretty=oneline --abbrev-commit
  - 查看分支的合并情况

-------------------

* git merge --no-ff –m“merge with no-ff”dev
  - 禁用fast forward的合并分支，fast forword是快速合并，但会丢失分支信息，不使用该模式可以保存分支信息，便于历史查看

-------------------

* git stash
  - 保存当前工作区现场，可多次保存
* git stash list
  - 查看保存的工作区，多个时按stash@{0}、stash@{1}……展示
* git stash apply （stash@{0}）
  - 恢复后保留stash内容，使用git stash drop删除，括号指定恢复哪个版本
* git stash pop
  - 恢复后删除stash内容

-------------------

* git tag v1.0
  - 给当前分支打标签
* git tag
  - 查看标签
* git tag v0.9 f52c633
  - 给指定版本打标签
* git tag –a v1.0 –m“xxx”1094abd
  - -a 指定版本名
  - -m 说明信息
* git show v1.0
  - 查看标签信息

-------------------

* 使用github.io作为个人网站主页
  - 要求：创建名为<账号名>.github.io的仓库，将网页文件放在master分支上
* 使用gh-pages分支生成项目主页
  - 要求：将项目主页的网页文件放在项目仓库中的gh-pages分支，网址为<账号名>.github.io/<仓库名>。

-------------------
