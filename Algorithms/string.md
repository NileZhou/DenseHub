# KMP










# Suffix Array

Given the string $s$ of length $n$ (composed of $s_0, s_1, s_2, ..., s_{n-1}$),

**suffix**

`suffix` $i$ (denoted as $suf_i$) refers to the substring of $s$ started at index $i$.

For example, $suf_3$ represents $(s_3, s_4, ..., s_{n-1})$

**Suffix Array (SA)**

Suffix Array, abbreviated as SA.

List all the suffixes of $s$ (a total of $n$), they are $suf_0, suf_1, \ldots, suf_{n-1}$ .

First, sort all these suffixes in lexicographical order (given the same prefix, no-character is the smallest; otherwise, sort according to the underlying encoding of the characters).

For example, suffixes and order rank of "camel"

Then, sort them in ascending order (From $0$ to $n-1$):

| index | suffix denote | underlying suffix | rank |
| ----- | ------------- | ----------------- | ---- |
| 0     | $suf_0$     | camel             | 1    |
| 1     | $suf_1$     | amel              | 0    |
| 2     | $suf_2$     | mel               | 4    |
| 3     | $suf_3$     | el                | 2    |
| 4     | $suf_4$     | l                 | 3    |

Let $rk[i]$ define the rank of $suf_i$, so we get $rk : (1, 0, 4, 2, 3)$


List them in the order of rank:

| rank | suffix_denote | underlying suffix |
| ---- | ------------- | ----------------- |
| 0    | $suf_1$     | amel              |
| 1    | $suf_0$     | camel             |
| 2    | $suf_3$     | el                |
| 3    | $suf_4$     | l                 |
| 4    | $suf_2$     | mel               |


**List the subscript of sorted suffix_denote, we get the `suffix array`, denoted as $sa$.**

In here is $(1, 0, 3, 4, 2)$, $sa_i$ was the **subscript** index of $i$-th sorted suffix.

*PS: Suffix arrays can do everything suffix trees(a compressed version of trie) can*


We can observe that: $rk[sa[i]] = i = sa[rk[i]]$, eg:

rk[2] = 4, sa[4] = 2


## Construction of SA


Brute Force: sort all the suffixes, times of compare/swap: $O(nlogn)$, time complexity in each substring compare: $O(n)$, so we get $O(n^2logn)$

Let we optimize it step by step !

First, we can use the concept of **Binary Lifting**, 

### Binary Lifting

1. sort all the substrings(not suffixes) of length 1 of string $s$, to compute $sa1$ and $rk1$

| index | substring denote | substring of length 1 | rank |
| :---: | :--------------: | :-------------------: | :--: |
|   0   |  $sub_{0:1}$  |           c           |  1  |
|   1   |  $sub_{1:2}$  |           a           |  0  |
|   2   |  $sub_{2:3}$  |           m           |  4  |
|   3   |  $sub_{3:4}$  |           e           |  2  |
|   4   |  $sub_{4:5}$  |           l           |  3  |

$sa1: ([1,2), [0,1), [3,4), [4,5), [2,3)) \\ rk1: (1, 0, 4, 2, 3)$

We can observe that we already get the final answer ! 




### SA-IS




## Application










# AC Automaton













# Longest Common Substring
