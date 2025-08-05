# Simple Open Interpreter

一个基于 LangChain 和 Ollama 的简单 Open Interpreter 项目，展示了如何使用 AI Agent 来执行文件系统操作。

## 项目简介

这个项目实现了一个简单的 AI Agent，能够：
- 列出当前目录下的文件
- 读取指定文件的内容
- 通过自然语言与用户交互

项目使用 ReAct Agent 模式，结合了 LangChain 框架和 Ollama 本地大语言模型。

## 功能特性

- 🤖 **AI Agent**: 基于 ReAct 模式的智能代理
- 📁 **文件操作**: 支持列出文件和读取文件内容
- ️ **自然语言交互**: 使用中文或英文与 Agent 对话
- 🏠 **本地部署**: 使用 Ollama 本地模型，保护隐私
-  **可扩展**: 易于添加新的工具和功能

## 技术栈

- **LangChain**: AI 应用开发框架
- **Ollama**: 本地大语言模型服务
- **Python**: 主要编程语言

## 环境要求

- Python 3.8+
- Ollama (需要本地安装并运行)

## 安装步骤

### 1. 克隆项目

```bash
git clone https://github.com/SpikeSpiegel25/simple-open-interpreter
cd simple-open-interpreter
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 安装并启动 Ollama

请参考 [Ollama 官方文档](https://ollama.ai/) 安装 Ollama，然后启动服务：

```bash
ollama serve
```

### 4. 下载模型

项目默认使用 `qwen2.5:7b` 模型，请确保已下载：

```bash
ollama pull qwen2.5:7b
```

## 使用方法

### 运行项目

```bash
python main.py
```

### 示例交互

项目会自动执行以下示例任务：

1. **列出文件**: Agent 会列出当前目录下的所有文件
2. **读取文件**: Agent 会读取 `example.txt` 文件的内容

### 自定义使用

你可以修改 `main.py` 中的 `agent_executor.invoke()` 调用来执行不同的任务：

```python
response = agent_executor.invoke({
    "input": "你的自然语言指令"
})
```

## 项目结构

```
simple-open-interpreter/
├── main.py              # 主程序文件
├── tools.py             # 工具函数定义
├── requirements.txt     # Python 依赖
├── example.txt         # 示例文件
├── README.md          # 项目文档
└── LICENSE            # 许可证文件
```

## 工具说明

### 可用工具

1. **list_files**: 列出指定目录下的文件
   - 参数: `directory` (可选，默认为当前目录)
   - 返回: 文件列表字符串

2. **read_file**: 读取指定文件的内容
   - 参数: `file_path` (文件路径)
   - 返回: 文件内容字符串

### 添加新工具

在 `tools.py` 中添加新的工具函数：

```python
@tool
def your_new_tool(param: str) -> str:
    """
    工具描述
    """
    # 工具实现
    return result
```

然后在 `main.py` 中将新工具添加到 `tools` 列表中。

## 配置说明

### 模型配置

在 `main.py` 中可以修改模型配置：

```python
llm = ChatOllama(
    base_url="http://localhost:11434",  # Ollama 服务地址
    model="qwen2.5:7b"                  # 使用的模型
)
```

### 支持的模型

项目支持任何 Ollama 兼容的模型，包括：
- qwen2.5:7b
- llama2:7b
- codellama:7b
- 其他自定义模型

## 故障排除

### 常见问题

1. **Ollama 连接失败**
   - 确保 Ollama 服务正在运行
   - 检查端口 11434 是否可访问

2. **模型未找到**
   - 使用 `ollama list` 检查已安装的模型
   - 使用 `ollama pull <model-name>` 下载所需模型

3. **依赖安装失败**
   - 确保 Python 版本 >= 3.10
   - 尝试使用虚拟环境

## 开发计划

- [ ] 添加更多文件操作工具
- [ ] 支持网络请求功能

## 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 致谢

- [LangChain](https://www.langchain.com/) - AI 应用开发框架
- [Ollama](https://ollama.ai/) - 本地大语言模型服务
- [Qwen](https://github.com/QwenLM/Qwen) - 开源大语言模型

## 联系方式

如有问题或建议，请通过以下方式联系：
- 提交 GitHub Issue

---

⭐ 如果这个项目对你有帮助，请给它一个星标！
