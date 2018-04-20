clear all
path1='F:\Fanzhenjia\video\2017-04-20-11-00-18_DataSets\JPEGImages';
path2='F:\Fanzhenjia\refinenet-master\refinenet-master\cache_data\test_examples_cityscapes\result_20170712174947_evaonly_custom_data\predict_result_mask';
im1=dir(path1);
im2=dir(path2);
label=imread('legendRGB.jpg');
label=imresize(label,[2160,452]);

aviobj = VideoWriter('sun.avi');
aviobj.FrameRate = 10;
open(aviobj)
for i=3:length(im1)
    disp(i);
    [seg_img,ind]=imread([path2,'\',im2(i).name]);
    seg_img=uint8((ind2rgb(seg_img,ind))*255);
    init_img=imread([path1,'\',im1(i).name]);
    I=[seg_img;init_img];
    I=[I,label];
    writeVideo(aviobj,I); 
end
close(aviobj);

% fileName = 'example.avi'; 
% obj = VideoReader(fileName);
% figure,imshow(I)