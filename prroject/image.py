from PIL import Image                                                                                               
import matplotlib.pyplot as plt                                                                                     
def flip_image_horizontally(image_path):                                                                            
#打开原始图片                                                                                                  
img = Image.open(image_path)                                                                                    
#左右翻转                                                                                                       
flipped_img =                                                                                                   
img.transpose(Image.FLIP_LEFT_RIGHT)                                                                                
#并排展示原图、翻转图                                                                                           
plt.figure(figsize=(10,5))                                                                                      
plt.subplot(1,2,1)                                                                                              
plt.title("原图")                                                                                               
plt.imshow(img)