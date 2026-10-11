# 麦式 Skills：把踩过的坑，变成别人能用的小工具

首批发布四个公开版，采用 [MIT 协议](LICENSE)，允许商用和修改。每个技能都有中英 README。每份都给明确触发场景、短工作流和虚构示例，UTF-8 版还带可直接运行的只读检查器。

| 技能 | 解决的具体麻烦 | 当前公开版 |
|---|---|---|
| [视频渐进精读](skills/video-progressive-review/README.md) | 看长视频时只读相关画面，小字回原视频取高清帧 | 方法包；需要使用者自己的抽帧、拼图和看图工具 |
| [Windows 防乱码](skills/windows-utf8-mojibake-guard/README.md) | 终端显示异常就误改正常中文文件 | 工作流 + Python 标准库只读检查器 |
| [麦式毒舌自检](skills/toxic-pm/README.md) | 本地能跑就说已上线，生成文件就说做完了 | 交付宣称、现实证据和最小修补工作流 |
| [短请求补全](skills/short-message-completion/README.md) | 用户说“短点”“就这个”以后，又被问一堆重复问题 | 从最近上下文接住对象，保留事实，直接交成品 |

使用方法：把选中的 `skills/<技能名>` 文件夹放入所用 Agent 宿主的技能目录，按照该宿主的实际说明验证发现和调用。也可以把入口与示例交给 Agent 做一次显式试用。本包遵循 [Agent Skills 格式](https://agentskills.io/specification)，不同宿主的真实行为需要各自测试。

署名：麦克 / Micker / Ghoscro 与 AI 协作者，麦式方法。原创贡献指本地设计和维护的工作流组合、约束和工具；通用编码知识、视频抽帧、拼图、质量审计等已有方法保留其来源边界。

版本 1.0.0。再分发时保留版权与许可声明。包内使用虚构示例；私人记忆、用户资料、凭据、部署细节和完整内部自动化保留在本地。更多候选见 [目录](CATALOG.md)，发布状态见 [说明](RELEASE_STATUS.md)。
