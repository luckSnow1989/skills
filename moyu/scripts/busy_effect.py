#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
看起来很忙的效果生成器
Busy Effect Generator - Make you look busy at work
"""

import random
import time
import sys
import os
from datetime import datetime
from typing import List, Optional


class BusyEffectGenerator:
    """看起来很忙的效果生成器"""
    
    def __init__(self):
        self.running = False
        self.stats = {
            "keystrokes": 0,
            "commands": 0,
            "files_opened": 0,
            "start_time": None
        }
    
    def typing_effect(self, text: str, speed: float = 0.03, with_sound: bool = False):
        """
        模拟打字效果
        
        Args:
            text: 要显示的文本
            speed: 打字速度（秒/字符）
            with_sound: 是否播放打字音效
        """
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            self.stats["keystrokes"] += 1
            time.sleep(speed)
        print()
    
    def terminal_busy_animation(self, duration: int = 60, scenario: str = "coding"):
        """
        终端忙碌动画
        
        Args:
            duration: 持续时间（秒）
            scenario: 场景类型 (coding/building/deploying/testing/debugging)
        """
        self.running = True
        self.stats["start_time"] = datetime.now()
        
        scenarios = {
            "coding": {
                "messages": [
                    "Writing function implementation...",
                    "Refactoring legacy code...",
                    "Adding error handling...",
                    "Optimizing algorithm...",
                    "Writing unit tests...",
                    "Updating documentation...",
                    "Fixing type annotations...",
                    "Importing modules..."
                ],
                "commands": [
                    "vim src/{file}",
                    "git diff --stat",
                    "pytest tests/",
                    "mypy src/",
                    "black src/",
                    "flake8 src/"
                ]
            },
            "building": {
                "messages": [
                    "Compiling TypeScript...",
                    "Bundling assets...",
                    "Minifying JavaScript...",
                    "Optimizing images...",
                    "Generating source maps...",
                    "Running post-build hooks..."
                ],
                "commands": [
                    "npm run build",
                    "webpack --mode production",
                    "tsc --noEmit",
                    "npm run lint",
                    "npm run test"
                ]
            },
            "deploying": {
                "messages": [
                    "Building Docker image...",
                    "Pushing to registry...",
                    "Updating Kubernetes deployment...",
                    "Waiting for rollout...",
                    "Running health checks...",
                    "Updating load balancer..."
                ],
                "commands": [
                    "docker build -t app:latest .",
                    "docker push registry/app:latest",
                    "kubectl apply -f k8s/",
                    "kubectl rollout status deployment/app",
                    "helm upgrade --install app ./chart"
                ]
            },
            "testing": {
                "messages": [
                    "Running unit tests...",
                    "Executing integration tests...",
                    "Checking code coverage...",
                    "Running E2E tests...",
                    "Validating API contracts...",
                    "Performance testing..."
                ],
                "commands": [
                    "pytest --cov=src tests/",
                    "jest --coverage",
                    "cypress run",
                    "k6 run load-test.js",
                    "newman run api-tests.json"
                ]
            },
            "debugging": {
                "messages": [
                    "Setting breakpoints...",
                    "Inspecting variables...",
                    "Analyzing stack trace...",
                    "Checking logs...",
                    "Reproducing issue...",
                    "Testing fix..."
                ],
                "commands": [
                    "tail -f logs/app.log",
                    "gdb ./app",
                    "curl -v http://localhost:8080/api",
                    "netstat -tlnp",
                    "lsof -i :8080"
                ]
            }
        }
        
        scene = scenarios.get(scenario, scenarios["coding"])
        frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        
        print(f"🚀 Starting {scenario} session...")
        print(f"⏱️  Duration: {duration} seconds")
        print("Press Ctrl+C to stop\n")
        
        end_time = time.time() + duration
        frame_idx = 0
        last_update = 0
        current_message = random.choice(scene["messages"])
        
        try:
            while time.time() < end_time and self.running:
                frame = frames[frame_idx % len(frames)]
                
                # 每3秒更新一次消息
                if time.time() - last_update > 3:
                    current_message = random.choice(scene["messages"])
                    last_update = time.time()
                    
                    # 偶尔显示命令
                    if random.random() > 0.7:
                        cmd = random.choice(scene["commands"])
                        file_name = random.choice(["app.py", "utils.js", "config.yaml", "models.py", "api.ts"])
                        print(f"\n$ {cmd.format(file=file_name)}")
                        self.stats["commands"] += 1
                
                # 显示进度
                remaining = int(end_time - time.time())
                progress_bar = self._generate_progress_bar(duration - remaining, duration)
                
                sys.stdout.write(f"\r{frame} {current_message} {progress_bar}")
                sys.stdout.flush()
                
                frame_idx += 1
                time.sleep(0.1)
                
        except KeyboardInterrupt:
            pass
        finally:
            self.running = False
            sys.stdout.write("\r" + " " * 80 + "\r")
            print(f"✅ Session completed!")
            self._print_stats()
    
    def _generate_progress_bar(self, current: int, total: int, length: int = 20) -> str:
        """生成进度条"""
        progress = current / total if total > 0 else 0
        filled = int(length * progress)
        bar = "█" * filled + "░" * (length - filled)
        percentage = int(progress * 100)
        return f"[{bar}] {percentage}%"
    
    def _print_stats(self):
        """打印统计信息"""
        if self.stats["start_time"]:
            duration = (datetime.now() - self.stats["start_time"]).total_seconds()
            print(f"\n📊 Session Stats:")
            print(f"   Duration: {duration:.1f}s")
            print(f"   Keystrokes: {self.stats['keystrokes']}")
            print(f"   Commands: {self.stats['commands']}")
            print(f"   Productivity: ████████████████████ 100% 😉")
    
    def code_scroll_effect(self, language: str = "python", duration: int = 30):
        """
        代码滚动效果
        
        Args:
            language: 编程语言
            duration: 持续时间
        """
        self.running = True
        end_time = time.time() + duration
        
        code_snippets = self._get_code_snippets(language)
        
        print(f"💻 Code Review Mode ({language})")
        print("=" * 60)
        
        try:
            while time.time() < end_time and self.running:
                # 清屏（Unix/Linux/Mac）
                if os.name == 'posix':
                    os.system('clear')
                else:
                    os.system('cls')
                
                print(f"💻 Code Review Mode ({language})")
                print("=" * 60)
                
                # 随机显示代码片段
                snippet = random.choice(code_snippets)
                lines = snippet.split('\n')
                
                # 显示部分代码（模拟滚动）
                start_idx = random.randint(0, max(0, len(lines) - 20))
                for i, line in enumerate(lines[start_idx:start_idx + 20]):
                    line_num = start_idx + i + 1
                    print(f"{line_num:4d} | {line}")
                
                print("=" * 60)
                print(f"⏱️  Remaining: {int(end_time - time.time())}s | Press Ctrl+C to stop")
                
                time.sleep(random.uniform(2, 4))
                
        except KeyboardInterrupt:
            pass
        finally:
            self.running = False
            print("\n✅ Code review completed!")
    
    def _get_code_snippets(self, language: str) -> List[str]:
        """获取代码片段"""
        snippets = {
            "python": '''
def complex_data_processing(data, config=None):
    """Process data with advanced algorithms"""
    if config is None:
        config = DEFAULT_CONFIG
    
    results = []
    for item in data:
        try:
            processed = transform_item(item, config)
            if validate_result(processed):
                results.append(processed)
        except ValidationError as e:
            logger.warning(f"Validation failed: {e}")
            continue
    
    return optimize_results(results)

class DataPipeline:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.metrics = MetricsCollector()
    
    async def process_stream(self):
        async for batch in self.source.read_batches():
            transformed = await self.transform(batch)
            await self.destination.write(transformed)
            self.metrics.record_batch(len(batch))
''',
            "javascript": '''
const processUserData = async (userId, options = {}) => {
  try {
    const cacheKey = `user:${userId}`;
    let data = await cache.get(cacheKey);
    
    if (!data) {
      data = await db.users.findById(userId);
      await cache.set(cacheKey, data, { ttl: 3600 });
    }
    
    const processed = await transformUserData(data, options);
    return { success: true, data: processed };
  } catch (error) {
    logger.error(`Failed to process user ${userId}:`, error);
    return { success: false, error: error.message };
  }
};

class UserManager extends EventEmitter {
  constructor(config) {
    super();
    this.config = config;
    this.users = new Map();
  }
  
  async initialize() {
    await this.loadUsers();
    this.emit('ready');
  }
''',
            "java": '''
@Service
public class OrderProcessingService {
    @Autowired
    private OrderRepository orderRepository;
    
    @Autowired
    private PaymentGateway paymentGateway;
    
    @Transactional
    public OrderResult processOrder(OrderRequest request) {
        log.info("Processing order: {}", request.getOrderId());
        
        Order order = orderRepository.findById(request.getOrderId())
            .orElseThrow(() -> new OrderNotFoundException("Order not found"));
        
        PaymentResult payment = paymentGateway.charge(
            order.getTotalAmount(),
            request.getPaymentMethod()
        );
        
        if (payment.isSuccess()) {
            order.setStatus(OrderStatus.CONFIRMED);
            orderRepository.save(order);
            return OrderResult.success(order);
        }
        
        return OrderResult.failure(payment.getErrorMessage());
    }
}
''',
            "go": '''
type OrderProcessor struct {
    db     *sql.DB
    cache  *redis.Client
    logger *zap.Logger
}

func NewOrderProcessor(db *sql.DB, cache *redis.Client) *OrderProcessor {
    return &OrderProcessor{
        db:     db,
        cache:  cache,
        logger: zap.L(),
    }
}

func (p *OrderProcessor) Process(ctx context.Context, orderID string) error {
    p.logger.Info("processing order", zap.String("id", orderID))
    
    order, err := p.getOrder(ctx, orderID)
    if err != nil {
        return fmt.Errorf("failed to get order: %w", err)
    }
    
    if err := p.validateOrder(order); err != nil {
        return fmt.Errorf("order validation failed: %w", err)
    }
    
    return p.updateOrderStatus(ctx, orderID, StatusProcessing)
}
'''
        }
        
        return [snippets.get(language, snippets["python"])]
    
    def log_monitoring_effect(self, duration: int = 30, log_type: str = "app"):
        """
        日志监控效果
        
        Args:
            duration: 持续时间
            log_type: 日志类型 (app/system/access/error)
        """
        self.running = True
        end_time = time.time() + duration
        
        log_generators = {
            "app": self._generate_app_logs,
            "system": self._generate_system_logs,
            "access": self._generate_access_logs,
            "error": self._generate_error_logs
        }
        
        generator = log_generators.get(log_type, self._generate_app_logs)
        
        print(f"📊 Log Monitor ({log_type})")
        print("=" * 80)
        print("Press Ctrl+C to stop\n")
        
        try:
            while time.time() < end_time and self.running:
                log_line = generator()
                print(log_line)
                time.sleep(random.uniform(0.1, 0.5))
        except KeyboardInterrupt:
            pass
        finally:
            self.running = False
            print("\n✅ Log monitoring stopped")
    
    def _generate_app_logs(self) -> str:
        """生成应用日志"""
        levels = ["INFO", "DEBUG", "WARN"]
        services = ["UserService", "OrderService", "PaymentService", "NotificationService", "CacheManager"]
        actions = [
            "Processing request",
            "Cache hit",
            "Database query executed",
            "Event published",
            "Message consumed",
            "Authentication successful",
            "Data synchronized"
        ]
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        level = random.choice(levels)
        service = random.choice(services)
        action = random.choice(actions)
        id = random.randint(10000, 99999)
        duration = random.randint(5, 500)
        
        return f"{timestamp} [{level}] {service} - {action}: id={id} duration={duration}ms"
    
    def _generate_system_logs(self) -> str:
        """生成系统日志"""
        components = ["kernel", "systemd", "docker", "nginx", "postgres"]
        messages = [
            "Service started successfully",
            "Memory usage: 45%",
            "CPU load: 2.34",
            "Disk I/O: normal",
            "Network interface up",
            "Process forked",
            "Signal received: SIGTERM"
        ]
        
        timestamp = datetime.now().strftime("%b %d %H:%M:%S")
        component = random.choice(components)
        message = random.choice(messages)
        
        return f"{timestamp} {component}[{random.randint(1000, 9999)}]: {message}"
    
    def _generate_access_logs(self) -> str:
        """生成访问日志"""
        methods = ["GET", "POST", "PUT", "DELETE", "PATCH"]
        paths = ["/api/users", "/api/orders", "/api/products", "/api/auth", "/health"]
        status_codes = [200, 201, 204, 301, 304, 400, 401, 403, 404, 500]
        
        timestamp = datetime.now().strftime("%d/%b/%Y:%H:%M:%S +0000")
        method = random.choice(methods)
        path = random.choice(paths)
        status = random.choices(status_codes, weights=[30, 20, 10, 5, 5, 10, 5, 5, 5, 5])[0]
        size = random.randint(100, 5000)
        duration = random.randint(10, 1000)
        
        return f'127.0.0.1 - - [{timestamp}] "{method} {path} HTTP/1.1" {status} {size} "-" "Mozilla/5.0" {duration}'
    
    def _generate_error_logs(self) -> str:
        """生成错误日志"""
        errors = [
            "Connection timeout after 30000ms",
            "Failed to connect to database",
            "Invalid JSON in request body",
            "Authentication token expired",
            "Rate limit exceeded",
            "Resource not found",
            "Validation failed: email required"
        ]
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error = random.choice(errors)
        stack_frames = random.randint(3, 10)
        
        return f"{timestamp} [ERROR] {error}\n  at {random.choice(['app.js', 'server.js', 'api.ts'])}:{random.randint(1, 500)}:{random.randint(1, 80)}"
    
    def multi_window_effect(self, duration: int = 45):
        """
        多窗口切换效果
        
        Args:
            duration: 持续时间
        """
        self.running = True
        end_time = time.time() + duration
        
        windows = [
            ("📝 VS Code", "Editing src/components/Dashboard.tsx"),
            ("🌐 Chrome", "localhost:3000/dashboard"),
            ("💻 Terminal", "npm run dev"),
            ("📊 DataGrip", "Query: SELECT * FROM users"),
            ("🔍 Figma", "Design System v2.0"),
            ("📋 Notion", "Sprint Planning Q4"),
        ]
        
        print("🖥️  Multi-Window Workflow Simulation")
        print("=" * 60)
        print("Press Ctrl+C to stop\n")
        
        try:
            while time.time() < end_time and self.running:
                window = random.choice(windows)
                print(f"\n┌{'─' * 58}┐")
                print(f"│ {window[0]:<56} │")
                print(f"├{'─' * 58}┤")
                print(f"│ {'Working on: ' + window[1]:<56} │")
                print(f"└{'─' * 58}┘")
                
                time.sleep(random.uniform(3, 8))
                
        except KeyboardInterrupt:
            pass
        finally:
            self.running = False
            print("\n✅ Window switching simulation completed")
    
    def dashboard_monitoring(self, duration: int = 60):
        """
        监控面板效果
        
        Args:
            duration: 持续时间
        """
        self.running = True
        end_time = time.time() + duration
        
        print("📊 System Monitoring Dashboard")
        print("=" * 70)
        print("Press Ctrl+C to stop\n")
        
        try:
            while time.time() < end_time and self.running:
                # 清屏
                if os.name == 'posix':
                    os.system('clear')
                else:
                    os.system('cls')
                
                print("📊 System Monitoring Dashboard")
                print("=" * 70)
                
                # CPU 使用率
                cpu = random.randint(20, 85)
                cpu_bar = "█" * (cpu // 5) + "░" * (20 - cpu // 5)
                print(f"\n💻 CPU Usage: [{cpu_bar}] {cpu}%")
                
                # 内存使用
                mem = random.randint(40, 75)
                mem_bar = "█" * (mem // 5) + "░" * (20 - mem // 5)
                print(f"🧠 Memory:    [{mem_bar}] {mem}%")
                
                # 磁盘使用
                disk = random.randint(60, 90)
                disk_bar = "█" * (disk // 5) + "░" * (20 - disk // 5)
                print(f"💾 Disk:      [{disk_bar}] {disk}%")
                
                # 网络
                net_in = random.randint(1, 50)
                net_out = random.randint(1, 30)
                print(f"\n🌐 Network: ↓ {net_in} MB/s  ↑ {net_out} MB/s")
                
                # 活跃进程
                print(f"\n🔥 Active Processes: {random.randint(80, 150)}")
                print(f"📦 Container Count: {random.randint(5, 20)}")
                print(f"⚡ API Requests/min: {random.randint(1000, 5000)}")
                
                # 服务状态
                print(f"\n✅ Services Status:")
                services = ["API Gateway", "User Service", "Order Service", "Payment Service", "Notification Service"]
                for service in services:
                    status = "🟢" if random.random() > 0.1 else "🟡"
                    latency = random.randint(10, 200)
                    print(f"   {status} {service:<25} {latency}ms")
                
                print(f"\n⏱️  Remaining: {int(end_time - time.time())}s | Press Ctrl+C to stop")
                
                time.sleep(2)
                
        except KeyboardInterrupt:
            pass
        finally:
            self.running = False
            print("\n✅ Monitoring stopped")


def main():
    """命令行入口"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="看起来很忙的效果生成器",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python busy_effect.py --type terminal --scenario coding 60    # 终端忙碌动画60秒
  python busy_effect.py --type code --language python 30        # 代码滚动效果
  python busy_effect.py --type logs --log-type app 45           # 日志监控效果
  python busy_effect.py --type windows 30                       # 多窗口切换效果
  python busy_effect.py --type dashboard 60                     # 监控面板效果
        """
    )
    
    parser.add_argument("--type", "-t", type=str, default="terminal",
                       choices=["terminal", "code", "logs", "windows", "dashboard"],
                       help="效果类型")
    parser.add_argument("--scenario", "-s", type=str, default="coding",
                       choices=["coding", "building", "deploying", "testing", "debugging"],
                       help="场景类型（仅用于terminal类型）")
    parser.add_argument("--language", "-l", type=str, default="python",
                       choices=["python", "javascript", "java", "go"],
                       help="编程语言（仅用于code类型）")
    parser.add_argument("--log-type", type=str, default="app",
                       choices=["app", "system", "access", "error"],
                       help="日志类型（仅用于logs类型）")
    parser.add_argument("duration", nargs="?", type=int, default=30,
                       help="持续时间（秒，默认30）")
    
    args = parser.parse_args()
    
    generator = BusyEffectGenerator()
    
    if args.type == "terminal":
        generator.terminal_busy_animation(duration=args.duration, scenario=args.scenario)
    elif args.type == "code":
        generator.code_scroll_effect(language=args.language, duration=args.duration)
    elif args.type == "logs":
        generator.log_monitoring_effect(duration=args.duration, log_type=args.log_type)
    elif args.type == "windows":
        generator.multi_window_effect(duration=args.duration)
    elif args.type == "dashboard":
        generator.dashboard_monitoring(duration=args.duration)


if __name__ == "__main__":
    main()
