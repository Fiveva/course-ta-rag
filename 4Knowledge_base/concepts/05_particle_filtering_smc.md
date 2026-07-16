---
document_id: concept_smc_001
title: 粒子滤波与序贯蒙特卡洛
aliases:
  - 粒子滤波
  - Particle Filtering
  - 序贯蒙特卡洛
  - Sequential Monte Carlo
  - SMC
  - 有效样本量
  - ESS
category: concept
course: Causal Reasoning
source_document: day4_handout(1).pdf
source_pages: 5-6
status: active
data_type: source_summarized
language: zh-CN
---

# 粒子滤波与序贯蒙特卡洛

## 核心定义

粒子滤波，又称序贯蒙特卡洛（SMC），使用一组带权假设来近似后验分布，并在每个新观察到来时在线更新。

每个粒子 $j$ 包含一个假设 $h_n^{(j)}$ 和权重 $w_n^{(j)}$。权重非负且总和为 1：

$$
\sum_{j=1}^{M}w_n^{(j)}=1.
$$

这组粒子用离散的经验分布近似后验：

$$
P(h\mid D_n)\approx
\sum_{j=1}^{M}w_n^{(j)}\delta_{h_n^{(j)}}(h).
$$

## 初始化

观察数据前，从先验分布中抽取 $M$ 个粒子，并给予相同权重：

$$
h_0^{(j)}\sim P(h),\qquad w_0^{(j)}=\frac{1}{M}.
$$

## 权重更新

新数据 $d_n$ 到来后，用该数据在每个假设下的似然更新权重：

$$
\widetilde{w}_n^{(j)}
=w_{n-1}^{(j)}P(d_n\mid h_{n-1}^{(j)}),
$$

然后归一化：

$$
w_n^{(j)}=
\frac{\widetilde{w}_n^{(j)}}{\sum_{\ell}\widetilde{w}_n^{(\ell)}}.
$$

因此，能更好解释新数据的粒子获得更高权重。

## 有效样本量（ESS）

反复更新后，权重可能退化：少数粒子拥有几乎全部权重，其余粒子贡献很小。有效样本量用于诊断这种情况：

$$
\mathrm{ESS}=\frac{1}{\sum_{j=1}^{M}(w_n^{(j)})^2}.
$$

所有权重相等时，$\mathrm{ESS}=M$；一个粒子权重为 1 时，$\mathrm{ESS}=1$。实践中可在 ESS 低于阈值（如 $M/2$）时触发重采样。

## 重采样与复壮

重采样按照当前权重复制高权重粒子、淘汰低权重粒子，并把新粒子的权重重新设为 $1/M$。这能缓解权重退化，但会产生大量重复粒子，降低多样性。

为恢复多样性，可以对重采样后的粒子执行若干次以当前后验为目标的 MH 移动。这个步骤称为复壮（rejuvenation）。在 PCFG 假设空间中，可以使用子树再生成作为 MH 提议。

## 与 MCMC 的区别

- MCMC 通常在观察全部数据后，通过一条马尔可夫链近似完整后验；
- 粒子滤波在数据依次到来时更新粒子与权重，更适合在线学习；
- 粒子滤波也可以在复壮阶段结合 MH。

## 常见问题

**粒子数量越多是否越好？**  
粒子越多通常能更细致地近似后验，但计算成本也更高。粒子数量需要在精度和效率之间权衡。

**为什么只重采样还不够？**  
重采样会复制高权重粒子，容易使粒子集合失去多样性；复壮步骤帮助重复粒子探索邻近的新假设。

## 来源定位

- `day4_handout(1).pdf`，第 5-6 页：粒子表示、权重更新、ESS、重采样与复壮。

