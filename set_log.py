import logging
import os


class MyLogging(logging.Logger) :
    def __init__(self, name, level=logging.INFO, file=None) :
        """

        :param name: 日志名字
        :param level: 级别
        :param file: 日志文件名称
        """
        # 继承logging模块中的Logger类，因为里面实现了各种各样的方法，很全面，但是初始化很简单
        # 所以我们需要继承后把初始化再优化下，变成自己想要的。
        super().__init__(name, level)

        # 设置日志格式
        fmt = "%(asctime)s %(name)s %(levelname)s %(filename)s--%(lineno)d line : %(message)s"
        formatter = logging.Formatter(fmt)

        # 文件输出渠道
        if file :
            handle2 = logging.FileHandler(file, encoding = "utf-8")
            handle2.setFormatter(formatter)
            self.addHandler(handle2)
        # 控制台渠道
        else :
            handle1 = logging.StreamHandler()
            handle1.setFormatter(formatter)
            self.addHandler(handle1)



current_file_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_file_dir)
# parent_dir = current_file_dir


logger = MyLogging("log", file = parent_dir + "./modify_window_size.log")
