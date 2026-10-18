import cv2
img = cv2.imread('../images/test.jpg')
if img is None:
    print("读取失败：图片路径不对，或者文件不存在")
else:
    print("图片尺寸:",img.shape)
    cv2.imshow("test",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("../imagse/test.jpg",img)