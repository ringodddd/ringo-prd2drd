# ringo-prd2drd

一个把 PRD 转成可评审数据需求文档（DRD）的通用 Agent Skill 工作流。

核心原则是把“分析”和“交付”分开：先阅读 PRD、梳理业务目标与分析问题，生成待确认的采集点；只有在用户明确确认后，才生成最终 DRD JSON。

## 工作流

```text
PRD
  ↓
需求分析与采集点草案
  ↓
用户确认（硬门禁）
  ↓
DRD JSON
  ↓
Schema 校验
```

仓库内包含三个 Cursor/Codex 兼容的 Skill：

- `prd2drd`：总控与阶段路由
- `prd-analysis`：PRD 分析和采集点草案
- `drd-builder`：生成、校验最终 DRD

## 使用方式

1. 将本仓库加入 Agent 的工作目录。
2. 提供 PRD 正文或 Agent 可读取的 PRD 文件。
3. 说“根据 PRD 生成 DRD”。
4. 审阅采集点草案。
5. 明确回复“采集点确认，可以生成 DRD”。

最终文件默认写入 `outputs/`。该目录不会进入 Git。

## 本地配置

如需接入你自己的项目系统、文档系统或事件元数据，复制示例配置：

```bash
cp config.example.json config.local.json
```

只在 `config.local.json` 中填写本地路径、私有地址或标识。这个文件已被 Git 忽略。

## 校验 DRD

安装依赖：

```bash
python3 -m pip install -r requirements.txt
```

执行校验：

```bash
python3 scripts/validate_drd.py outputs/example-drd.json
```

## 隐私与发布安全

此公开仓库不包含：

- 真实 PRD、生成结果或过程文件
- 业务知识库和事件元数据
- 公司内部链接、空间标识、节点标识或账号信息
- 真实业务事件、属性、版本和项目案例

提交前建议运行：

```bash
git status --short
git ls-files
```

确认待提交文件中没有本地配置、输入文档、业务数据或生成结果。

## 目录结构

```text
.cursor/skills/        Agent Skills
schemas/drd.schema.json  通用 DRD JSON Schema
scripts/validate_drd.py  DRD 校验脚本
config.example.json      无敏感信息的配置模板
outputs/                 本地生成目录（Git 忽略）
```

## 设计边界

- 不从信息不足的 PRD 中编造事件、属性、平台或负责人。
- 未经用户确认，不生成最终 DRD。
- 私有知识库仅在本地读取，不复制进分析文档或仓库。
- 示例名称必须使用虚构数据，不能替换成线上真实案例。
