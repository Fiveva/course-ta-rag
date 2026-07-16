# Application Configuration

## Application
- Type: Chatflow / RAG-based Course QA Application
- Model: GLM-4.5-Air
- Reasoning mode: false
- Temperature: 0.2

## Knowledge Retrieval
- Knowledge base: Course-TA
- Retrieval mode: Hybrid / Vector
- Top K: 3
- Score threshold: 未启用
- Rerank: 未启用

## Generation Rules
- 仅根据知识库证据回答
- 没有可靠依据时明确拒答
- 不提供可直接提交的作业答案
- 不披露学生成绩和个人反馈
- 回答中标明文档、渠道和发布时间
- 不输出内部思考过程或 `<think>` 标签

## Version
- V0: baseline
- V1: optimized document structure and generation configuration