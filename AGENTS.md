# Codex 项目上下文

## 用户背景

用户是工程方向研究生，使用 Windows 系统。研究方向是偏振成像结合超分辨率和 HDR 重建。用户关注 AI 产品、模型体系、Agent、编程工具和科研效率，能够接受较高技术密度，但偏好紧凑、中文、少废话的回答。

本机显卡为 NVIDIA GeForce MX450，约 2GB 显存；涉及本地模型、训练或推理时，应优先考虑轻量模型、CPU、云端或 API 方案。

## 当前项目定位

当前工作区：

```text
D:\Codex_Projects\Learn_GitHub
```

远程 GitHub 仓库：

```text
MingyiJiang/Polarization-HDR-SR-Baseline
```

这个仓库目前主要用于保存 Git / GitHub 学习上下文和练习记录。除非用户明确重新定义用途，不要把它当作前端项目、Python 包或正在开发的科研代码仓库。不要在没有真实启动开发服务器的情况下提供 localhost 预览链接。

当前期望的内容结构：

```text
AGENTS.md       # 宏观项目上下文、协作偏好、长期状态
Git学习笔记.md  # Git / GitHub 细节知识点
.git/           # Git 历史与远程连接，不能手动修改
```

## Git / GitHub 学习进度

用户已经练习过 GitHub Star / Watch、Fork、Pull Request、Issue、个人仓库创建、本地 clone、Git 身份配置、add / commit / push、pull / fetch / clone / init、branch / merge / delete、restore / revert、HEAD，以及基础 Trae 源代码管理操作。

用户更偏好用 Trae 做 Git 操作，但可以在需要时运行 PowerShell 命令。解释 Git 操作时，优先讲清楚“这个操作会改变什么”，再给命令。

新会话开始或用户要求对齐项目状态时，先运行：

```powershell
git status --short --branch
git remote -v
```

然后解释结果，再建议后续 Git 操作。

本地远程连接曾配置为：

```text
origin = https://github.com/MingyiJiang/Polarization-HDR-SR-Baseline.git
```

用户曾在 PowerShell 中配置临时代理后成功 push 到 GitHub；也完成过远程分支清理和 feature 分支合并到 `main` 的练习。

## GitHub 练习历史

- Fork 过 `ChenyangLEI/awesome-polarization-in-vision`。
- 打开过 PR：`Add PIDSR CVPR 2025 paper`，用于添加 PIDSR CVPR 2025 论文条目。
- 在 `elerac/polanalyser` 打开过关于 HDR 和高位深偏振图像工作流的 Issue。
- 创建过个人仓库 `MingyiJiang/Polarization-HDR-SR-Baseline`。
- 练习过本地分支创建、push、合并到 `main`、删除远程分支。

## Git 操作心智模型

常规提交流程：

```text
编辑文件 -> stage/add 暂存 -> commit 本地提交 -> push 推送到 GitHub
```

分支模型：

```text
main = 稳定主线
feature/... 或 experiment/... = 临时工作线
merge = 把认可的修改合回 main
```

撤销模型：

```text
restore = 丢弃未提交修改
revert = 创建一个新提交，用来反向抵消某个旧提交
```

避免使用 `reset --hard`，除非用户明确要求并理解它会强制丢弃工作区和提交指针相关变化。

## Windows 与终端约束

当前主要使用 Windows PowerShell 5.1，不计划升级 PowerShell 7。PowerShell 已配置 UTF-8 profile；但读取包含中文的文本文件时，仍优先显式使用 `-Encoding UTF8`。

如果终端输出中文乱码，不要直接判断文件损坏，应先用 UTF-8 重新读取验证。Windows 路径可能包含中文和空格，执行命令时注意引号、转义和当前工作目录。在 PowerShell 中查询可执行文件路径时，使用 `where.exe node`、`where.exe npm`，不要误用 `where` 别名。

## 本机开发环境

- Git 已安装。
- VS Code 已安装。
- Node.js 安装在 `D:\software\NODE\`。
- Anaconda / conda 可用，PowerShell 启动时会加载 conda 初始化。

## 网络与代理

Git 访问 GitHub 可能失败：

```text
Failed to connect to github.com port 443
```

此前原因是 Git 未使用代理。曾经可用的临时 PowerShell 代理为：

```powershell
$env:HTTPS_PROXY="http://127.0.0.1:7897"
$env:HTTP_PROXY="http://127.0.0.1:7897"
```

这只影响当前 PowerShell 会话，不是全局配置。

## 协作偏好

- 默认使用中文。
- 回答紧凑但技术上说清楚，减少不必要换行、分段和列表。
- 涉及 Git 操作时，先解释操作影响，再给命令。
- 用户要求检查或整理仓库时，先检查状态，避免无理由破坏性操作。
- 不手动修改 `.git`。
- 不随意改变共享环境、全局配置、PATH、profile、包管理器配置或长期后台任务。
- 下载外部资源、模型、数据集或依赖前，如果体积较大、写入共享缓存或影响环境，应先询问用户。
- 如果继续 GitHub 学习，优先用实践任务引导，而不是抽象背命令。
