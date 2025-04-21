# Argon2id Password Generator

这是一个基于Argon2id密钥派生函数的安全密码生成工具。该工具可以从您的主密码（记忆密码）和服务标识符（区分密码）派生出强密码，无需存储任何密码。

## 特点

- 使用Argon2id密钥派生函数（2015年密码哈希竞赛获胜者）
- 对每个服务生成唯一且可重复的密码
- 可自定义密码长度和字符集（大小写字母、数字、特殊字符）
- 命令行界面，易于使用
- 不存储任何密码，完全基于您输入的信息进行派生
- 可调整的安全参数（内存成本、时间成本、并行度）

## 安装

1. 克隆这个仓库：
```
git clone https://github.com/yourusername/argon2-password-generator.git
cd argon2-password-generator
```

2. 安装依赖：
```
pip install -r argon2_password_generator_requirements.txt
```

## 使用方法

### 基本用法

```
python argon2_password_generator.py -s github.com -l 20
```

这将提示您输入主密码，然后为"github.com"生成一个20字符长的密码。

### 命令行选项

```
usage: argon2_password_generator.py [-h] [-s SERVICE] [-l LENGTH] [--no-lowercase] [--no-uppercase] [--no-digits] [--no-special] [-m MEMORY] [-t TIME] [-p PARALLELISM]

Generate secure passwords using Argon2id

options:
  -h, --help            显示帮助信息并退出
  -s SERVICE, --service SERVICE
                        服务或网站标识符
  -l LENGTH, --length LENGTH
                        密码长度 (默认: 16)
  --no-lowercase        排除小写字母
  --no-uppercase        排除大写字母
  --no-digits           排除数字
  --no-special          排除特殊字符
  -m MEMORY, --memory MEMORY
                        内存成本 (默认: 65536 KiB)
  -t TIME, --time TIME  时间成本 (默认: 3)
  -p PARALLELISM, --parallelism PARALLELISM
                        并行度 (默认: 4)
```

### 示例

1. 生成包含所有字符类型的24字符密码：
```
python argon2_password_generator.py -s amazon.com -l 24
```

2. 生成只包含字母和数字的16字符密码：
```
python argon2_password_generator.py -s gmail.com --no-special
```

3. 生成只包含大写字母和数字的12字符密码：
```
python argon2_password_generator.py -s bank.com -l 12 --no-lowercase --no-special
```

## 安全注意事项

- 主密码应当复杂且长度足够（建议至少12个字符）
- 服务标识符应当唯一且一致，建议使用完整域名
- 增加内存和时间成本参数可以提高安全性，但会增加密码生成的时间
- 建议在本地执行，不要在不可信的系统上使用

## 工作原理

该工具结合您的主密码和服务标识符，使用Argon2id密钥派生函数生成确定性的强密码。只要输入相同的主密码和服务标识符，就会生成相同的密码，因此您无需存储生成的密码。

## 许可证

MIT 