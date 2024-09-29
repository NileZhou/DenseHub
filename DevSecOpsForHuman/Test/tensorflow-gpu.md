
# GPU测试

一般测试：
```python
tf.config.list_physical_devices('GPU')
tf.test.is_gpu_available()
```


极限压测:
```python
import tensorflow as tf

# 下边这4行的意思是让tensorflow 吃显存按需增长，不会直接把显存吃光
tf.debugging.set_log_device_placement(True)
config=tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.compat.v1.Session(config=config)
import numpy as np

print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

n = 5000

for i in range(1000):
    # Place tensors on the GPU
    with tf.device('/GPU:0'):
        a = tf.constant(np.random.randn(n, n))
        b = tf.constant(np.random.randn(n, n))
        c = tf.matmul(a, b)
        d = tf.linalg.inv(c)
```




![image.png](https://cdn.nlark.com/yuque/0/2022/png/22348649/1651301412059-fe4c70ed-4673-4f91-be67-19db1b1f1a70.png#clientId=u3aefc5e6-9bed-4&from=paste&height=504&id=u55662eb2&originHeight=693&originWidth=1244&originalType=binary&ratio=1&rotation=0&showTitle=false&size=332236&status=done&style=none&taskId=u9c269896-96dd-4b2c-b91b-b0cbc80ea1f&title=&width=904.7272727272727)

![image.png](https://cdn.nlark.com/yuque/0/2022/png/22348649/1651301431432-c7a6d2d1-2717-486f-83d2-0c0d2fbe421e.png#clientId=u3aefc5e6-9bed-4&from=paste&height=468&id=u97bc8b22&originHeight=643&originWidth=1310&originalType=binary&ratio=1&rotation=0&showTitle=false&size=438537&status=done&style=none&taskId=u126ee671-8678-49e1-b717-4d913f65b32&title=&width=952.7272727272727)

申请1张tesla v100也得排1个小时
查看排队:
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22348649/1651301551484-026e0c73-136f-4ac2-9ab3-8deb9e534167.png#clientId=u3aefc5e6-9bed-4&from=paste&height=513&id=u8707668f&originHeight=706&originWidth=1339&originalType=binary&ratio=1&rotation=0&showTitle=false&size=465724&status=done&style=none&taskId=u9ed80bd6-c1b0-40e2-9fc0-3c37ba266b0&title=&width=973.8181818181819)

![image.png](https://cdn.nlark.com/yuque/0/2022/png/22348649/1651301739009-1b1f2a59-2765-4842-a479-067ff05e4974.png#clientId=u3aefc5e6-9bed-4&from=paste&height=617&id=ub3dfb430&originHeight=849&originWidth=1601&originalType=binary&ratio=1&rotation=0&showTitle=false&size=628099&status=done&style=none&taskId=ueee3ab6e-2aed-4edf-b567-12ce576060c&title=&width=1164.3636363636363)