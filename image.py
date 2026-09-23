from PIL import Image                                                                                               
import matplotlib.pyplot as plt                                                                                     
def flip_image_horizontally(image_path):                                                                            
	# 打开原始图片                                                                                                  
	img = Image.open(image_path)                                                                                    
	# 左右翻转图片                                                                                                       
	flipped_img  = img.transpose(Image.FLIP_LEFT_RIGHT)                                                                                
	# 并排展示原图、翻转图                                                                                           
	plt.figure(figsize=(10,5))                                                                                      
	plt.subplot(1,2,1)                                                                                              
	plt.title("原图")                                                                                               
	plt.imshow(img)
	plt.axis("off")
	plt.subplot(1,2,2)
	plt.title("左右翻转后")
	plt.imshow(flipped_img)
	plt.axis("off")
	plt.show( )
	return flipped_img
# 测试
if __name__ == "__main__":
	result_img = flip_image_horizontally("test.jpg")