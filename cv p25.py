a=imread("D:\open cv\Picture4.png");
Lap=[0, 1, 0, 1, -4, 1, 0, 1, 0];
a1=conv2(a,Lap,"D:\open cv\Picture4.png");
a2=uint8(a1);
imtool(abs(a-a2),[])
lap=[-1 ,-1, -1, -1, 8, -1, -1, -1 ,-1];
a3=conv2(a,lap,"D:\open cv\Picture4.png");
a4=uint8(a3);
imtool(abs(a+a4),[])
