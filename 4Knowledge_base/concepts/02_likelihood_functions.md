---
document_id: concept_likelihood_001
title: 假设评价中的硬似然与软似然
aliases:
  - 似然函数
  - 硬似然
  - 软似然
  - deterministic likelihood
  - soft likelihood
category: concept
course: Causal Reasoning
source_document: day3_handout(1).pdf
source_pages: 3-4
status: active
data_type: source_summarized
language: zh-CN
---

# 假设评价中的硬似然与软似然

## 核心定义

似然函数 $P(d\mid h)$ 衡量：如果假设 $h$ 为真，观察到数据 $d$ 的可能性有多大。它不是假设本身的概率，而是用数据评价假设与观察结果的一致程度。

在因果程序的表示中，假设 $h$ 对应函数：

$$
f_h:(a,r)\mapsto r',
$$

数据则记录一次实际观察到的因果交互 $d=(a_i,r_i,r_i')$。

## 硬似然

对于确定性假设，可以使用严格的一致性判断：

$$
P(d\mid h)=\mathbf{1}[f_h(a_i,r_i)=r_i'].
$$

如果假设的预测与观察完全一致，似然为 1；否则为 0。这样能够快速排除与数据冲突的假设，但无法表达“部分正确”或“接近正确”。

## 软似然

如果观察过程存在噪声，或预测结果允许近似匹配，可以使用软似然：

$$
P(d\mid h)=\frac{1}{Z}\exp\left(-\beta\,\mathrm{dist}(f_h(a_i,r_i),r_i')\right).
$$

其中：

- $\mathrm{dist}(\cdot,\cdot)$ 衡量预测与观察之间的差异，例如汉明距离或平方误差；
- $\beta\geq 0$ 控制对偏差的惩罚强度；
- $Z$ 是归一化常数，使结果构成合法概率分布。

预测越接近实际观察，似然越高。即使预测不完全正确，假设也可以保留非零概率。

## 参数 $\beta$ 的作用

$\beta$ 越大，模型越严厉地惩罚预测误差；$\beta$ 越小，模型对误差越宽容。当 $\beta\to\infty$ 时，软似然趋近于硬似然。

## 如何选择

- 任务规则完全确定、观测几乎无误差时，可以使用硬似然。
- 数据可能含噪声、结果具有连续差异或需要保留近似假设时，更适合使用软似然。

## 常见误区

**似然是否等于后验概率？**  
不是。似然只评价数据在某个假设下出现的可能性；后验概率还需要结合假设的先验概率。

**似然为 0 有什么后果？**  
在标准贝叶斯更新中，只要某个数据点使假设的总体似然为 0，该假设的后验概率也会变为 0。

## 来源定位

- `day3_handout(1).pdf`，第 3-4 页：确定性似然、软似然、距离函数与 $\beta$ 的解释。

