# Git 学习笔记

这个文件专门记录 Git / GitHub 学习过程中的细节知识点。整体项目背景、协作偏好和长期上下文放在 `AGENTS.md`。

## .gitignore

### 核心结论

`.gitignore` 的作用对象是本地工作区中尚未被 Git 跟踪的新文件。它不是在 GitHub 上传或下载时才生效，而是在本地 `git status`、`git add`、`git commit` 之前影响哪些文件进入 Git 管理范围。

一句话记忆：

```text
.gitignore 只忽略未 tracked 的文件；已经 tracked 的文件不受它影响。
```

### 被忽略的文件不会被提交是什么意思

如果一个文件被 `.gitignore` 匹配，并且它从未被 `git add` / `git commit` 过，那么它可以理解为不属于 Git 仓库管理。

这意味着：

- Git 不记录它的内容。
- `git status` 通常不会提示它。
- `git add .` 默认不会把它加入暂存区。
- 它不会进入 commit。
- 它不会被 push 到 GitHub。
- Git 历史中没有它的版本，因此以后也无法通过 Git 回溯它。

例如 `.gitignore` 中写了：

```gitignore
.env
data/
```

如果 `.env` 和 `data/raw.zip` 从未被提交过，它们只是本机普通文件，不属于仓库历史。以后切换分支、回到旧 commit、查看 `git log`，都查不到这些文件的历史版本。

### 远程仓库已有 .env，但 .gitignore 写了 .env，还会下载吗

会。

如果 `.env` 已经存在于远程仓库的某个提交中，说明它已经是 tracked 文件。即使 `.gitignore` 里写了 `.env`，执行 `git clone` 或 `git pull` 时仍然会把它下载下来。

原因是 `.gitignore` 不会过滤远端仓库中已经存在的 tracked 文件。远程仓库里能看到的文件，通常就是已经提交进 Git 历史的文件。

典型情况：

```text
远程仓库已有：
.env

.gitignore 里写了：
.env

结果：
git clone 仍会下载 .env
```

### 如何让已经 tracked 的 .env 以后不再被仓库管理

如果想让 `.env` 从当前版本开始不再被 Git 跟踪，但保留本地文件，可以执行：

```powershell
git rm --cached .env
git commit -m "Stop tracking .env"
git push
```

其中：

- `git rm --cached .env`：从 Git 索引中移除 `.env`，但不删除本地文件。
- `commit`：记录“仓库以后不再跟踪 .env”这个变化。
- `push`：把这个变化同步到 GitHub。

注意：这样只能让 `.env` 从新提交开始不再被跟踪。历史提交中曾经出现过的 `.env` 仍然存在。如果 `.env` 里包含 token、API key、密码等敏感信息，应视为已经泄露，需要更换密钥。

### 已经 tracked 的文件写进 .gitignore 后为什么还需要 git rm --cached

已经被 Git 跟踪的文件，单纯写进 `.gitignore` 不会停止跟踪。`.gitignore` 只影响未 tracked 的新文件，不会改变 Git 已经记录在索引里的文件。

如果目标是让某个已经 tracked 的文件以后不再进入仓库，例如 `AGENTS.md`，需要两步：

```powershell
# 1. 让以后这个文件被忽略
# 在 .gitignore 中写入：
AGENTS.md

# 2. 从 Git 索引中移除，但保留本地文件
git rm --cached AGENTS.md
```

执行 `git rm --cached AGENTS.md` 后，`git status` 里可能会看到：

```text
D  AGENTS.md
?? .gitignore
```

这里的 `D AGENTS.md` 不是说本地磁盘上的 `AGENTS.md` 被删除了，而是说相对于 Git 仓库，下一次 commit 会记录“仓库不再跟踪 AGENTS.md”。本地文件仍然保留。

完整逻辑是：

```text
已 tracked 的 AGENTS.md
  -> 写进 .gitignore：不够，仍会继续跟踪
  -> git rm --cached AGENTS.md：停止跟踪
  -> commit：记录“仓库不再管理 AGENTS.md”
  -> push：GitHub 上新版本不再有 AGENTS.md
```

但历史提交里曾经出现过的 `AGENTS.md` 仍然存在，只是最新版本不再跟踪它。

### 当前理解模型

```text
本地普通文件
  -> git add
  -> tracked 文件
  -> git commit
  -> 仓库历史
  -> git push
  -> GitHub 远端仓库
```

`.gitignore` 主要拦在 `git add` 之前：

```text
被 .gitignore 匹配的未 tracked 文件
  -> 默认不会被 git add .
  -> 默认不会进入 commit
  -> 默认不会被 push
```

但如果文件已经 tracked：

```text
已经 tracked 的文件
  -> .gitignore 不再阻止 Git 管理它
  -> clone / pull 仍会下载它
```

## GitHub 网页编辑器、Codespaces 与本地 VS Code

在 GitHub 仓库页面按英文句号 `.`，会打开 `github.dev` 网页编辑器。它看起来像 VS Code，但不是完整的本地 VS Code。

区别可以这样理解：

```text
github.dev
  -> 浏览器里的轻量编辑器
  -> 适合快速看代码、搜索文件、改 README、小修文本、提交 commit
  -> 没有本地终端、conda、本机 Python、GPU、完整文件系统
  -> 不能直接当成本地开发环境来跑复杂代码

本地 VS Code
  -> 安装在本机的完整 IDE
  -> 可以用 PowerShell / conda / Python / Node / Git / 本机文件系统
  -> 可以调试、运行代码、访问本机 GPU 和本地环境

GitHub Codespaces
  -> GitHub 提供的云端开发环境
  -> 可以有终端、容器、依赖环境
  -> 适合在线运行和开发代码，但最好用 .devcontainer/devcontainer.json 明确配置环境
```

所以，`github.dev` 更像“快速在线改文件”；Codespaces 才更接近“云端 VS Code 开发机”；本地 VS Code 仍然最适合需要本机环境、conda、GPU 或复杂调试的开发。

## Fork 后为什么建议在分支上修改

Fork 一个仓库后，自己账号下会出现一份副本。为了后续同步原仓库和发 PR 更清楚，通常不建议直接在 fork 的 `main` 上做所有修改，而是从 `main` 新建功能分支。

推荐模型：

```text
fork/main
  -> 尽量保持接近原仓库 main
  -> 用来同步 upstream

feature/add-pidsr-paper
  -> 专门放这一次 PR 的修改

feature/other-change
  -> 下一次 PR 另开一个分支
```

这样做的好处：

- 每个 PR 只包含一个明确任务，维护者更容易 review。
- 如果上一个 PR 没合并，下一次 PR 不会意外带上旧改动。
- fork 的 `main` 可以保持干净，之后同步原仓库时更不容易把实验改动和 upstream 更新混在一起。
- 出现冲突时，冲突范围通常只集中在当前功能分支里。

简单理解：

```text
main = 保持干净，方便同步原仓库
分支 = 放具体改动，方便发 PR 和处理冲突
```

## Pull Request 页面怎么看

PR 页面是在表达“某个来源分支的改动，请求合并到目标仓库的目标分支”。

例如：

```text
Mingyi-L wants to merge 1 commit into ChenyangLEI:main from Mingyi-L:add-pidsr-paper
```

含义是：

```text
来源：Mingyi-L:add-pidsr-paper
目标：ChenyangLEI:main
请求：把来源分支的 1 个 commit 合并到目标分支
```

常见标签页：

```text
Conversation
  -> PR 讨论区，包含说明、评论、维护者反馈、关闭/合并记录

Commits
  -> 这个 PR 包含哪些提交

Checks
  -> CI / 自动测试 / 格式检查等结果

Files changed
  -> 这个 PR 修改了哪些文件、具体改了哪些行
```

如果要查看以前 PR 具体改了哪里，进入 PR 页面后点 `Files changed`。

## PR 的 Merged、Closed、未合并关闭

PR 有两种常见结束状态：

```text
Merged
  -> PR 被合并
  -> 改动已经进入目标分支
  -> GitHub 自动把 PR 标记为完成

Closed / Closed with unmerged commits
  -> PR 被关闭
  -> 改动没有进入目标分支
  -> 等于这次合并请求结束，但没有被采纳
```

如果页面显示：

```text
Closed with unmerged commits
```

意思是：PR 里有提交，但这些提交没有合并进目标仓库。

如果页面显示类似：

```text
Mingyi-L closed this by deleting the head repository
```

意思是：PR 的来源仓库或来源引用被删除了，GitHub 无法继续从来源分支合并，所以 PR 被关闭。这不是维护者手动拒绝，也不是合并成功，而是来源不存在导致的未合并关闭。

权限上不是只有发起者能关闭：

```text
PR 发起者
  -> 通常可以关闭自己发起的 PR

原仓库维护者 / 有权限的人
  -> 可以关闭 PR
  -> 也可以 merge PR

Issue 发起者
  -> 通常可以关闭自己开的 issue

仓库维护者 / 有权限的人
  -> 可以关闭仓库里的 issue
```

所以，PR / Issue 不是“谁发起谁才能关闭”。发起者可以关闭自己的，仓库维护者也可以关闭仓库中的。

## 如何找自己以前的 PR、Issue、Watch 和 Star

查看自己创建或参与过的 PR，可以用 GitHub 顶部搜索框：

```text
is:pr author:Mingyi-L
```

如果想看自己参与过的 PR，包括自己创建、评论、被提到的：

```text
is:pr involves:Mingyi-L
```

也可以直接打开：

```text
https://github.com/pulls
```

查看自己关注过动态的仓库，也就是 Watch 过的仓库：

```text
https://github.com/watching
```

GitHub 网页路径：

```text
右上角头像
  -> Settings
  -> Notifications
  -> Watched repositories
```

查看自己 Star 过的仓库：

```text
https://github.com/Mingyi-L?tab=stars
```

三者区别：

```text
Watch
  -> 订阅仓库动态，用来收通知

Star
  -> 收藏 / 标记感兴趣，更像书签和公开兴趣展示

Fork
  -> 复制一份仓库到自己账号下，方便改代码和发 PR
```
