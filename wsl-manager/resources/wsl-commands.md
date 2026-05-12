# WSL 命令快速参考

## 基础命令

### wsl — 启动 / 执行

```powershell
wsl                                           # 启动默认发行版
wsl --distribution <名称>                     # 启动指定发行版
wsl --distribution <名称> --user <用户>       # 以指定用户启动
wsl --distribution <名称> --cd <路径>         # 在指定目录启动
wsl -- <命令>                                 # 在默认发行版执行命令
wsl --distribution <名称> -- <命令>           # 在指定发行版执行命令
wsl -d <名称> -- <命令>                       # -d 是 --distribution 的简写
wsl -u <用户> -- <命令>                       # -u 是 --user 的简写
wsl --exec <命令>                             # 执行命令（不经过 shell 解析）
wsl --shell-type standard -- <命令>           # 使用标准 shell 执行
wsl --shell-type login -- <命令>              # 使用登录 shell 执行
wsl --shell-type none -- <命令>               # 不使用 shell 直接执行
```

### wsl —install — 安装

```powershell
wsl --install                                 # 安装 WSL 和默认发行版(Ubuntu)
wsl --install --distribution <名称>           # 安装指定发行版
wsl --install --no-distribution               # 仅安装 WSL，不安装发行版
wsl --install --web-download                  # 从网络下载（绕过 Microsoft Store）
```

### wsl —list — 列出

```powershell
wsl --list                                    # 列出已安装发行版
wsl --list --verbose                          # 列出已安装发行版（含详细信息）
wsl --list --running                          # 仅列出运行中的发行版
wsl --list --online                           # 列出可安装的在线发行版
wsl -l -v                                     # 简写形式
wsl -l -o                                     # 列出在线发行版的简写
```

### wsl —set-version — 版本转换

```powershell
wsl --set-version <名称> <版本号>             # 转换发行版的 WSL 版本(1 或 2)
wsl --set-default-version <版本号>            # 设置新安装发行版的默认 WSL 版本
```

### wsl —set-default — 设置默认

```powershell
wsl --set-default <名称>                      # 设置默认发行版
```

### wsl —terminate / —shutdown — 关闭

```powershell
wsl --terminate <名称>                        # 关闭指定发行版
wsl --shutdown                                # 关闭所有运行中的发行版
wsl -t <名称>                                 # --terminate 的简写
```

### wsl —unregister — 卸载

```powershell
wsl --unregister <名称>                       # 注销（卸载）指定发行版
```

### wsl —export / —import — 导出导入

```powershell
wsl --export <名称> <输出路径>                # 导出发行版为 tar 文件
wsl --export <名称> <输出路径> --vhd          # 导出为 VHD 格式
wsl --import <名称> <安装路径> <tar路径>       # 从 tar 导入发行版
wsl --import <名称> <安装路径> <vhd路径> --vhd # 从 VHD 导入发行版
wsl --import-in-place <名称> <vhd路径>        # 就地注册 VHD 为发行版
```

### wsl —update — 更新

```powershell
wsl --update                                  # 更新 WSL 到最新版本
wsl --update --pre-release                    # 更新到预发布版本
wsl --update --status                         # 查看更新状态
wsl --update --rollback                       # 回滚到上一版本
```

### wsl —status / —version — 状态

```powershell
wsl --status                                  # 查看 WSL 运行状态
wsl --version                                 # 查看 WSL 版本信息
```

### wsl —manage — 管理（WSL2 专用）

```powershell
wsl --manage <名称> --set-sparse true         # 启用稀疏 VHD（自动回收磁盘空间）
wsl --manage <名称> --set-sparse false        # 禁用稀疏 VHD
```

## 路径转换工具

```bash
wslpath 'C:\Users\test'                       # Windows 路径 → WSL 路径
wslpath -w '/home/user'                       # WSL 路径 → Windows 路径
wslpath -u 'C:\Users\test'                    # Windows 路径 → WSL 路径（显式）
wslpath -m 'C:\Users\test'                    # Windows 路径 → 混合路径
```

## 网络访问

```text
从 Windows 访问 WSL 服务：localhost:<端口>
从 WSL 访问 Windows 服务：localhost:<端口> 或 $(cat /etc/resolv.conf | grep nameserver | awk '{print $2}')

WSL 文件系统在 Windows 中的路径：
\\wsl$\<发行版名称>\<路径>
\\wsl.localhost\<发行版名称>\<路径>

Windows 文件系统在 WSL 中的路径：
/mnt/c/  (C盘)
/mnt/d/  (D盘)
```

## .wslconfig 配置参考

文件位置：`%USERPROFILE%\.wslconfig`

```ini
[wsl2]
memory=4GB                    # 内存限制
processors=2                  # 处理器核心数
swap=2GB                      # 交换空间大小
swapFile=C:\\temp\\swap.vhdx  # 交换文件路径
localhostForwarding=true       # 转发 localhost 端口到 Windows
nestedVirtualization=true      # 嵌套虚拟化
guiApplications=true           # GUI 应用支持(WSLg)
debugConsole=false             # 调试控制台
reclaimMemory=true             # 自动回收内存

[experimental]
autoMemoryReclaim=gradual      # 自动回收内存（gradual/dropcache/disabled）
sparseVhd=true                 # 自动稀疏化 VHD
networkingMode=mirrored        # 镜像网络模式
hostAddressLoopback=true       # 允许 WSL 通过 127.0.0.1 访问 Windows
```

## /etc/wsl.conf 配置参考

文件位置：WSL 发行版内 `/etc/wsl.conf`

```ini
[boot]
systemd=true                   # 启用 systemd
command=<命令>                 # 启动时执行的命令

[user]
default=<用户名>               # 默认登录用户

[network]
generateResolvConf=true        # 自动生成 resolv.conf
generateHosts=true             # 自动生成 hosts

[interop]
enabled=true                   # 启用 Windows/Linux 互操作
appendWindowsPath=true         # 将 Windows PATH 追加到 Linux PATH

[automount]
enabled=true                   # 自动挂载 Windows 磁盘
root=/mnt/                     # 挂载根目录
options="metadata,umask=22,fmask=11"  # 挂载选项
mountFsTab=true                # 读取 /etc/fstab

[debug]
console=true                   # 启用调试控制台
```
