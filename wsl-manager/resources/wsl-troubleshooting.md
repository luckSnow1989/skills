# WSL 常见问题排查指南

## 安装类问题

### 错误：0x80070003 或 0x80070002

**原因**：WSL 功能未正确启用。

**解决方案**：
```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```
执行后重启计算机。

### 错误：0x80040324

**原因**：Windows 版本不支持 WSL2。

**解决方案**：
1. 检查 Windows 版本：`winver`
2. WSL2 需要 Windows 10 版本 1903 或更高（内部版本 18362+）
3. 升级 Windows 或使用 WSL1：`wsl --set-default-version 1`

### 错误：WslRegisterDistribution failed with error 0x8007019e

**原因**：未启用"适用于 Linux 的 Windows 子系统"功能。

**解决方案**：
```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```
重启计算机后重试。

### 错误：WslRegisterDistribution failed with error 0x80370102

**原因**：未启用虚拟机平台功能，或 BIOS 中未启用虚拟化。

**解决方案**：
1. 启用虚拟机平台：
   ```powershell
   dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
   ```
2. 检查 BIOS 虚拟化是否启用（Intel VT-x / AMD-V）
3. 重启计算机

### 安装时下载速度慢或失败

**原因**：网络问题，Microsoft Store 下载受限。

**解决方案**：
1. 使用 `--web-download` 参数绕过 Store：
   ```powershell
   wsl --install --web-download
   ```
2. 手动下载发行版：
   - 访问 https://aka.ms/wslstore
   - 或使用 `Invoke-WebRequest` 直接下载 appx 包
3. 配置代理（如需要）

---

## 运行类问题

### WSL 启动非常慢

**可能原因及解决方案**：

1. **Windows Defender 扫描**：
   - 将 WSL 文件系统路径添加到排除列表：
   ```powershell
   Add-MpPreference -ExclusionPath "$env:LOCALAPPDATA\Packages"
   Add-MpPreference -ExclusionPath "\\wsl$"
   Add-MpPreference -ExclusionProcess "vmmem"
   ```

2. **内存不足**：
   - 在 `.wslconfig` 中限制内存：
   ```ini
   [wsl2]
   memory=4GB
   ```

3. **启动项过多**：
   - 检查 `/etc/wsl.conf` 中的 `[boot]` 配置
   - 禁用不必要的 systemd 服务

### 错误：0x8007007e

**原因**：WSL 组件损坏。

**解决方案**：
```powershell
wsl --update
wsl --shutdown
```
如果仍然失败，尝试重新安装 WSL：
```powershell
wsl --unregister <发行版名称>
wsl --install --distribution <发行版名称>
```

### Vmmem 进程占用大量内存/CPU

**原因**：WSL2 虚拟机未限制资源使用。

**解决方案**：
1. 创建或编辑 `%USERPROFILE%\.wslconfig`：
   ```ini
   [wsl2]
   memory=4GB
   processors=2
   swap=2GB
   ```
2. 关闭并重启 WSL：
   ```powershell
   wsl --shutdown
   ```
3. 启用自动内存回收（实验性功能）：
   ```ini
   [experimental]
   autoMemoryReclaim=gradual
   ```

### WSL 磁盘空间不释放

**原因**：WSL2 的 VHD 文件不会自动缩小。

**解决方案**：
1. 启用稀疏 VHD：
   ```powershell
   wsl --manage <发行版名称> --set-sparse true
   ```
2. 手动压缩 VHD：
   ```powershell
   wsl --shutdown
   diskpart
   # 在 diskpart 中：
   select vdisk file="<VHD路径>"
   compact vdisk
   ```
3. 或在 `.wslconfig` 中配置：
   ```ini
   [experimental]
   sparseVhd=true
   ```

---

## 网络类问题

### WSL 无法访问网络

**解决方案**：

1. 检查 DNS 配置：
   ```bash
   cat /etc/resolv.conf
   ```
   如果 nameserver 不正确，手动设置：
   ```bash
   echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
   ```

2. 禁用自动生成 resolv.conf，在 `/etc/wsl.conf` 中：
   ```ini
   [network]
   generateResolvConf=false
   ```

3. 使用镜像网络模式（Windows 11 22H2+）：
   ```ini
   [experimental]
   networkingMode=mirrored
   ```

### Windows 无法访问 WSL 中的服务

**解决方案**：

1. 确认 localhost 转发已启用：
   ```ini
   [wsl2]
   localhostForwarding=true
   ```

2. 检查 WSL 防火墙：
   ```bash
   sudo ufw status
   sudo ufw allow <端口号>
   ```

3. 使用 Windows 路径直接访问：
   ```text
   \\wsl$\<发行版名称>\<路径>
   ```

### 代理配置问题

**解决方案**：

1. 获取 Windows 主机 IP：
   ```bash
   export WIN_IP=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}')
   ```

2. 设置代理：
   ```bash
   export http_proxy="http://${WIN_IP}:<代理端口>"
   export https_proxy="http://${WIN_IP}:<代理端口>"
   ```

3. 或使用镜像网络模式后直接使用 `127.0.0.1`：
   ```bash
   export http_proxy="http://127.0.0.1:<代理端口>"
   export https_proxy="http://127.0.0.1:<代理端口>"
   ```

---

## 文件系统类问题

### 跨文件系统性能差

**原因**：WSL2 访问 Windows 文件系统（/mnt/c/）性能显著低于访问 WSL 文件系统。

**解决方案**：
1. 将项目文件放在 WSL 文件系统内（`/home/<用户>/`）
2. 从 Windows 通过 `\\wsl$\<发行版>\` 路径访问 WSL 文件
3. 禁用 Windows Defender 对 WSL 路径的实时扫描

### 文件权限问题

**原因**：Windows 和 Linux 文件权限模型不同。

**解决方案**：

1. 配置自动挂载选项，在 `/etc/wsl.conf` 中：
   ```ini
   [automount]
   options="metadata,umask=22,fmask=11"
   ```

2. `metadata` 选项启用后，WSL 可以正确设置和读取 Windows 文件系统上的 Linux 权限

### 符号链接不工作

**解决方案**：
1. 确保开发者模式已启用（Windows 设置 → 更新和安全 → 开发者选项）
2. 或以管理员权限运行 WSL

---

## 版本转换问题

### WSL1 转 WSL2 失败

**解决方案**：
1. 确认虚拟机平台已启用：
   ```powershell
   Get-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform
   ```
2. 如果未启用：
   ```powershell
   dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
   ```
3. 更新 WSL 内核：
   ```powershell
   wsl --update
   ```
4. 重启后重试转换

---

## systemd 相关问题

### systemd 未运行

**检查方法**：
```bash
systemctl status
ps -p 1 -o comm=
```
如果输出不是 `systemd`，说明未启用。

**解决方案**：

1. 在 `/etc/wsl.conf` 中添加：
   ```ini
   [boot]
   systemd=true
   ```

2. 重启 WSL：
   ```powershell
   wsl --terminate <发行版名称>
   ```

3. 确认 WSL 版本支持 systemd（需要 WSL2 且内核版本 5.15+）

### Docker 服务无法启动

**解决方案**：
1. 确认 systemd 已启用
2. 检查 Docker 安装状态：
   ```bash
   sudo systemctl status docker
   sudo journalctl -u docker
   ```
3. 考虑使用 Docker Desktop for Windows（集成 WSL2 后端）

---

## 通用排查流程

当遇到未知 WSL 问题时，按以下步骤排查：

1. **收集基本信息**：
   ```powershell
   wsl --version
   wsl --status
   wsl --list --verbose
   ```

2. **尝试重启 WSL**：
   ```powershell
   wsl --shutdown
   wsl
   ```

3. **更新 WSL**：
   ```powershell
   wsl --update
   ```

4. **检查 Windows 事件日志**：
   - 事件查看器 → 应用程序和服务日志 → Microsoft → Windows → WSL

5. **检查 Windows 功能状态**：
   ```powershell
   Get-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
   Get-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform
   ```

6. **检查 Hyper-V 状态**（如适用）：
   ```powershell
   Get-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V
   ```

7. **查看 WSL 日志**：
   ```powershell
   wsl --shutdown
   wsl --debug-console
   ```

8. **终极方案**：重置 WSL
   ```powershell
   # 备份数据后
   wsl --unregister <发行版名称>
   wsl --install --distribution <发行版名称>
   ```
