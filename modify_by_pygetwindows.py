import pygetwindow as gw
import re
from set_log import logger


def modify_by_pygetwindows(pattern, width, height, offset_x, offset_y) :
    logger.info("modify_by_pygetwindows()")
    logger.info((pattern, width, height, offset_x, offset_y))
    # 列出所有窗口标题
    window_titles = gw.getAllTitles()
    logger.info('列出所有窗口标题 {}'.format(window_titles))

    # 使用正则表达式匹配窗口标题
    matched_titles = [title for title in window_titles if re.search(pattern, title)]
    logger.info('匹配到的窗口列表 {}'.format(matched_titles))
    if not matched_titles:
        logger.warning('未匹配到窗口')
        return 0

    try :
        for title in matched_titles :
            # print(title)
            # 获取窗口对象列表
            windows = gw.getWindowsWithTitle(title)
            for window in windows :
                logger.info(window)
                # 设置窗口大小和位置
                logger.info('resizeTo %s %s %s %s' % (width, height, offset_x, offset_y))
                window.resizeTo(width, height)
                window.moveTo(offset_x, offset_y)
        return 1
    except Exception as e :
        logger.error('modify_by_pygetwindows() error {]'.format(e))


# if __name__ == '__main__' :
#     res = modify_by_pygetwindows(pattern = 'Fcms', width = 200, height = 200, offset_x = -100, offset_y = -100)
#     print(res)
