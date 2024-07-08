
# Algorithms in my career



## Automaton

NFA: 正则表达式，流中匹配模式串

[Aho Corasick自动机](https://www.hankcs.com/program/algorithm/aho-corasick-double-array-trie.html) + Double Array Trie: 从流中识别模式串  [Aho Corasick自动机结合DoubleArrayTrie极速多模式匹配](https://www.hankcs.com/program/algorithm/aho-corasick-double-array-trie.html)

神器：能将正则表达式对应的自动机画出来 https://cyberzhg.github.io/toolbox/nfa2dfa



## Suffix Array


```shell
Let the given string be "banana".

0 banana                          5 a
1 anana     Sort the Suffixes     3 ana
2 nana      ---------------->     1 anana  
3 ana        alphabetically       0 banana  
4 na                              4 na   
5 a                               2 nana

So the suffix array for "banana" is {5, 3, 1, 0, 4, 2}
```


https://oi-wiki.org/string/sa/


SA构建方法:
1. DC3算法 O(n)
https://www.cs.helsinki.fi/u/tpkarkka/publications/jacm05-revised.pdf
https://wenku.baidu.com/view/5b886b1ea76e58fafab00374.html?_wkts_=1718990454825&needWelcomeRecommand=1


2. 诱导排序与SA-IS算法 O(n)
https://riteme.site/blog/2016-6-19/sais.html



应用场景:
1. 对于目标串T, 在线地(查的次数多，P会变)在T中查找是否有匹配模式串PAT的子串。时间复杂度为 $O(|S|log|T|)$




## 控制算法

Lyapunov函数法是一种常用于系统稳定性分析的方法。这种方法和Lyapunov第二方法有关，该方法主要用于动态系统的稳定性理论和控制理论。Lyapunov函数法提供了一种标量函数，可以用于证明一个常规微分方程的平衡状态的稳定性。对于某些类型的常规微分方程，Lyapunov函数的存在是稳定性的必要和充分条件。然而，对于常规微分方程的Lyapunov函数的构造没有通用的技术。Lyapunov函数法的一个主要优点是它能够避免直接解微分方程，而只需要考虑与系统的稳定性和性能有关的一些性质。

PID（比例-积分-微分）控制器是一种含有反馈机制的控制回路，广泛应用于各种需要连续调整控制的场景。PID控制器根据误差值的大小、积累和变化率，计算出一个修正值，用于调整被控制的过程。这三种控制参数分别由比例项（P）、积分项（I）和微分项（D）生成，它们三者结合起来产生控制器的输出。

在大多数情况下，想要获得稳定且高性能的控制系统，需要通过适当的调谐才能找到最佳的PID参数。这个过程是一个优化问题，尝试找到可以使系统性能达到最优的PID参数。在很多情况下，也可以借助Lyapunov函数法来设计和调整PID控制器，确保整个控制系统的稳定性和性能。

总的来说，Lyapunov函数法和PID控制方式都是两种解决控制问题的重要方法，它们在各自的领域都发挥着巨大的作用。

### PID
应用场景:

1. 业务金额控制

2. 并发水位控制

3. 调控用户请求，达到CPU水位控制

4. 调控画质档速，达到缓存/画质控制

5. 服务质量（QoS）保证：在云计算环境中，PID 算法常用来保证服务质量。例如，在动态调整虚拟机资源分配（如 CPU、内存等）以满足服务级别协议（SLA）的场景中，PID 算法能帮助系统对波动的工作负载进行响应。

6. 流量控制：在互联网服务中，流量控制是非常重要的一环。PID 算法可以用于动态调整系统的输入和输出速率，以防止网络拥塞和服务过载。例如在CDN(Content Delivery Network)中就存在这样的应用。

7. 系统性能优化：在软件系统中，往往需要对系统性能进行实时优化，例如内存使用、数据库查询、系统延迟等。PID 控制算法可以用来自动调整系统参数以优化系统性能。

8. 广告竞价：在互联网广告投放系统中，PID 算法也得到了应用。通过使用 PID 算法，广告系统可以动态调整出价，以在满足广告商的预算和目标的同时，尽可能地获取更多的曝光



## 分布式实时协同

比如在线文档，多人编辑解决冲突的问题

可以用的算法：

1. GNU's diff-patch
2. Myer’s diff-patch
3. Operational Transformation (Google docs中的方案)
4. 分布式Operational Transformation (这才是难)

