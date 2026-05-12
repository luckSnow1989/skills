#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
摸鱼助手 - 帮助不同职业的人在公司看起来忙碌
Moyu Assistant - Help different professionals look busy at work
"""

import random
import time
import argparse
import sys
from datetime import datetime
from typing import List, Dict, Optional


class MoyuGenerator:
    """摸鱼内容生成器"""
    
    # 支持的摸鱼职业
    JOBS = {
        "programmer": "程序员",
        "designer": "设计师",
        "pm": "产品经理",
        "operation": "运营",
        "hr": "HR",
        "finance": "财务",
        "sales": "销售",
        "admin": "行政"
    }
    
    # 摸鱼模式
    MODES = {
        "programmer": ["coding", "debugging", "building", "reviewing", "terminal"],
        "designer": ["ui-design", "graphic", "prototyping", "branding"],
        "pm": ["prd", "analysis", "roadmap", "meeting"],
        "operation": ["data", "content", "campaign", "social"],
        "hr": ["resume", "interview", "onboarding", "training"],
        "finance": ["report", "audit", "budget", "invoice"],
        "sales": ["crm", "proposal", "followup", "demo"],
        "admin": ["schedule", "procurement", "event", "archive"]
    }
    
    def __init__(self, job: str = "programmer"):
        """
        初始化摸鱼生成器
        
        Args:
            job: 职业类型，可选 programmer/designer/pm/operation/hr/finance/sales/admin
        """
        if job not in self.JOBS:
            raise ValueError(f"不支持的职业: {job}。支持的选项: {list(self.JOBS.keys())}")
        
        self.job = job
        self.job_name = self.JOBS[job]
        self.custom_snippets = {}
        self.terminal_commands = {}
    
    def generate_busy_code(self, language: str = "python", lines: int = 30) -> str:
        """
        生成看起来很忙的代码
        
        Args:
            language: 编程语言
            lines: 代码行数
            
        Returns:
            代码字符串
        """
        code_generators = {
            "python": self._generate_python_code,
            "javascript": self._generate_js_code,
            "java": self._generate_java_code,
            "go": self._generate_go_code,
            "rust": self._generate_rust_code
        }
        
        generator = code_generators.get(language, self._generate_python_code)
        return generator(lines)
    
    def _generate_python_code(self, lines: int) -> str:
        """生成Python代码"""
        templates = [
            "def process_{func}(data):",
            "    # TODO: Optimize {item} performance",
            "    result = []",
            "    for item in data:",
            "        if item['status'] == '{status}':",
            "            processed = transform_{func}(item)",
            "            result.append(processed)",
            "    return result",
            "",
            "class {ClassName}Manager:",
            "    def __init__(self, config):",
            "        self.config = config",
            "        self.cache = {{}}",
            "        self.logger = logging.getLogger(__name__)",
            "",
            "    def handle_{func}(self, request):",
            "        try:",
            "            validated = self.validate(request)",
            "            return self.process(validated)",
            "        except {Exception} as err:",
            "            self.logger.error('Error: ' + str(err))",
            "            raise",
            "",
            "# Performance optimization for {module}",
            "@lru_cache(maxsize={size})",
            "def cached_{func}(key):",
            "    return expensive_operation(key)",
        ]
        
        funcs = ["user", "order", "payment", "inventory", "analytics", "notification", "auth"]
        statuses = ["active", "pending", "completed", "failed", "processing"]
        classes = ["User", "Order", "Payment", "Inventory", "Analytics", "System"]
        exceptions = ["ValidationError", "NotFoundError", "TimeoutError", "ConnectionError"]
        modules = ["database", "cache", "queue", "search", "recommendation"]
        
        code_lines = []
        for i in range(lines):
            template = random.choice(templates)
            code = template.format(
                func=random.choice(funcs),
                status=random.choice(statuses),
                ClassName=random.choice(classes),
                Exception=random.choice(exceptions),
                module=random.choice(modules),
                item=random.choice(["query", "algorithm", "pipeline", "workflow"]),
                size=random.choice([128, 256, 512, 1024])
            )
            code_lines.append(code)
        
        return "\n".join(code_lines)
    
    def _generate_js_code(self, lines: int) -> str:
        """生成JavaScript代码"""
        templates = [
            "const {name} = async (params) => {{",
            "  try {{",
            "    const response = await fetch(`/api/{endpoint}`);",
            "    const data = await response.json();",
            "    return process{Type}(data);",
            "  }} catch (error) {{",
            "    console.error('{name} failed:', error);",
            "    throw error;",
            "  }}",
            "}};",
            "",
            "export const use{Hook} = () => {{",
            "  const [{state}, set{State}] = useState(null);",
            "  const {loading, error} = useSelector(state => state.{reducer});",
            "  ",
            "  useEffect(() => {{",
            "    dispatch(fetch{Action}());",
            "  }}, [dispatch]);",
            "  ",
            "  return {{ {state}, loading, error }};",
            "}};",
            "",
            "// TODO: Refactor {component} component",
            "const {Component} = ({props}) => {{",
            "  const classes = useStyles();",
            "  return (",
            "    <div className={{classes.root}}>",
            "      {/* Implementation pending */}",
            "    </div>",
            "  );",
            "}};",
        ]
        
        names = ["fetchUser", "updateOrder", "processPayment", "syncData", "handleEvent"]
        endpoints = ["users", "orders", "payments", "products", "analytics"]
        types = ["User", "Order", "Payment", "Product", "Analytics"]
        hooks = ["Data", "Auth", "Cart", "Search", "Filter"]
        states = ["data", "items", "result", "list", "details"]
        reducers = ["user", "order", "product", "cart", "search"]
        actions = ["UserData", "Orders", "Products", "CartItems", "SearchResults"]
        components = ["Header", "Sidebar", "Dashboard", "Profile", "Settings"]
        
        code_lines = []
        for i in range(lines):
            template = random.choice(templates)
            name = random.choice(names)
            code = template.format(
                name=name,
                Name=name.capitalize(),
                endpoint=random.choice(endpoints),
                Type=random.choice(types),
                Hook=random.choice(hooks),
                state=random.choice(states),
                State=random.choice(states).capitalize(),
                reducer=random.choice(reducers),
                Action=random.choice(actions),
                component=random.choice(components).lower(),
                Component=random.choice(components),
                props="props" if random.random() > 0.5 else "{ data, loading }"
            )
            code_lines.append(code)
        
        return "\n".join(code_lines)
    
    def _generate_java_code(self, lines: int) -> str:
        """生成Java代码"""
        templates = [
            "@Service",
            "public class {Service}Service {{",
            "    @Autowired",
            "    private {Repository}Repository {repository}Repository;",
            "    ",
            "    @Transactional",
            "    public {Type} process{Action}({Param} param) {{",
            "        log.info(\"Processing {action}: {{}}\", param.getId());",
            "        ",
            "        {Type} result = {repository}Repository.findById(param.getId())",
            "            .orElseThrow(() -> new {Exception}(\"Not found\"));",
            "            ",
            "        // Business logic here",
            "        return transform(result);",
            "    }}",
            "}}",
            "",
            "@Entity",
            "@Table(name = \"{table}\")",
            "public class {Entity} {{",
            "    @Id",
            "    @GeneratedValue(strategy = GenerationType.IDENTITY)",
            "    private Long id;",
            "    ",
            "    @Column(name = \"{column}\", nullable = false)",
            "    private String {field};",
            "    ",
            "    @ManyToOne(fetch = FetchType.LAZY)",
            "    @JoinColumn(name = \"{fk}\")",
            "    private {RefEntity} {refField};",
            "}}",
        ]
        
        services = ["User", "Order", "Payment", "Inventory", "Analytics"]
        repos = ["User", "Order", "Payment", "Product", "Category"]
        types = ["UserDTO", "OrderDTO", "PaymentResult", "InventoryVO", "ReportData"]
        actions = ["Order", "Payment", "Refund", "Sync", "Report"]
        params = ["Request", "Command", "Query", "Filter", "Criteria"]
        exceptions = ["NotFoundException", "BusinessException", "ValidationException"]
        tables = ["t_users", "t_orders", "t_payments", "t_inventory", "t_logs"]
        entities = ["User", "Order", "Payment", "Inventory", "AuditLog"]
        columns = ["username", "email", "status", "created_at", "updated_at"]
        fields = ["name", "email", "status", "createTime", "updateTime"]
        fks = ["user_id", "order_id", "product_id", "category_id", "parent_id"]
        ref_entities = ["User", "Order", "Product", "Category", "Department"]
        ref_fields = ["user", "order", "product", "category", "parent"]
        
        code_lines = []
        for i in range(lines):
            template = random.choice(templates)
            service = random.choice(services)
            code = template.format(
                Service=service,
                Repository=random.choice(repos),
                repository=random.choice(repos).lower(),
                Type=random.choice(types),
                Action=random.choice(actions),
                Param=random.choice(params),
                action=random.choice(actions).lower(),
                Exception=random.choice(exceptions),
                table=random.choice(tables),
                Entity=random.choice(entities),
                column=random.choice(columns),
                field=random.choice(fields),
                fk=random.choice(fks),
                RefEntity=random.choice(ref_entities),
                refField=random.choice(ref_fields)
            )
            code_lines.append(code)
        
        return "\n".join(code_lines)
    
    def _generate_go_code(self, lines: int) -> str:
        """生成Go代码"""
        templates = [
            "type {Service} struct {{",
            "    db     *gorm.DB",
            "    cache  *redis.Client",
            "    logger *zap.Logger",
            "}}",
            "",
            "func New{Service}(db *gorm.DB, cache *redis.Client) *{Service} {{",
            "    return &{Service}{{",
            "        db:     db,",
            "        cache:  cache,",
            "        logger: zap.L(),",
            "    }}",
            "}}",
            "",
            "func (s *{Service}) Handle{Action}(ctx context.Context, req *{Request}) (*{Response}, error) {{",
            "    s.logger.Info(\"handling request\", zap.String(\"id\", req.ID))",
            "    ",
            "    result, err := s.process(ctx, req)",
            "    if err != nil {{",
            "        return nil, fmt.Errorf(\"process failed: %w\", err)",
            "    }}",
            "    ",
            "    return &{Response}{{Data: result}}, nil",
            "}}",
            "",
            "// TODO: implement {feature}",
            "func init() {{",
            "    register{Type}(\"{name}\", &{Impl}{{}})",
            "}}",
        ]
        
        services = ["UserService", "OrderService", "PaymentService", "AuthService"]
        actions = ["Create", "Update", "Delete", "Get", "List", "Sync"]
        requests = ["CreateRequest", "UpdateRequest", "QueryRequest", "ListRequest"]
        responses = ["CreateResponse", "UpdateResponse", "QueryResponse", "ListResponse"]
        features = ["caching", "rate limiting", "circuit breaker", "retry logic"]
        types = ["Handler", "Middleware", "Repository", "Strategy"]
        names = ["default", "cached", "validated", "authorized"]
        impls = ["DefaultHandler", "CachedHandler", "ValidatedHandler"]
        
        code_lines = []
        for i in range(lines):
            template = random.choice(templates)
            service = random.choice(services)
            code = template.format(
                Service=service,
                Action=random.choice(actions),
                Request=random.choice(requests),
                Response=random.choice(responses),
                feature=random.choice(features),
                Type=random.choice(types),
                name=random.choice(names),
                Impl=random.choice(impls)
            )
            code_lines.append(code)
        
        return "\n".join(code_lines)
    
    def _generate_rust_code(self, lines: int) -> str:
        """生成Rust代码"""
        templates = [
            "pub struct {Service} {{",
            "    db: Pool<Postgres>,",
            "    cache: Cache<String, {Type}>,",
            "}}",
            "",
            "impl {Service} {{",
            "    pub async fn new(db: Pool<Postgres>) -> Self {{",
            "        Self {{",
            "            db,",
            "            cache: Cache::new(1000),",
            "        }}",
            "    }}",
            "",
            "    pub async fn process_{func}(&self, req: {Request}) -> Result<{Response}, Error> {{",
            "        let cached = self.cache.get(&req.id).await;",
            "        if let Some(data) = cached {{",
            "            return Ok(data);",
            "        }}",
            "        ",
            "        let result = sqlx::query_as::<_, {Type}>(",
            "            SELECT * FROM {table} WHERE id = $1",
            "        )",
            "        .bind(&req.id)",
            "        .fetch_one(&self.db)",
            "        .await?;",
            "        ",
            "        self.cache.set(req.id, result.clone()).await;",
            "        Ok(result)",
            "    }}",
            "}}",
            "",
            "#[derive(Debug, Serialize, Deserialize)]",
            "pub struct {Type} {{",
            "    pub id: Uuid,",
            "    pub {field}: String,",
            "    pub status: {Status},",
            "    pub created_at: DateTime<Utc>,",
            "}}",
        ]
        
        services = ["UserRepository", "OrderService", "PaymentProcessor", "AuthManager"]
        types = ["User", "Order", "Payment", "Product", "Category"]
        funcs = ["order", "payment", "user", "product", "inventory"]
        requests = ["CreateOrder", "UpdatePayment", "GetUser", "QueryProduct"]
        responses = ["OrderResult", "PaymentStatus", "UserProfile", "ProductDetail"]
        tables = ["users", "orders", "payments", "products", "categories"]
        fields = ["name", "email", "description", "metadata", "config"]
        statuses = ["Status", "OrderStatus", "PaymentStatus", "UserState"]
        
        code_lines = []
        for i in range(lines):
            template = random.choice(templates)
            service = random.choice(services)
            code = template.format(
                Service=service,
                Type=random.choice(types),
                func=random.choice(funcs),
                Request=random.choice(requests),
                Response=random.choice(responses),
                table=random.choice(tables),
                field=random.choice(fields),
                Status=random.choice(statuses)
            )
            code_lines.append(code)
        
        return "\n".join(code_lines)
    
    def generate_terminal_output(self, command: str = "build", status: str = "running") -> str:
        """
        生成终端输出
        
        Args:
            command: 命令类型
            status: 状态
            
        Returns:
            终端输出字符串
        """
        outputs = {
            "build": self._generate_build_output,
            "deploy": self._generate_deploy_output,
            "test": self._generate_test_output,
            "docker": self._generate_docker_output,
            "git": self._generate_git_output,
            "log": self._generate_log_output,
            "system": self._generate_system_output
        }
        
        generator = outputs.get(command, self._generate_build_output)
        return generator(status)
    
    def _generate_build_output(self, status: str) -> str:
        """生成构建输出"""
        lines = [
            f"$ npm run build",
            f"",
            f"> project@1.0.0 build",
            f"> webpack --mode production",
            f"",
            f"asset {random.choice(['main', 'vendor', 'app'])}.{random.choice(['js', 'css'])} {random.randint(100, 900)} KiB [emitted] [immutable]",
            f"asset {random.choice(['runtime', 'polyfill'])}.{random.choice(['js', 'css'])} {random.randint(10, 100)} KiB [emitted] [immutable]",
            f"",
            f"WARNING in {random.randint(1, 50)}:23-45",
            f"export '{random.choice(['default', 'named'])}' was not found in '{random.choice(['utils', 'helpers', 'constants'])}'",
            f"",
            f"webpack compiled with {random.randint(0, 3)} warnings",
        ]
        return "\n".join(lines)
    
    def _generate_deploy_output(self, status: str) -> str:
        """生成部署输出"""
        services = ["api-gateway", "user-service", "order-service", "payment-service", "notification-service"]
        lines = [
            f"$ kubectl apply -f k8s/",
            f"",
            f"deployment.apps/{random.choice(services)} configured",
            f"service/{random.choice(services)} unchanged",
            f"configmap/app-config unchanged",
            f"",
            f"$ kubectl rollout status deployment/{random.choice(services)}",
            f"Waiting for deployment \"{random.choice(services)}\" rollout to finish: {random.randint(0, 5)} of {random.randint(5, 10)} updated replicas are available...",
            f"deployment \"{random.choice(services)}\" successfully rolled out",
            f"",
            f"$ curl -s https://api.example.com/health",
            f'{{"status":"healthy","version":"1.{random.randint(0, 9)}.{random.randint(0, 9)}"}}',
        ]
        return "\n".join(lines)
    
    def _generate_test_output(self, status: str) -> str:
        """生成测试输出"""
        passed = random.randint(45, 100)
        failed = random.randint(0, 5)
        lines = [
            f"$ npm test",
            f"",
            f"PASS src/{random.choice(['components', 'utils', 'hooks'])}/{random.choice(['User', 'Order', 'Payment'])}.test.js",
            f"  ✓ should {random.choice(['render correctly', 'handle click', 'update state', 'call api'])} ({random.randint(10, 100)}ms)",
            f"  ✓ should {random.choice(['validate input', 'show error', 'redirect user', 'cache result'])} ({random.randint(10, 100)}ms)",
            f"",
            f"PASS src/{random.choice(['services', 'api', 'store'])}/{random.choice(['auth', 'cart', 'search'])}.test.js",
            f"  ✓ should {random.choice(['authenticate', 'add item', 'search'])} ({random.randint(10, 100)}ms)",
            f"",
            f"Test Suites: {passed + failed} passed, {passed + failed} total",
            f"Tests:       {passed} passed, {failed} failed, {passed + failed} total",
            f"Snapshots:   0 total",
            f"Time:        {random.randint(5, 30)}s",
        ]
        return "\n".join(lines)
    
    def _generate_docker_output(self, status: str) -> str:
        """生成Docker输出"""
        lines = [
            f"$ docker-compose up -d",
            f"",
            f"[+] Running {random.randint(3, 8)}/{random.randint(3, 8)}",
            f" ✔ Container {random.choice(['db', 'redis', 'mq'])}           Started",
            f" ✔ Container {random.choice(['api', 'worker', 'scheduler'])}   Started",
            f" ✔ Container {random.choice(['nginx', 'lb', 'gateway'])}       Started",
            f"",
            f"$ docker ps",
            f"CONTAINER ID   IMAGE                STATUS          PORTS",
            f"{self._random_id(12)}   app/api:latest       Up {random.randint(1, 60)} minutes   0.0.0.0:8080->8080/tcp",
            f"{self._random_id(12)}   postgres:14          Up {random.randint(1, 60)} minutes   5432/tcp",
            f"{self._random_id(12)}   redis:alpine         Up {random.randint(1, 60)} minutes   6379/tcp",
        ]
        return "\n".join(lines)
    
    def _generate_git_output(self, status: str) -> str:
        """生成Git输出"""
        lines = [
            f"$ git status",
            f"On branch {random.choice(['main', 'develop', 'feature/new-ui', 'hotfix/critical'])}",
            f"Your branch is ahead of 'origin/main' by {random.randint(1, 10)} commits.",
            f"",
            f"Changes not staged for commit:",
            f"  (use \"git add <file>...\" to update what will be committed)",
            f"  modified:   src/{random.choice(['components', 'pages', 'utils'])}/{random.choice(['Button', 'Header', 'utils'])}.{random.choice(['tsx', 'ts', 'js'])}",
            f"  modified:   package.json",
            f"",
            f"$ git log --oneline -5",
            f"{self._random_id(7)} fix: resolve {random.choice(['memory leak', 'race condition', 'null pointer'])} in {random.choice(['auth', 'payment', 'cache'])} module",
            f"{self._random_id(7)} feat: add {random.choice(['dark mode', 'pagination', 'search filter'])} support",
            f"{self._random_id(7)} refactor: optimize {random.choice(['database query', 'api response', 'render performance'])}",
            f"{self._random_id(7)} docs: update {random.choice(['api documentation', 'deployment guide', 'changelog'])}",
        ]
        return "\n".join(lines)
    
    def _generate_log_output(self, status: str) -> str:
        """生成日志输出"""
        levels = ["INFO", "DEBUG", "WARN"]
        lines = []
        for i in range(10):
            level = random.choice(levels)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            lines.append(f"{timestamp} [{level}] {random.choice(['UserService', 'OrderController', 'PaymentGateway', 'CacheManager'])} - {random.choice(['Processing request', 'Cache hit', 'Database query executed', 'Event published', 'Message consumed'])}: id={random.randint(10000, 99999)}")
        return "\n".join(lines)
    
    def _generate_system_output(self, status: str) -> str:
        """生成系统监控输出"""
        lines = [
            f"$ htop",
            f"",
            f"  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND",
            f"{random.randint(1000, 99999)} root      20   0  {random.randint(100, 999)}m   {random.randint(10, 99)}m  {random.randint(5000, 15000)} S   {random.randint(0, 99)}.{random.randint(0, 9)}  {random.randint(0, 9)}.{random.randint(0, 9)}   0:{random.randint(10, 59)}.{random.randint(10, 99)} node",
            f"{random.randint(1000, 99999)} root      20   0  {random.randint(100, 999)}m   {random.randint(10, 99)}m  {random.randint(5000, 15000)} S   {random.randint(0, 99)}.{random.randint(0, 9)}  {random.randint(0, 9)}.{random.randint(0, 9)}   0:{random.randint(10, 59)}.{random.randint(10, 99)} python",
            f"{random.randint(1000, 99999)} root      20   0  {random.randint(100, 999)}m   {random.randint(10, 99)}m  {random.randint(5000, 15000)} S   {random.randint(0, 99)}.{random.randint(0, 9)}  {random.randint(0, 9)}.{random.randint(0, 9)}   0:{random.randint(10, 59)}.{random.randint(10, 99)} postgres",
            f"",
            f"KiB Mem :  {random.randint(1000000, 9999999)} total,   {random.randint(100000, 999999)} free,  {random.randint(100000, 999999)} used,  {random.randint(100000, 999999)} buff/cache",
            f"KiB Swap:  {random.randint(100000, 999999)} total,   {random.randint(100000, 999999)} free,        0 used.  {random.randint(100000, 999999)} avail Mem",
        ]
        return "\n".join(lines)
    
    def _random_id(self, length: int) -> str:
        """生成随机ID"""
        chars = "abcdef0123456789"
        return "".join(random.choice(chars) for _ in range(length))
    
    def generate_design_content(self, mode: str = "ui-design") -> str:
        """
        生成设计师摸鱼内容
        
        Args:
            mode: 设计模式
            
        Returns:
            设计内容字符串
        """
        if mode == "ui-design":
            return self._generate_ui_design_content()
        elif mode == "graphic":
            return self._generate_graphic_content()
        elif mode == "prototyping":
            return self._generate_prototype_content()
        elif mode == "branding":
            return self._generate_branding_content()
        else:
            return self._generate_ui_design_content()
    
    def _generate_ui_design_content(self) -> str:
        """生成UI设计内容"""
        components = ["Button", "Card", "Modal", "Form", "Navigation", "Table", "Chart", "Avatar"]
        states = ["default", "hover", "active", "disabled", "loading", "error"]
        colors = ["primary-500", "secondary-300", "neutral-100", "success-600", "warning-400", "error-500"]
        
        lines = [
            "# Design System - Component Library",
            "",
            "## Color Palette",
            f"- Primary: #{random.randint(100000, 999999)}",
            f"- Secondary: #{random.randint(100000, 999999)}",
            f"- Accent: #{random.randint(100000, 999999)}",
            "",
            "## Typography",
            "- Heading: Inter Bold 24px",
            "- Body: Inter Regular 16px",
            "- Caption: Inter Medium 12px",
            "",
            "## Component Specifications",
        ]
        
        for comp in random.sample(components, 4):
            lines.extend([
                f"",
                f"### {comp}",
                f"- Size: {random.choice(['sm', 'md', 'lg'])} ({random.randint(32, 64)}px)",
                f"- Border Radius: {random.choice([4, 8, 12, 16])}px",
                f"- States: {', '.join(random.sample(states, 3))}",
                f"- Colors: {random.choice(colors)}, {random.choice(colors)}",
            ])
        
        return "\n".join(lines)
    
    def _generate_graphic_content(self) -> str:
        """生成平面设计内容"""
        lines = [
            "# Visual Design - Marketing Assets",
            "",
            "## Banner Design (1920x1080)",
            "- Layout: Grid 12-column",
            "- Main Visual: Abstract gradient shapes",
            "- Typography: Bold headline + subheading",
            "- CTA Button: High contrast, prominent placement",
            "",
            "## Social Media Posts",
            "### Instagram (1080x1080)",
            f"- Theme: {random.choice(['Minimalist', 'Vibrant', 'Professional', 'Playful'])}",
            f"- Color Scheme: {random.choice(['Monochrome', 'Complementary', 'Analogous', 'Triadic'])}",
            "- Elements: Icon + Text overlay",
            "",
            "### LinkedIn (1200x627)",
            "- Style: Corporate, clean",
            "- Imagery: Team collaboration, office environment",
            "- Text: Concise, impactful messaging",
            "",
            "## Print Materials",
            "- Business Card: 85x55mm, 300dpi",
            "- Flyer: A5, double-sided",
            "- Brochure: Tri-fold, full color",
        ]
        return "\n".join(lines)
    
    def _generate_prototype_content(self) -> str:
        """生成交互原型内容"""
        screens = ["Login", "Dashboard", "Profile", "Settings", "Search", "Checkout"]
        interactions = ["Tap", "Swipe", "Long Press", "Drag", "Pinch", "Scroll"]
        animations = ["Fade In", "Slide Up", "Scale", "Rotate", "Bounce", "Elastic"]
        
        lines = [
            "# Interactive Prototype - User Flow",
            "",
            "## Screen Flow",
        ]
        
        for i, screen in enumerate(random.sample(screens, 4), 1):
            lines.extend([
                f"",
                f"### {i}. {screen} Screen",
                f"- Entry: {random.choice(['Direct', 'From Home', 'Deep Link', 'Notification'])}",
                f"- Primary Action: {random.choice(['Submit', 'Navigate', 'Filter', 'Save'])}",
                f"- Gestures: {', '.join(random.sample(interactions, 2))}",
                f"- Transitions: {random.choice(animations)} ({random.randint(200, 500)}ms)",
            ])
        
        lines.extend([
            "",
            "## Micro-interactions",
            "- Button hover: Scale 1.05 + shadow",
            "- Loading: Skeleton + shimmer effect",
            "- Success: Checkmark animation + haptic",
            "- Error: Shake + red border + toast",
            "",
            "## Responsive Breakpoints",
            "- Mobile: 375px",
            "- Tablet: 768px",
            "- Desktop: 1440px",
        ])
        
        return "\n".join(lines)
    
    def _generate_branding_content(self) -> str:
        """生成品牌设计内容"""
        lines = [
            "# Brand Identity Guidelines",
            "",
            "## Logo System",
            "### Primary Logo",
            "- Format: SVG, PNG, PDF",
            "- Clear Space: Minimum 1x logo height",
            "- Minimum Size: 24px height (digital), 10mm (print)",
            "",
            "### Logo Variations",
            "- Horizontal: Full wordmark + symbol",
            "- Stacked: Symbol above wordmark",
            "- Symbol Only: For favicon, app icon",
            "- Monochrome: For single-color applications",
            "",
            "## Color System",
            f"- Primary: #{random.randint(100000, 999999)} (Brand recognition)",
            f"- Secondary: #{random.randint(100000, 999999)} (Supporting)",
            f"- Neutral: #{random.randint(100000, 999999)} (Backgrounds)",
            f"- Accent: #{random.randint(100000, 999999)} (CTAs, highlights)",
            "",
            "## Typography",
            "- Headlines: [Brand Font] Bold",
            "- Body: [System Font] Regular",
            "- Scale: Major Third (1.25)",
            "",
            "## Voice & Tone",
            "- Professional yet approachable",
            "- Clear and concise",
            "- Action-oriented",
            "- Empathetic to user needs",
        ]
        return "\n".join(lines)
    
    def generate_pm_content(self, mode: str = "prd") -> str:
        """
        生成产品经理摸鱼内容
        
        Args:
            mode: 产品模式
            
        Returns:
            产品内容字符串
        """
        if mode == "prd":
            return self._generate_prd_content()
        elif mode == "analysis":
            return self._generate_analysis_content()
        elif mode == "roadmap":
            return self._generate_roadmap_content()
        elif mode == "meeting":
            return self._generate_meeting_content()
        else:
            return self._generate_prd_content()
    
    def _generate_prd_content(self) -> str:
        """生成PRD文档内容"""
        features = ["User Authentication", "Payment Integration", "Search & Filter", "Notifications", "Analytics Dashboard"]
        personas = ["New User", "Power User", "Admin", "Guest", "Premium Subscriber"]
        
        lines = [
            "# Product Requirements Document",
            f"## Feature: {random.choice(features)}",
            "",
            "### 1. Overview",
            f"**Objective:** Enable {random.choice(personas).lower()}s to {random.choice(['complete core tasks efficiently', 'access premium features', 'manage their account', 'discover relevant content'])}.",
            "",
            "### 2. User Stories",
        ]
        
        for i in range(1, 4):
            lines.extend([
                f"",
                f"#### US-{random.randint(100, 999)}",
                f"**As a** {random.choice(personas).lower()},",
                f"**I want to** {random.choice(['quickly find what I need', 'complete my task without confusion', 'see my progress', 'get help when stuck'])},",
                f"**So that** {random.choice(['I can save time', 'I feel confident using the product', 'I achieve my goals', 'I have a positive experience'])}.",
                "",
                "**Acceptance Criteria:**",
                f"- [ ] {random.choice(['Load time < 2 seconds', 'Error rate < 1%', 'Success rate > 95%', 'User satisfaction > 4.5/5'])}",
                f"- [ ] {random.choice(['Works on mobile and desktop', 'Accessible via keyboard', 'Screen reader compatible', 'Supports 10+ languages'])}"
            ])
        
        lines.extend([
            "",
            "### 3. Technical Requirements",
            "- API Response Time: < 200ms (p95)",
            "- Availability: 99.9% uptime",
            "- Data Retention: 90 days",
            "- Security: OAuth 2.0 + MFA",
            "",
            "### 4. Success Metrics",
            "- Feature adoption rate: > 60%",
            "- Task completion rate: > 80%",
            "- NPS improvement: +10 points",
        ])
        
        return "\n".join(lines)
    
    def _generate_analysis_content(self) -> str:
        """生成数据分析内容"""
        metrics = ["DAU", "MAU", "Retention", "Conversion", "Churn", "ARPU", "LTV"]
        periods = ["Week over Week", "Month over Month", "Quarter over Quarter", "Year over Year"]
        
        lines = [
            "# Data Analysis Report",
            f"**Period:** {datetime.now().strftime('%Y-%m-%d')} (Last 30 days)",
            "",
            "## Executive Summary",
            f"Overall performance shows {random.choice(['positive', 'mixed', 'concerning'])} trends. Key metrics indicate {random.choice(['growth opportunities', 'areas needing attention', 'steady progress'])}.",
            "",
            "## Key Metrics",
        ]
        
        for metric in random.sample(metrics, 4):
            change = random.uniform(-15, 25)
            trend = "📈" if change > 0 else "📉"
            lines.extend([
                f"",
                f"### {metric}",
                f"- Current: {random.randint(1000, 999999):,}",
                f"- Change: {trend} {abs(change):.1f}% {random.choice(periods)}",
                f"- Target: {random.randint(1000, 999999):,}",
                f"- Status: {'✅ On Track' if change > 0 else '⚠️ Below Target'}",
            ])
        
        lines.extend([
            "",
            "## Insights",
            f"1. **{random.choice(metrics)}** shows {random.choice(['strong correlation', 'inverse relationship', 'seasonal pattern'])} with {random.choice(metrics)}.",
            f"2. **{random.choice(['Mobile users', 'Premium segment', 'New acquisitions', 'Returning users'])}** demonstrate {random.choice(['higher engagement', 'lower retention', 'increasing value', 'shifting preferences'])}.",
            f"3. **{random.choice(['Feature X', 'Campaign Y', 'Redesign Z'])}** contributed to {random.choice(['20% uplift', 'significant drop', 'mixed results', 'unexpected outcome'])}.",
            "",
            "## Recommendations",
            "1. Prioritize optimization of underperforming metrics",
            "2. A/B test new onboarding flow",
            "3. Investigate correlation between engagement and retention",
        ])
        
        return "\n".join(lines)
    
    def _generate_roadmap_content(self) -> str:
        """生成产品路线图内容"""
        quarters = ["Q1", "Q2", "Q3", "Q4"]
        themes = ["Foundation", "Growth", "Scale", "Innovation"]
        
        lines = [
            "# Product Roadmap 2024",
            "",
            "## Vision",
            "Become the leading platform for [target market] by delivering exceptional [value proposition].",
            "",
            "## Strategic Themes",
        ]
        
        for i, (quarter, theme) in enumerate(zip(quarters, themes), 1):
            features = ["Core Platform", "Mobile App", "API Ecosystem", "Enterprise Features", "AI Integration", "Global Expansion"]
            lines.extend([
                f"",
                f"### {quarter} 2024 - {theme}",
                f"**Focus:** {random.choice(['Stability & Performance', 'User Acquisition', 'Revenue Growth', 'Market Expansion'])}",
                "",
                "**Key Initiatives:**",
                f"- 🎯 {random.choice(features)}",
                f"- 🎯 {random.choice(features)}",
                f"- 🎯 {random.choice(features)}",
                "",
                "**Success Metrics:**",
                f"- {random.choice(['99.9% uptime', '50% faster load', '30% cost reduction', '2x user growth'])}",
            ])
        
        lines.extend([
            "",
            "## Dependencies",
            "- Engineering capacity allocation",
            "- Third-party API integrations",
            "- Compliance & security reviews",
            "",
            "## Risks",
            "- Resource constraints",
            "- Technical debt accumulation",
            "- Market timing",
        ])
        
        return "\n".join(lines)
    
    def _generate_meeting_content(self) -> str:
        """生成会议记录内容"""
        lines = [
            "# Meeting Notes",
            f"**Date:** {datetime.now().strftime('%Y-%m-%d')}",
            f"**Time:** {random.choice(['09:00-10:00', '14:00-15:00', '10:30-11:30'])}",
            "**Attendees:** Product, Engineering, Design, QA",
            "",
            "## Agenda",
            "1. Sprint Review",
            "2. Upcoming Priorities",
            "3. Blockers & Risks",
            "4. Action Items",
            "",
            "## Discussion",
            "",
            "### Sprint Review",
            f"- Completed {random.randint(8, 15)} story points",
            f"- {random.randint(0, 3)} bugs identified, {random.randint(1, 3)} resolved",
            f"- Feature '{random.choice(['Search V2', 'Dashboard Redesign', 'Mobile Optimization', 'API Migration'])}' ready for QA",
            "",
            "### Priorities",
            f"1. **P0:** {random.choice(['Critical bug fix', 'Security patch', 'Performance optimization', 'Compliance update'])}",
            f"2. **P1:** {random.choice(['Feature launch', 'User research', 'Tech debt', 'Documentation'])}",
            f"3. **P2:** {random.choice(['Refactoring', 'Testing', 'Monitoring', 'Analytics'])}",
            "",
            "## Action Items",
            "| Task | Owner | Due Date | Status |",
            "|------|-------|----------|--------|",
        ]
        
        owners = ["@alice", "@bob", "@carol", "@dave"]
        for i in range(4):
            lines.append(f"| {random.choice(['Update PRD', 'Fix critical bug', 'Prepare demo', 'Review designs'])} | {random.choice(owners)} | {datetime.now().strftime('%Y-%m-%d')} | 🔄 In Progress |")
        
        lines.extend([
            "",
            "## Next Steps",
            "- Follow up on action items by EOD",
            "- Schedule design review for next week",
            "- Prepare release notes for v2.3.0",
        ])
        
        return "\n".join(lines)
    
    def generate_busy_status(self, task: str = "working", progress: int = 50) -> str:
        """
        生成工作状态
        
        Args:
            task: 任务类型
            progress: 进度百分比
            
        Returns:
            状态字符串
        """
        status_emojis = {
            "working": "💻",
            "meeting": "📅",
            "reviewing": "👀",
            "debugging": "🐛",
            "deploying": "🚀",
            "testing": "🧪",
            "planning": "📊",
            "researching": "🔍"
        }
        
        emoji = status_emojis.get(task, "💻")
        bar_length = 20
        filled = int(bar_length * progress / 100)
        bar = "█" * filled + "░" * (bar_length - filled)
        
        tasks = {
            "working": ["Implementing feature", "Writing documentation", "Refactoring code", "Optimizing performance"],
            "meeting": ["In standup", "Client call", "Design review", "Sprint planning"],
            "reviewing": ["Code review", "Design critique", "Document review", "PR review"],
            "debugging": ["Investigating issue", "Tracing bug", "Fixing error", "Testing fix"],
            "deploying": ["Deploying to staging", "Production release", "Rolling update", "Hotfix deployment"],
            "testing": ["Running tests", "QA validation", "User testing", "Performance test"],
            "planning": ["Sprint planning", "Roadmap review", "Capacity planning", "Risk assessment"],
            "researching": ["Competitor analysis", "User research", "Technical spike", "Market research"]
        }
        
        task_desc = random.choice(tasks.get(task, tasks["working"]))
        
        lines = [
            f"{emoji} {task_desc}...",
            f"",
            f"Progress: [{bar}] {progress}%",
            f"",
            f"⏱️  Elapsed: {random.randint(10, 120)} minutes",
            f"🎯 Estimated: {random.randint(5, 60)} minutes remaining",
            f"📊 Tasks: {random.randint(1, 10)}/{random.randint(5, 20)} completed",
        ]
        
        return "\n".join(lines)
    
    def print_busy_animation(self, duration: int = 30):
        """
        打印忙碌的动画效果
        
        Args:
            duration: 持续时间（秒）
        """
        import time
        import sys
        
        frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        messages = [
            "Compiling modules...",
            "Optimizing assets...",
            "Running tests...",
            "Building project...",
            "Deploying services...",
            "Processing data...",
            "Generating reports...",
            "Syncing repositories..."
        ]
        
        end_time = time.time() + duration
        message = random.choice(messages)
        frame_idx = 0
        
        try:
            while time.time() < end_time:
                frame = frames[frame_idx % len(frames)]
                sys.stdout.write(f"\r{frame} {message}")
                sys.stdout.flush()
                frame_idx += 1
                time.sleep(0.1)
        except KeyboardInterrupt:
            pass
        finally:
            sys.stdout.write("\r✓ Done!                    \n")
            sys.stdout.flush()


def main():
    """命令行入口"""
    parser = argparse.ArgumentParser(
        description="摸鱼助手 - 帮助你在公司看起来忙碌",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python moyu.py --job programmer --mode coding          # 生成程序员代码
  python moyu.py --job designer --mode ui-design         # 生成设计规范
  python moyu.py --job pm --mode prd                     # 生成PRD文档
  python moyu.py --job programmer --animate 30           # 显示忙碌动画30秒
  python moyu.py --list                                  # 列出所有职业和模式
        """
    )
    
    parser.add_argument("--job", "-j", type=str, default="programmer",
                       help="职业类型 (programmer/designer/pm/operation/hr/finance/sales/admin)")
    parser.add_argument("--mode", "-m", type=str, default="coding",
                       help="摸鱼模式")
    parser.add_argument("--lines", "-l", type=int, default=30,
                       help="代码行数 (默认30)")
    parser.add_argument("--language", "-lang", type=str, default="python",
                       help="编程语言 (python/javascript/java/go/rust)")
    parser.add_argument("--animate", "-a", type=int, metavar="SECONDS",
                       help="显示忙碌动画指定秒数")
    parser.add_argument("--progress", "-p", type=int, default=50,
                       help="进度百分比 (0-100)")
    parser.add_argument("--list", action="store_true",
                       help="列出所有支持的职业和模式")
    
    args = parser.parse_args()
    
    if args.list:
        print("=" * 60)
        print("🐟 摸鱼助手 - 支持的职业和模式")
        print("=" * 60)
        for job, modes in MoyuGenerator.MODES.items():
            job_name = MoyuGenerator.JOBS[job]
            print(f"\n📌 {job_name} ({job})")
            for mode in modes:
                print(f"   • {mode}")
        print("\n" + "=" * 60)
        return
    
    try:
        generator = MoyuGenerator(job=args.job)
    except ValueError as e:
        print(f"❌ 错误: {e}")
        return
    
    if args.animate:
        print(f"🎭 开始{generator.job_name}摸鱼模式...")
        print(f"⏱️  持续时间: {args.animate}秒")
        print("按 Ctrl+C 提前结束\n")
        generator.print_busy_animation(duration=args.animate)
        return
    
    print(f"🐟 {generator.job_name}摸鱼内容生成中...")
    print("=" * 60)
    
    if args.job == "programmer":
        if args.mode in ["coding", "debugging", "reviewing"]:
            content = generator.generate_busy_code(language=args.language, lines=args.lines)
        elif args.mode == "terminal":
            content = generator.generate_terminal_output(command="build")
        else:
            content = generator.generate_busy_code(language=args.language, lines=args.lines)
    
    elif args.job == "designer":
        content = generator.generate_design_content(mode=args.mode)
    
    elif args.job == "pm":
        content = generator.generate_pm_content(mode=args.mode)
    
    else:
        # 其他职业使用通用内容
        content = generator.generate_busy_status(task=args.mode, progress=args.progress)
    
    print(content)
    print("=" * 60)
    print(f"✅ {generator.job_name}摸鱼内容已生成！")
    print("💡 提示: 使用 --animate 参数可以显示忙碌的动画效果")


if __name__ == "__main__":
    main()
