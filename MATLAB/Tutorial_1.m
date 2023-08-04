% Matlab tutorial video 1
% Lisa Jacklin
% 8/3/2023
% 
% Tutorial link: https://www.youtube.com/watch?v=OHxR8iMHDWw&list=PL7CAABC40B2825C8B&ab_channel=MATLAB

% in this video we are trying to determine how efficient sojme solar panels
% are based on a formula that is displayed as sunangle.

%in order to continue through with this, you need to know that lattitude,
%degrees and a time area to study.
lat = 42 +17/60;

%this is the degrees at which we are given
dec = 23.45;

lateral = lat*pi/180;

%we need to adjust the degrees to be in radians
dec2 = dec2rad(dec); %note that this function does not work with my version on my laptop...

%this is the time ratio for every half hour from 5.30 to 10 at night.
T = 5.5:0.25:20;

LST = T - 1 + 14.6/60;

sunangle = sin(dec2) * sin(lat) + cos(dec2) * cos(lat)*cosd(LST - 12);

%from here, we can select different variables and go through and hit plot
%to setup different views of whst we are looking at.

% also note that ^ is the default for matrix math,
% use .^ to use a normal exponent setup.

%note that with a live script, you can ask to plot() and plot different
%variables.

%also note that you can plot using different variables:
%ex. plot (tablename.variablename, etc...) for anything imported.

