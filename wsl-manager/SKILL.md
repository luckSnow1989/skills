---
name: wsl-manager
description: 管理 Windows 系统上的 WSL（Windows Subsystem for Linux），支持安装、卸载、启动、关闭、列出、导出、导入、执行命令等常规操作。当用户提到 WSL 相关操作、Linux 子系统管理、在 Windows 上运行 Linux 时自动激活。
---

# WSL 管理技能

## 描述

本技能提供对 Windows 系统上 WSL（Windows Subsystem for Linux）的完整管理能力。通过参数化的操作指令，智能体可以执行 WSL 的安装、卸载、启动、关闭、配置等一系列常规管理任务。

## 使用场景

- 用户要求安装或卸载 WSL 或某个 Linux 发行版
- 用户需要启动、关闭或重启 WSL 实例
- 用户需要查看当前 WSL 发行版列表或运行状态
- 用户需要在 WSL 中执行特定命令
- 用户需要导出或导入 WSL 发行版（备份/迁移）
- 用户需要配置 WSL 参数（内存、处理器、网络等）
- 用户需要更新 WSL 内核
- 用户需要设置默认 WSL 发行版
- 用户遇到 WSL 相关问题需要排查

## 操作参数说明

本技能通过 `操作类型 + 参数` 的方式调用。操作类型和对应参数如下：

| 操作 | 参数 | 必填 | 说明 |
|------|------|------|------|
| `install` | `--distribution <名称>` | 否 | 安装 WSL 及指定发行版，不指定则安装默认发行版(Ubuntu) |
| `uninstall` | `--distribution <名称>` | 是 | 卸载指定 WSL 发行版（会删除所有数据） |
| `start` | `--distribution <名称>` | 否 | 启动指定发行版，不指定则启动默认发行版 |
| `stop` | `--distribution <名称>` | 否 | 关闭指定发行版，不指定则关闭所有运行中的实例 |
| `restart` | `--distribution <名称>` | 否 | 重启指定发行版（先 stop 再 start） |
| `list` | `--running` / `--verbose` | 否 | 列出发行版，`--running` 仅显示运行中的，`--verbose` 显示详细信息 |
| `set-default` | `--distribution <名称>` | 是 | 设置默认 WSL 发行版 |
| `update` | 无 | - | 更新 WSL 内核到最新版本 |
| `status` | 无 | - | 查看 WSL 运行状态和版本信息 |
| `export` | `--distribution <名称>` `--output <文件路径>` | 是 | 将发行版导出为 tar 文件 |
| `import` | `--distribution <名称>` `--input <文件路径>` `--location <安装路径>` | 是 | 从 tar 文件导入发行版 |
| `exec` | `--distribution <名称>` `--command <命令>` | 是 | 在指定 WSL 发行版中执行命令 |
| `config` | `--key <配置项>` `--value <值>` | 是 | 配置 WSL 参数（.wslconfig 文件） |
| `convert` | `--distribution <名称>` | 是 | 将 WSL1 发行版转换为 WSL2 |
| `check-version` | `--distribution <名称>` | 否 | 检查发行版使用的 WSL 版本(1 或 2) |

## 指令

### 前置检查

在执行任何 WSL 操作之前，必须先执行以下检查：

1. **确认操作系统**：确保当前系统为 Windows 10（版本 2004+）或 Windows 11。执行命令：
   ```powershell
   [System.Environment]::OSVersion.Version
   ```
   Windows 10 需要 Major=10 且 Build>=19041，Windows 11 需要 Build>=22000。

2. **确认 WSL 可用性**：检查 WSL 是否已安装：
   ```powershell
   wsl --status 2>&1
   ```
   如果返回错误信息提示 WSL 未安装，则需先执行 `install` 操作。

3. **确认管理员权限**：安装和卸载操作需要管理员权限。检查方式：
   ```powershell
   ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
   ```
   如果返回 `False`，需要提示用户以管理员身份运行。

---

### 操作：install — 安装 WSL

**适用场景**：首次安装 WSL，或安装额外的 Linux 发行版。

**步骤**：

1. 检查是否已安装 WSL：
   ```powershell
   wsl --status 2>&1
   ```

2. 如果 WSL 未安装，执行安装（需要管理员权限）：
   ```powershell
   wsl --install
   ```
   此命令会自动启用"适用于 Linux 的 Windows 子系统"和"虚拟机平台"功能，然后安装默认的 Ubuntu 发行版。

3. 如果需要安装特定发行版，先查看可用发行版列表：
   ```powershell
   wsl --list --online
   ```

4. 安装指定发行版：
   ```powershell
   wsl --install --distribution <发行版名称>
   ```

5. 安装完成后，可能需要重启计算机。如果提示重启，告知用户：
   > "WSL 安装需要重启计算机才能生效，请保存工作后重启。"

6. 重启后，首次启动发行版会要求创建用户名和密码，引导用户完成初始化。

**注意事项**：
- 安装 WSL2 需要启用虚拟机平台功能
- 如果企业环境中组策略限制了 Windows 功能启用，需要联系 IT 管理员
- 网络代理环境下可能需要配置代理才能下载发行版

---

### 操作：uninstall — 卸载 WSL 发行版

**适用场景**：移除不再需要的 Linux 发行版。

**步骤**：

1. 确认要卸载的发行版存在：
   ```powershell
   wsl --list --verbose
   ```

2. **重要警告**：向用户确认卸载操作，明确告知此操作将删除该发行版中的所有数据且不可恢复：
   > "⚠️ 卸载 <发行版名称> 将永久删除该发行版中的所有文件和数据，此操作不可逆。确认是否继续？"

3. 用户确认后执行卸载：
   ```powershell
   wsl --unregister <发行版名称>
   ```

4. 验证卸载结果：
   ```powershell
   wsl --list --verbose
   ```

**注意事项**：
- `--unregister` 会删除发行版及所有数据
- 如果只是想重置发行版而非删除，可使用 Windows 设置中的"重置"功能
- 卸载最后一个发行版不会卸载 WSL 本身

---

### 操作：start — 启动 WSL

**适用场景**：启动指定的 WSL 发行版。

**步骤**：

1. 查看当前发行版状态：
   ```powershell
   wsl --list --verbose
   ```

2. 启动默认发行版：
   ```powershell
   wsl
   ```

3. 或启动指定发行版：
   ```powershell
   wsl --distribution <发行版名称>
   ```

4. 如需以指定用户身份启动：
   ```powershell
   wsl --distribution <发行版名称> --user <用户名>
   ```

5. 如需在指定目录启动：
   ```powershell
   wsl --distribution <发行版名称> --cd <目录路径>
   ```

---

### 操作：stop — 关闭 WSL

**适用场景**：关闭运行中的 WSL 实例以释放资源。

**步骤**：

1. 查看当前运行中的发行版：
   ```powershell
   wsl --list --running
   ```

2. 关闭指定发行版：
   ```powershell
   wsl --terminate <发行版名称>
   ```

3. 或关闭所有运行中的 WSL 实例：
   ```powershell
   wsl --shutdown
   ```

4. 验证关闭结果：
   ```powershell
   wsl --list --running
   ```

**注意事项**：
- 关闭操作会终止该发行版中所有正在运行的进程
- 未保存的工作将会丢失，执行前应提醒用户保存
- `--shutdown` 会关闭所有发行版，谨慎使用

---

### 操作：restart — 重启 WSL

**适用场景**：需要重启 WSL 实例（如应用配置更改后）。

**步骤**：

1. 关闭指定发行版：
   ```powershell
   wsl --terminate <发行版名称>
   ```

2. 重新启动该发行版：
   ```powershell
   wsl --distribution <发行版名称>
   ```

3. 如果修改了 `.wslconfig` 文件，需要关闭所有实例再重启：
   ```powershell
   wsl --shutdown
   wsl
   ```

---

### 操作：list — 列出 WSL 发行版

**适用场景**：查看已安装的 WSL 发行版信息。

**步骤**：

1. 列出所有已安装的发行版：
   ```powershell
   wsl --list --verbose
   ```

2. 仅列出运行中的发行版：
   ```powershell
   wsl --list --running
   ```

3. 列出可安装的在线发行版：
   ```powershell
   wsl --list --online
   ```

**输出解读**：
- `NAME`：发行版名称
- `STATE`：运行状态（Running / Stopped）
- `VERSION`：WSL 版本（1 或 2）
- 默认发行版前会有 `*` 标记

---

### 操作：set-default — 设置默认发行版

**适用场景**：更改默认启动的 WSL 发行版。

**步骤**：

1. 查看当前发行版列表和默认发行版：
   ```powershell
   wsl --list --verbose
   ```

2. 设置新的默认发行版：
   ```powershell
   wsl --set-default <发行版名称>
   ```

3. 验证设置结果：
   ```powershell
   wsl --list --verbose
   ```

---

### 操作：update — 更新 WSL

**适用场景**：更新 WSL 内核到最新版本。

**步骤**：

1. 执行 WSL 更新：
   ```powershell
   wsl --update
   ```

2. 检查更新状态：
   ```powershell
   wsl --update --status
   ```

3. 如需回滚到之前的版本：
   ```powershell
   wsl --update --rollback
   ```

**注意事项**：
- 更新可能需要从 GitHub 下载，网络受限环境可能需要配置代理
- 更新后建议重启 WSL 实例

---

### 操作：status — 查看 WSL 状态

**适用场景**：查看 WSL 整体运行状态和配置信息。

**步骤**：

1. 查看 WSL 状态：
   ```powershell
   wsl --status
   ```

2. 查看 WSL 版本信息：
   ```powershell
   wsl --version
   ```

**输出解读**：
- 默认发行版
- 默认 WSL 版本
- 内核版本
- Windows 版本兼容性

---

### 操作：export — 导出发行版

**适用场景**：备份 WSL 发行版，或迁移到其他机器。

**步骤**：

1. 确认发行版存在且最好处于停止状态：
   ```powershell
   wsl --terminate <发行版名称>
   ```

2. 导出发行版为 tar 文件：
   ```powershell
   wsl --export <发行版名称> <输出文件路径.tar>
   ```
   示例：
   ```powershell
   wsl --export Ubuntu D:\Backup\ubuntu-backup.tar
   ```

3. 验证导出文件：
   ```powershell
   Get-Item <输出文件路径.tar> | Select-Object Name, Length, LastWriteTime
   ```

**注意事项**：
- 导出文件可能较大（数 GB），确保目标磁盘有足够空间
- 导出期间发行版不可用
- 建议在导出前关闭发行版以确保数据一致性

---

### 操作：import — 导入发行版

**适用场景**：从备份恢复 WSL 发行版，或迁移其他机器的发行版。

**步骤**：

1. 确认 tar 备份文件存在：
   ```powershell
   Test-Path <tar文件路径>
   ```

2. 导入发行版：
   ```powershell
   wsl --import <发行版名称> <安装路径> <tar文件路径>
   ```
   示例：
   ```powershell
   wsl --import Ubuntu-Restored D:\WSL\Ubuntu-Restored D:\Backup\ubuntu-backup.tar
   ```

3. 验证导入结果：
   ```powershell
   wsl --list --verbose
   ```

4. 导入的发行版默认以 root 用户登录，如需设置默认用户：
   在发行版内创建 `/etc/wsl.conf` 文件：
   ```bash
   [user]
   default=<用户名>
   ```

**注意事项**：
- 导入路径不要使用系统盘根目录
- 导入后需要手动配置默认用户
- 导入的发行版默认使用 WSL2，如需使用 WSL1 需手动转换

---

### 操作：exec — 在 WSL 中执行命令

**适用场景**：从 Windows 端在 WSL 中执行 Linux 命令。

**步骤**：

1. 在默认发行版中执行命令：
   ```powershell
   wsl -- <命令>
   ```
   示例：
   ```powershell
   wsl -- ls -la /home
   ```

2. 在指定发行版中执行命令：
   ```powershell
   wsl --distribution <发行版名称> -- <命令>
   ```

3. 以指定用户执行命令：
   ```powershell
   wsl --distribution <发行版名称> --user <用户名> -- <命令>
   ```

4. 在 WSL 中执行 Windows 路径的程序：
   ```powershell
   wsl -- <命令> 2>&1
   ```
   注意捕获标准输出和错误输出。

**路径转换**：
- Windows 路径转 WSL 路径：`wsl wslpath 'C:\Users\test'` → `/mnt/c/Users/test`
- WSL 路径转 Windows 路径：`wsl wslpath -w '/home/user'` → `\\wsl$\<发行版>\home\user`

---

### 操作：config — 配置 WSL 参数

**适用场景**：调整 WSL 的内存、处理器、网络等配置。

**步骤**：

1. 检查当前 `.wslconfig` 文件是否存在：
   ```powershell
   Test-Path "$env:USERPROFILE\.wslconfig"
   ```

2. 如果不存在，创建 `.wslconfig` 文件。文件路径为 `%USERPROFILE%\.wslconfig`。

3. `.wslconfig` 文件格式（INI 风格）：
   ```ini
   [wsl2]
   memory=4GB
   processors=2
   swap=2GB
   swapFile=C:\\temp\\wsl-swap.vhdx
   localhostForwarding=true
   nestedVirtualization=true
   ```

4. 常用配置项说明：

   | 配置项 | 说明 | 示例值 |
   |--------|------|--------|
   | `memory` | WSL2 可用内存 | `4GB`、`8GB`、`50%` |
   | `processors` | WSL2 可用处理器核心数 | `2`、`4` |
   | `swap` | 交换空间大小 | `2GB`、`0`（禁用） |
   | `swapFile` | 交换文件路径 | `C:\\temp\\wsl-swap.vhdx` |
   | `localhostForwarding` | 是否转发 localhost 端口 | `true` / `false` |
   | `nestedVirtualization` | 是否启用嵌套虚拟化 | `true` / `false` |
   | `guiApplications` | 是否启用 GUI 应用支持 | `true` / `false` |
   | `debugConsole` | 是否显示调试控制台 | `true` / `false` |

5. 修改配置后需要重启 WSL 才能生效：
   ```powershell
   wsl --shutdown
   wsl
   ```

6. 发行版级别配置（`/etc/wsl.conf`）通过 `exec` 操作在 WSL 内部修改：
   ```ini
   [boot]
   systemd=true

   [user]
   default=<用户名>

   [network]
   generateResolvConf=true

   [interop]
   enabled=true
   appendWindowsPath=true
   ```

---

### 操作：convert — 转换 WSL 版本

**适用场景**：将 WSL1 发行版转换为 WSL2。

**步骤**：

1. 检查当前发行版的 WSL 版本：
   ```powershell
   wsl --list --verbose
   ```

2. 转换指定发行版为 WSL2：
   ```powershell
   wsl --set-version <发行版名称> 2
   ```

3. 设置默认新安装的发行版使用 WSL2：
   ```powershell
   wsl --set-default-version 2
   ```

4. 验证转换结果：
   ```powershell
   wsl --list --verbose
   ```

**注意事项**：
- 转换过程可能需要几分钟
- 转换前确保已启用"虚拟机平台"功能
- WSL1 到 WSL2 的转换通常是安全的，但建议先备份

---

### 操作：check-version — 检查 WSL 版本

**适用场景**：确认发行版使用的 WSL 版本。

**步骤**：

1. 查看所有发行版及其 WSL 版本：
   ```powershell
   wsl --list --verbose
   ```

2. 查看 WSL 本身的版本信息：
   ```powershell
   wsl --version
   ```

---

## 通用注意事项

1. **权限要求**：
   - `install` 和 `uninstall` 操作需要管理员权限
   - 其他操作通常不需要管理员权限

2. **数据安全**：
   - 执行 `uninstall` 和 `stop` 前必须提醒用户保存数据
   - 重要操作前建议先 `export` 备份

3. **命令执行环境**：
   - 所有 PowerShell 命令在 Windows 端执行
   - `exec` 操作中的 Linux 命令在 WSL 内执行
   - 注意区分 Windows 路径和 Linux 路径格式

4. **错误处理**：
   - 如果命令执行失败，先检查错误信息
   - 常见错误及解决方案参见 `resources/wsl-troubleshooting.md`
   - 对于未知错误，建议用户执行 `wsl --status` 和 `wsl --version` 获取诊断信息

5. **操作确认**：
   - 破坏性操作（uninstall、stop、shutdown）执行前必须向用户确认
   - 确认信息中应包含操作的具体影响

6. **WSL1 与 WSL2 差异**：
   - WSL2 使用真正的 Linux 内核，兼容性更好
   - WSL2 需要虚拟机平台支持
   - WSL2 跨文件系统性能较 WSL1 差，建议在 WSL 文件系统内工作
