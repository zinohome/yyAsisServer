# 测试工具说明

本目录包含了数字人项目的各种测试工具和测试脚本。

## 测试文件说明

### API测试
- `test_agent_api.py` - Agent API接口测试
- `test_asr_api.py` - ASR API接口测试
- `test_llm_api.py` - LLM API接口测试
- `test_tts_api.py` - TTS API接口测试
- `test_common_api.py` - 通用API接口测试

### WebSocket测试
- `test_asr_websocket_client.py` - **ASR WebSocket客户端测试工具**
- `test_ws_web.html` - WebSocket Web测试页面

### 专项测试
- `server/test_streaming_asr_api.py` - 流式ASR API专项测试
- `engine/asr/` - ASR引擎相关测试
- `src/audio/` - 音频处理测试资源

## ASR WebSocket客户端测试工具

`test_asr_websocket_client.py` 是一个功能完整的ASR WebSocket测试客户端，支持：

- 🎤 实时麦克风音频流测试
- 📁 音频文件流测试
- 🔗 完整的WebSocket协议实现
- 📊 实时显示识别结果
- 📝 详细的日志输出

### 快速使用

```bash
# 进入test目录
cd test

# 麦克风测试（默认10秒）
python test_asr_websocket_client.py --mode mic

# 音频文件测试
python test_asr_websocket_client.py --mode file --file /path/to/audio.wav

# 详细日志模式
python test_asr_websocket_client.py --mode mic --verbose
```

### 详细文档

完整的使用说明和配置指南请参考：[ASR客户端测试工具文档](../docs/asr_client_testing.md)

## 运行测试

### 环境准备

```bash
# 安装测试依赖
pip install -r ../test_requirements.txt

# 确保服务器正在运行
# 参考部署文档启动数字人服务
```

### 运行单个测试

```bash
# 运行ASR API测试
python test_asr_api.py

# 运行WebSocket客户端测试
python test_asr_websocket_client.py --mode mic --duration 5
```

### 运行所有测试

```bash
# 使用pytest运行所有测试
pytest

# 运行特定模块测试
pytest test_asr_api.py -v

# 运行测试并生成报告
pytest --html=report.html --self-contained-html
```

## 测试配置

### pytest配置

测试配置在 `pytest.ini` 文件中定义，包括：
- 测试发现规则
- 日志配置
- 标记定义

### 测试环境

在 `conftest.py` 中定义了测试的公共配置和fixture：
- 测试服务器配置
- 公共测试数据
- 测试环境初始化

## 注意事项

1. **服务器依赖**: 大部分测试需要数字人服务器正在运行
2. **音频设备**: ASR相关测试需要可用的音频输入设备
3. **网络连接**: WebSocket测试需要稳定的网络连接
4. **权限要求**: 麦克风测试可能需要系统音频权限

## 故障排除

### 常见问题

1. **连接失败**: 检查服务器是否启动，端口是否正确
2. **音频设备错误**: 检查麦克风权限和设备可用性
3. **依赖缺失**: 确保安装了所有测试依赖
4. **权限问题**: 确保有足够的系统权限访问音频设备

### 调试技巧

```bash
# 启用详细日志
python test_asr_websocket_client.py --mode mic --verbose

# 检查服务器连通性
telnet localhost 8000

# 查看pytest详细输出
pytest -v -s
```

## 贡献指南

如果你想添加新的测试或改进现有测试：

1. 遵循现有的测试命名规范
2. 添加适当的文档和注释
3. 确保测试的独立性和可重复性
4. 更新相关的README文档

## 相关文档

- [部署说明](../docs/deploy_instrction.md)
- [开发说明](../docs/developer_instrction.md)
- [ASR客户端测试工具](../docs/asr_client_testing.md)
- [流式ASR使用指南](../docs/streaming_asr_usage.md)