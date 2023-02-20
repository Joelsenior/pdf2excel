import cv2
import time
import parallel

# 并口控制器初始化
p = parallel.Parallel()
p.setData(0)

# 视频文件路径
video_path = 'your_video_file.mp4'

# 时间列表路径
time_list_path = 'your_time_list.txt'

# 读取时间列表
with open(time_list_path, 'r') as f:
    time_list = [float(line.strip()) for line in f]

# 使用OpenCV打开视频文件
cap = cv2.VideoCapture(video_path)

# 逐帧读取视频并按时刻列表发送并口信号
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 计算当前帧的时间戳
    current_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0

    # 检查当前时间是否在时刻列表中
    if current_time in time_list:
        # 发送并口信号
        p.setData(1)
        time.sleep(0.1)  # 延迟0.1秒
        p.setData(0)

    # 在窗口中显示视频帧
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
# 这个代码将打开指定的视频文件和时间列表文件，然后使用OpenCV库按帧读取视频文件，
# 并检查当前帧的时间是否在时刻列表中。如果当前时间在列表中，则代码将发送并口信号，
# 然后在窗口中显示视频帧。

# 请注意，这只是一个基本的示例代码，并且假定你已经了解了使用OpenCV和并口控制库的
# 基本知识。如果你对这些库不熟悉，你可能需要查阅它们的文档并进行更深入的学习。