k=imread("1.png");
k=rgb2gray(k);
SE=strel('disk',2,0);
k1=imerode(k,SE);
k2= k-k1;
imtool(k);
imtool(k2);
