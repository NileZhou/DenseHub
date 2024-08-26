基础语法

| 比较项                                  | Go                                                                   | Java                         |
| --------------------------------------- | -------------------------------------------------------------------- | ---------------------------- |
| 在定义一个结构体/类时，给属性设置初始值 | 不能                                                                 | 能                           |
| nil/null有无默认类型                    | 无，需要根据上下文判断是哪种类型的nil。不同类型的nil变量不能相互赋值 | 本质也无，但可以指向任何对象 |

性能对比

来自专业团队，多个benchmark的对比：

[https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/go.html](https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/go.html)
