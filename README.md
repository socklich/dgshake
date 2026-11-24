# Shake Coyote

单文件网页：用手机陀螺仪/加速度触发郊狼 3.0（DG-LAB Coyote V3）输出。

- 在线地址：https://luke7628.github.io/DG/
- iPhone：用 **Bluefy** 浏览器打开；Android：Chrome。
- 协议参考：https://github.com/sdewis/dg-lab-opensource-english/blob/main/coyote/v3/README_V3.md

## 用法
1. 连接郊狼（名称前缀 `47L121`），连接后自动写入 BF 软上限（默认 200，可在页面里调低）。
2. 启用陀螺仪 → 调阈值、输出时长、波形。
3. 点「启用触发」，晃动超过阈值即输出一段波形；「停止」立即把 A/B 强度归零。

页面进入后台时会自动解除触发。请从低强度开始。
