---
name: moyu
description: "摸鱼助手 - 帮助不同职业的人在公司看起来忙碌的技能。支持程序员、设计师、产品经理、运营、HR、财务等多种职业的摸鱼场景，生成看起来很忙的工作界面和任务"
license: Proprietary
---

# 摸鱼助手 (Moyu Assistant)

一个帮助职场人士在工作中看起来忙碌的技能。支持多种职业的摸鱼场景，生成专业的工作界面、任务列表和忙碌状态。

## 支持的摸鱼职业

| 职业 | 摸鱼场景 | 忙碌效果 |
|------|----------|----------|
| 程序员 | 代码编辑器、终端、日志监控 | 疯狂敲代码、编译中、调试中 |
| 设计师 | Figma/Sketch界面、设计稿 | 精细调整、图层管理、配色方案 |
| 产品经理 | PRD文档、需求分析、原型图 | 写文档、画流程图、开会中 |
| 运营 | 数据报表、活动策划、社媒管理 | 数据分析、内容编辑、排期表 |
| HR | 简历筛选、面试安排、员工档案 | 看简历、整理档案、安排面试 |
| 财务 | Excel表格、财务报表、发票处理 | 核对数据、做报表、审计中 |
| 销售 | CRM系统、客户跟进、报价单 | 联系客户、更新商机、做方案 |
| 行政 | 会议安排、办公用品、档案管理 | 整理会议室、采购清单、日程表 |

## 快速使用

### 命令行使用

```bash
# 生成程序员摸鱼界面
python3 moyu/scripts/moyu.py --job programmer --duration 30

# 生成设计师摸鱼界面
python3 moyu/scripts/moyu.py --job designer --mode "ui-design"

# 生成产品经理摸鱼文档
python3 moyu/scripts/moyu.py --job pm --output prd.docx

# 查看所有支持的摸鱼模式
python3 moyu/scripts/moyu.py --list
```

### Python API 使用

```python
from moyu.scripts.moyu import MoyuGenerator

# 创建摸鱼生成器
generator = MoyuGenerator(job="programmer")

# 生成看起来很忙的代码
busy_code = generator.generate_busy_code(language="python", lines=50)

# 生成终端输出
terminal_output = generator.generate_terminal_output(command="deploy", status="running")

# 生成工作状态
work_status = generator.generate_work_status(task="debugging", progress=65)
```

## 摸鱼模式详解

### 程序员摸鱼

**模式选项：**
- `coding` - 写代码（默认）
- `debugging` - 调试程序
- `building` - 编译构建
- `reviewing` - 代码审查
- `terminal` - 终端操作

**生成内容：**
- 看起来很专业的代码片段
- 复杂的终端命令和输出
- 调试日志和错误信息
- Git操作记录
- 系统监控界面

### 设计师摸鱼

**模式选项：**
- `ui-design` - UI设计
- `graphic` - 平面设计
- `prototyping` - 原型制作
- `branding` - 品牌设计

**生成内容：**
- 设计规范文档
- 配色方案说明
- 图层命名列表
- 设计评审意见
- 用户调研报告

### 产品经理摸鱼

**模式选项：**
- `prd` - 写需求文档
- `analysis` - 数据分析
- `roadmap` - 产品规划
- `meeting` - 会议记录

**生成内容：**
- PRD文档片段
- 用户故事列表
- 功能优先级矩阵
- 竞品分析报告
- 会议纪要模板

### 运营摸鱼

**模式选项：**
- `data` - 数据分析
- `content` - 内容运营
- `campaign` - 活动策划
- `social` - 社媒运营

**生成内容：**
- 数据报表
- 内容排期表
- 活动策划案
- 用户增长分析
- 竞品监控报告

### 其他职业

HR、财务、销售、行政等职业同样支持多种摸鱼模式，生成对应的专业文档和工作界面。

## 看起来很忙的效果

### 视觉忙碌效果

1. **快速打字效果** - 模拟高速输入代码/文档
2. **频繁切换窗口** - 在多个工作界面间切换
3. **滚动浏览** - 长文档/代码的快速滚动
4. **弹窗提示** - 工作通知、提醒、警告
5. **进度条动画** - 显示任务进行中

### 状态指示器

- 🟢 在线工作中
- 🟡 会议中/请勿打扰
- 🔴 紧急处理中
- ⏳ 等待响应中
- 💭 思考中

## 高级功能

### 自定义摸鱼内容

```python
# 自定义代码片段
generator.add_custom_snippet("python", """
def complex_algorithm(data):
    # 这是一个看起来很复杂的算法
    result = process_data(data)
    return optimize_result(result)
""")

# 自定义终端命令
generator.add_terminal_command("deploy", """
Building project...
[████████████████████] 100% 
Deploying to production...
Successfully deployed!
""")
```

### 智能切换

```python
# 设置自动切换间隔
generator.set_auto_switch(interval=300)  # 每5分钟切换一次

# 添加切换规则
generator.add_switch_rule(
    from_mode="coding",
    to_mode="terminal",
    trigger="after_10_minutes"
)
```

### 老板键

一键切换到"安全"界面：

```python
# 设置老板键
generator.set_boss_key(key="ctrl+shift+b")

# 老板键触发时显示的内容
generator.set_boss_screen(content="工作周报.docx")
```

## 注意事项

1. **适度使用** - 摸鱼是为了调节工作状态，不要影响正常工作
2. **注意场合** - 在合适的时机使用，避免在重要会议或紧急任务时使用
3. **保持专业** - 生成的内容要符合职业特点，不要太过离谱
4. **及时切换** - 发现有人靠近时及时切换到工作界面

## 免责声明

本技能仅供娱乐和学习使用，请合理安排工作时间，认真完成工作任务。过度摸鱼可能影响工作效率和职业发展。

## 依赖

- Python 3.7+
- 可选: `rich` - 用于美化终端输出
- 可选: `colorama` - Windows终端颜色支持
