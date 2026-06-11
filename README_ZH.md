# 开普勒轨道动力学与三维交互式实验室

这是一个开源的教学和研究仓库，展示了开普勒轨道力学、天体动力学、软件设计模式以及国际化（i18n）规范。该仓库可用于卫星系统建模，特别适用于欧洲的 IRIS² 卫星星座。

---

## 主要特点

- **开普勒方程求解器**：利用牛顿-拉夫逊方法，高效、高精度地数值求解开普勒方程（$M = E - e \sin E$）。
- **多语言支持**：实时本地化翻译机制，支持英文、西班牙文和中文（简体）。
- **三维交互式可视化**：基于 Plotly 和 ipywidgets，在深色背景主题下展示带有半透明地球的交互式轨道图形。
- **轨道分类**：直接建模并对比近地轨道（LEO）、中地球轨道（MEO）、地球静止轨道（GEO）以及高椭圆轨道（HEO）。
- **IRIS² 多轨道星座建模**：研究低轨与中轨混合星座，分析延迟、覆盖范围以及现代 New Space（新航天）系统架构。
- **软件设计模式**：完美实现策略模式（Strategy）、模板方法模式（Template Method）、观察者模式（Observer）、外观模式（Facade）和注册表模式（Registry）。
- **游戏化进度系统**：本地成就引擎，记录并跟踪学生在 Jupyter Notebook 挑战中的学习进度。

---

## 技术栈与系统架构

### 技术栈
- **核心逻辑**：Python 3.9+
- **数学与数值计算**：NumPy
- **数据可视化**：Plotly
- **交互小部件**：ipywidgets, JupyterLab
- **自动化测试**：pytest

### 系统架构分层
本库采用分层架构设计，使物理逻辑、呈现形式以及基础设施相互解耦：

1. **领域层 (Domain Layer)**：`kepler.py`, `orbits.py`, `constants.py`, `types.py` —— 包含基本数学算法和轨道物理规则。
2. **应用层 (Application Layer)**：`i18n.py`（注册表模式）、`gamification.py`（观察者模式） —— 提供公共应用逻辑。
3. **展示层 (Presentation Layer)**：Jupyter 交互式笔记本（`notebooks/`）与命令行运行示例（`examples/`）。
4. **基础设施层 (Infrastructure Layer)**：本地化翻译文件（`locales/*.json`）与成就元数据（`assets/badges/*.json`）。

有关设计模式和详细架构的说明，请参考 [ARCHITECTURE.md](ARCHITECTURE.md) 和 [docs/design_patterns.md](docs/design_patterns.md)。

---

## 安装说明

```bash
# 克隆代码仓库
git clone https://github.com/your-username/gnss-orbital-py.git
cd gnss-orbital-py

# 创建并激活虚拟环境
python -m venv .venv
source .venv/bin/activate  # Windows 用户: .venv\Scripts\activate

# 以可编辑模式安装此包并包含开发依赖
pip install -e .
```

---

## 快速上手

### 运行命令行示例
您可以直接通过命令行运行示例脚本。使用 `--lang` 参数指定所需语言（`en`, `es`, `zh`）：

```bash
# 运行低轨（LEO）卫星轨道外推
python examples/leo_orbit.py --lang zh

# 运行多种轨道类型的对比 (LEO, MEO, GEO, HEO)
python examples/orbit_comparison.py --lang en
```

### 打开 Jupyter 交互式笔记本
启动 Jupyter 环境以交互式地研究轨道：

```bash
jupyter lab
```

然后在左侧侧边栏中选择以下笔记本：
1. `notebooks/01_interactive_orbits.ipynb`：经典轨道六要素的交互式三维可视化学习。
2. `notebooks/02_kepler_equation.ipynb`：开普勒数值求解器的收敛性与容差分析。
3. `notebooks/03_iris2_constellation.ipynb`：欧洲 IRIS² 低轨与中轨混合星座的仿真与建模。

---

## 游戏化成就系统

本平台内置了一个免后台的本地成就系统。当您在笔记本中完成挑战任务后，系统将自动解锁相应的徽章，并保存在本地路径 `~/.gnss-orbital/progress.json` 中。

- **铜牌：轨道探索者 (Orbit Explorer)** —— 成功模拟了一条低地球轨道 (LEO)。
- **铜牌：开普勒学徒 (Keplerian Apprentice)** —— 首次使用数值方法成功解出开普勒方程。
- **银牌：轨道领航员 (Orbital Navigator)** —— 成功修改全部 6 个经典轨道六要素并完成轨道外推。
- **银牌：轨道分析师 (Trajectory Analyst)** —— 并排对比分析了四种标准地球轨道类型。
- **金牌：航天飞行员 (Space Pilot)** —— 设计并完成了一条从低地球轨道到地球静止轨道的霍曼转移。
- **大师：IRIS2 星座架构师 (IRIS2 Constellation Designer)** —— 完成了欧洲 IRIS² 复杂多轨道星座的模型构建。

---

## 参考文献与学习资源

1. David A. Vallado, *Fundamentals of Astrodynamics and Applications*, 第4版.
2. Howard D. Curtis, *Orbital Mechanics for Engineering Students*, Elsevier.
3. 欧盟委员会 (European Commission), *IRIS²: Infrastructure for Resilience, Interconnection and Security by Satellite*.
4. CDIO 教育模式倡议 (CDIO Initiative) 对工程实践能力的指导。

---

## 开源协议

本软件采用 MIT 开源协议。详情请查阅项目中的 `LICENSE` 文件。
