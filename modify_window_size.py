# coding=utf-8
import wx
from set_log import logger
import yaml
from datetime import datetime
from modify_by_pygetwindows import modify_by_pygetwindows


# 读取config.yaml配置文件
def read_configyaml() :
    try :
        logger.info("Reading config.yaml")
        case_path = './config.yaml'
        f = open(case_path, 'r', encoding = 'utf-8')
        res = f.read()
        # print(res)
        res = yaml.safe_load(res)
        f.close()
        return res
    except Exception as e :
        logger.error(e)


# config.yam数据
datas = read_configyaml()
pattern = datas['pattern']
width = datas['width']
height = datas['height']
offset_x = datas['offset_x']
offset_y = datas['offset_y']
use_function = datas['use_function']
selfpos_x = datas['selfpos_x']
selfpos_y = datas['selfpos_y']



class MaimFrame(wx.Frame) :
    def __init__(self, parent, id) :
        panel1_w = 160
        panel1_h = 160
        panel5_h = 50
        wx.Frame.__init__(self, parent, id, title = "modify_window_size", pos = (selfpos_x, selfpos_y),
                          size = (panel1_w * 3, panel1_h + panel5_h + 40))
        # 创建第一个面板

        panel = wx.Panel(self, pos = (0, 0), size = (panel1_w, panel1_h))
        # 控件
        self.text_pattern = wx.StaticText(panel, label = "pattern", pos = (5, 10))
        self.text_width = wx.StaticText(panel, label = "width", pos = (5, 40))
        self.text_height = wx.StaticText(panel, label = "height", pos = (5, 70))
        self.text_offset_x = wx.StaticText(panel, label = "offset_x", pos = (5, 100))
        self.text_offset_y = wx.StaticText(panel, label = "offset_y", pos = (5, 130))

        # 控件
        self.label_pattern = wx.TextCtrl(panel, pos = (65, 10), size = (85, 20), style = wx.TE_LEFT)
        self.label_width = wx.TextCtrl(panel, pos = (65, 40), size = (85, 20), style = wx.TE_LEFT)
        self.label_height = wx.TextCtrl(panel, pos = (65, 70), size = (85, 20), style = wx.TE_LEFT)
        self.label_offset_x = wx.TextCtrl(panel, pos = (65, 100), size = (85, 20), style = wx.TE_LEFT)
        self.label_offset_y = wx.TextCtrl(panel, pos = (65, 130), size = (85, 20), style = wx.TE_LEFT)

        # 设置控件默认值
        self.label_pattern.SetValue(pattern)
        self.label_width.SetValue(str(width))
        self.label_height.SetValue(str(height))
        self.label_offset_x.SetValue(str(offset_x))
        self.label_offset_y.SetValue(str(offset_y))

        # 创建第二个面板（----------------测试结果显示框-----------------------------）
        panel1 = wx.Panel(self, pos = (panel1_w, 0), size = (panel1_w * 2 - 15, panel1_h + panel5_h))
        self.show_text = wx.TextCtrl(panel1, id = -1, value = '', pos = (0, 0),
                                     size = (panel1_w * 2 - 15, panel1_h + panel5_h + 40),
                                     style = wx.TE_MULTILINE | wx.TE_READONLY)

        # 修改窗口大小按钮
        panel5 = wx.Panel(self, pos = (0, panel1_h + 1), size = (panel1_w, panel5_h))
        self.get_lst = wx.Button(panel5, label = '修改窗口大小', pos = (5, 10), size = (100, 30))
        self.get_lst.Bind(wx.EVT_BUTTON, self.get_lsts)

    def append_txt(self, infostr) :
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # print(current_time)
        self.show_text.AppendText('{0} {1}\n'.format(current_time, infostr))

    # 获取修改窗口大小
    def get_lsts(self, event) :
        self.append_txt('use_function == {}'.format(use_function))
        if use_function == 1 :
            result = modify_by_pygetwindows(pattern = self.label_pattern.GetValue(),
                                            width = int(self.label_width.GetValue()),
                                            height = int(self.label_height.GetValue()),
                                            offset_x = int(self.label_offset_x.GetValue()),
                                            offset_y = int(self.label_offset_y.GetValue()), )
        else :
            result = '9999'
        # 断言
        if result == 1 :
            self.append_txt('修改窗口位置成功')
        else :
            self.append_txt('修改窗口位置失败，检查参数是否正确')


def main() :
    app = wx.App()
    win = MaimFrame(parent = None, id = -1)  # 创建窗体
    win.Show()  # 显示窗体
    app.MainLoop()  # 运行程序


if __name__ == "__main__" :
    main()
