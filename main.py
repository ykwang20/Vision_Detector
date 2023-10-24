import cv2
import numpy as np

# 指定图像文件的绝对路径
image_path = r'D:\ProductCV\Vision_Detector\Cable_3_in_a_View.jpg'

# 读取图像
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# 使用Sobel算子进行边缘检测
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# 合并x和y方向的边缘检测结果
edges = np.sqrt(sobel_x**2 + sobel_y**2)

# 将边缘结果转换为8位图像
edges = np.uint8(edges)

# 显示原始图像
cv2.imshow('Original Image', image)

# 显示边缘检测结果
cv2.imshow('Edge Detection (Sobel)', edges)

# 等待按下任意键后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
