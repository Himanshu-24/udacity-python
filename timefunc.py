import time 
import webbrowser 

brk=0
total=5;
print("this program started at"+time.ctime())

while(brk<total):

 time.sleep(5)
 webbrowser.open("https://www.youtube.com/watch?v=i_yLpCLMaKk&list=RDi_yLpCLMaKk")
 brk = brk+1;

