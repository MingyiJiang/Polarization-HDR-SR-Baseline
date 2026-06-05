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
