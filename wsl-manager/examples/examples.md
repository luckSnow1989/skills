# WSL 管理技能使用示例

## 示例 1：首次安装 WSL

### 用户输入
> 帮我安装 WSL，我要用 Ubuntu

### 智能体执行步骤

1. 检查操作系统版本：
   ```powershell
   [System.Environment]::OSVersion.Version
   ```

2. 检查管理员权限：
   ```powershell
   ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
   ```

3. 安装 WSL 和 Ubuntu：
   ```powershell
   wsl --install --distribution Ubuntu
   ```

4. 提示用户重启计算机

5. 重启后引导用户完成 Ubuntu 初始化（创建用户名和密码）

---

## 示例 2：安装额外的发行版

### 用户输入
> 我想再安装一个 Debian

### 智能体执行步骤

1. 查看可用发行版：
   ```powershell
   wsl --list --online
   ```

2. 安装 Debian：
   ```powershell
   wsl --install --distribution Debian
   ```

3. 安装完成后验证：
   ```powershell
   wsl --list --verbose
   ```

---

## 示例 3：查看 WSL 状态

### 用户输入
> 看看我有哪些 WSL 发行版

### 智能体执行步骤

1. 列出所有发行版详细信息：
   ```powershell
   wsl --list --verbose
   ```

2. 查看运行状态：
   ```powershell
   wsl --status
   ```

### 预期输出示例
```
  NAME            STATE           VERSION
* Ubuntu          Running         2
  Debian          Stopped         2
  Ubuntu-20.04    Stopped         1
```

---

## 示例 4：启动和关闭 WSL

### 用户输入
> 启动 Debian，然后帮我关掉 Ubuntu

### 智能体执行步骤

1. 启动 Debian：
   ```powershell
   wsl --distribution Debian
   ```

2. 关闭 Ubuntu：
   ```powershell
   wsl --terminate Ubuntu
   ```

3. 验证状态：
   ```powershell
   wsl --list --running
   ```

---

## 示例 5：在 WSL 中执行命令

### 用户输入
> 在 Ubuntu 里查看磁盘使用情况

### 智能体执行步骤

```powershell
wsl --distribution Ubuntu -- df -h
```

### 预期输出示例
```
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdb        251G   12G  227G   5% /
tmpfs           3.2G     0  3.2G   0% /mnt/wsl
tools           476G  286G  191G  60% /init
C:\             476G  286G  191G  60% /mnt/c
D:\             932G  456G  477G  49% /mnt/d
```

---

## 示例 6：备份和恢复发行版

### 用户输入
> 把我的 Ubuntu 备份一下，我要换台电脑

### 智能体执行步骤

1. 关闭 Ubuntu 确保数据一致性：
   ```powershell
   wsl --terminate Ubuntu
   ```

2. 导出 Ubuntu：
   ```powershell
   wsl --export Ubuntu D:\Backup\ubuntu-backup.tar
   ```

3. 验证导出文件：
   ```powershell
   Get-Item D:\Backup\ubuntu-backup.tar | Select-Object Name, @{N='Size(GB)';E={[math]::Round($_.Length/1GB,2)}}, LastWriteTime
   ```

### 在新电脑上恢复

```powershell
wsl --import Ubuntu D:\WSL\Ubuntu D:\Backup\ubuntu-backup.tar
```

---

## 示例 7：配置 WSL 资源限制

### 用户输入
> WSL 占用太多内存了，限制到 4GB

### 智能体执行步骤

1. 检查当前配置：
   ```powershell
   if (Test-Path "$env:USERPROFILE\.wslconfig") { Get-Content "$env:USERPROFILE\.wslconfig" } else { Write-Output "文件不存在" }
   ```

2. 创建或更新 `.wslconfig`：
   ```powershell
   $wslConfig = @"
   [wsl2]
   memory=4GB
   processors=2
   swap=2GB
   "@
   Set-Content -Path "$env:USERPROFILE\.wslconfig" -Value $wslConfig -Encoding UTF8
   ```

3. 重启 WSL 使配置生效：
   ```powershell
   wsl --shutdown
   ```

4. 启动 WSL 验证：
   ```powershell
   wsl
   ```

---

## 示例 8：转换 WSL 版本

### 用户输入
> 把我的 Ubuntu-20.04 从 WSL1 升级到 WSL2

### 智能体执行步骤

1. 检查当前版本：
   ```powershell
   wsl --list --verbose
   ```

2. 确认虚拟机平台已启用：
   ```powershell
   Get-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform | Select-Object State
   ```

3. 执行转换：
   ```powershell
   wsl --set-version Ubuntu-20.04 2
   ```

4. 验证转换结果：
   ```powershell
   wsl --list --verbose
   ```

---

## 示例 9：卸载发行版

### 用户输入
> 我不需要 Debian 了，帮我删掉

### 智能体执行步骤

1. 确认发行版存在：
   ```powershell
   wsl --list --verbose
   ```

2. **向用户确认**：
   > ⚠️ 卸载 Debian 将永久删除该发行版中的所有文件和数据，此操作不可逆。确认是否继续？

3. 用户确认后执行：
   ```powershell
   wsl --unregister Debian
   ```

4. 验证卸载结果：
   ```powershell
   wsl --list --verbose
   ```

---

## 示例 10：启用镜像网络模式

### 用户输入
> WSL 网络有问题，帮我配置镜像网络模式

### 智能体执行步骤

1. 检查 Windows 版本（镜像网络需要 Windows 11 22H2+）：
   ```powershell
   [System.Environment]::OSVersion.Version.Build
   ```

2. 更新 `.wslconfig`：
   ```powershell
   $configPath = "$env:USERPROFILE\.wslconfig"
   $config = @"
   [wsl2]
   memory=4GB

   [experimental]
   networkingMode=mirrored
   hostAddressLoopback=true
   "@
   Set-Content -Path $configPath -Value $config -Encoding UTF8
   ```

3. 重启 WSL：
   ```powershell
   wsl --shutdown
   wsl
   ```

4. 验证网络配置：
   ```powershell
   wsl -- ip addr show eth0
   ```
