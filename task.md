先给了四张 sample，考试结束后评分用 test 看，只看结果没看代码，评分时不允许调参（除了修改文件路径）

1. 任务一，转为灰度图；
    - `cvtColor()`
2. 任务二，大小调整为 1224*1024 并保存为 resize.bmp
    - `resize()`
3. 任务三，找出所有黄色小块，用绿色框框住
    - `inRange()`
    - `findContours()`
4. 任务四，找出所有小块，用绿色框框住
    - `inRange()`
    - `findContours()`
5. 任务五，找出所有小块，用绿色框框住，并在旁边注释颜色
    - `inRange()`
    - `findContours()`
    - `putText()`
6. 任务六，识别蓝色小块的二维码信息，输出（这个题偷懒了，示例图片和test图片恰好只有蓝色小块上有信息）
    - pyzbar
7. 任务七，标注所有小块的位置（1-9，左上为1，右上为3，右下为9）
    - 感觉上可以找钉子或者九宫格作为位置参考，任务五找到的轮廓的重心算相对位置
    - 钉子可以用霍夫圆或者模板匹配去找
    - 当然如果赌test和sample托盘位置差不多的的话可以直接用图片重心作为参考位置