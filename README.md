# Argon2id 密码生成器

这是一个基于Argon2id密钥派生函数的安全密码生成工具。该工具可以从您的主密码（记忆密码）和服务标识符（区分密码）派生出强密码，无需存储任何密码。

## 特点

- 使用Argon2id密钥派生函数（2015年密码哈希竞赛获胜者）
- 对每个服务生成唯一且可重复的密码
- 可自定义密码长度和字符集（大小写字母、数字、特殊字符）
- 方便的Web界面，无需安装
- 不存储任何密码，完全在浏览器本地运行
- 可调整的安全参数（内存成本、时间成本、并行度）

## 使用方法

### 在线使用

访问 [https://moonlovelj.github.io/PasswordGenerator/](https://moonlovelj.github.io/PasswordGenerator/) 即可在线使用该工具。

### 界面使用说明

1. 输入您的主密码 - 这是您需要记住的密码
2. 输入服务标识符 - 这是用来区分不同网站/应用的标识，如"github.com"
3. 选择密码长度和字符集选项
4. 点击"生成密码"按钮
5. 使用"复制"按钮将生成的密码复制到剪贴板

## 高级选项

您可以调整以下安全参数来增强安全性：

- **内存成本**：用于哈希计算的内存量，默认为65536 KiB
- **时间成本**：哈希迭代次数，默认为3
- **并行度**：并行计算的线程数，默认为4

增加这些参数会提高生成密码的安全性，但也会增加生成密码所需的时间和资源。

## 安全注意事项

- 主密码应当复杂且长度足够（建议至少12个字符）
- 服务标识符应当唯一且一致，建议使用完整域名
- 增加内存和时间成本参数可以提高安全性，但会增加密码生成的时间
- 所有处理都在本地浏览器中完成，您的主密码不会被发送到任何服务器

## 工作原理

该工具结合您的主密码和服务标识符，使用Argon2id密钥派生函数生成确定性的强密码。只要输入相同的主密码和服务标识符，就会生成相同的密码，因此您无需存储生成的密码。

## 许可证

MIT 