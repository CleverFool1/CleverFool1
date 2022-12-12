clear all
close all
clc


a = input('请输入区间左端点:a=');
b = input('请输入区间右端点:b=');
eps=input('请输入停止精度要求:eps=');
k=1;
m=(a+b)/2;
n=(a+b)/2;
fprintf('        m        n  \n' );


y='((m-30)/40)/(abs((m-30)/40))*4.7*0.003*((9.81^4)*(10^6)*0.003^(5)*((m-30)/40)^4)^(1/7)+((m-H8)/40)/(abs((m-H8)/40))*4.7*0.003*((9.81^4)*(10^6)*0.003^(5)*((m-H8)/40)^4)^(1/7)';
f1=inline(y,'m','H8');

z='((n-H5)/40)/(abs((n-H5)/40))*4.7*0.003*((9.81^4)*(10^6)*0.003^(5)*((n-H5)/40)^4)^(1/7)+((n-20)/20)/(abs((n-20)/20))*4.7*0.003*((9.81^4)*(10^6)*0.003^(5)*((n-20)/20)^4)^(1/7)';
f2=inline(z,'n','H5');

H8=29.7;
H5=29.7;

syms mm;
ff1=((mm-30)/40)/(abs((mm-30)/40))*4.7*0.003*((9.81^4)*(10^6)*0.003^(5)*((mm-30)/40)^4)^(1/7)+((mm-H8)/40)/(abs((mm-H8)/40))*4.7*0.003*((9.81^4)*(10^6)*0.003^(5)*((mm-H8)/40)^4)^(1/7);

syms nn;
ff2=((nn-H5)/40)/(abs((nn-H5)/40))*4.7*0.003*((9.81^4)*(10^6)*0.003^(5)*((nn-H5)/40)^4)^(1/7)+((nn-20)/20)/(abs((nn-20)/20))*4.7*0.003*((9.81^4)*(10^6)*0.003^(5)*((nn-20)/20)^4)^(1/7);


T1=[k,a,f1(a,H8),b,f1(b,H8),m,f1(m,H8)];
T2=[k,a,f2(a,H5),b,f2(b,H5),n,f2(n,H5)];
while abs(T1(k,4)-T1(k,6))>(eps/2) && abs(T2(k,4)-T2(k,6))>(eps/2)
    k=k+1;
    m1=f1(m,H8);
    m2=f1(a,H8);
    n1=f2(n,H5);
    n2=f2(a,H5);
    if isnan(m1)
        m1=double( limit(ff1,mm,m));
    end
    if isnan(m2)
        m2=double( limit(ff1,mm,a));
    end
    if  m1*m2==0
        T1=[T1;k,a,f1(a,H8),b,f1(b,H8),m,f1(m,H8)];
        break
    elseif  m1*m2>0
        a=m;
        b=b;
        m=(a+b)/2;
        T1=[T1;k,a,f1(a,H8),b,f1(b,H8),m,f1(m,H8)];
    elseif  m1*m2<0
        a=a;
        b=m;
        m=(a+b)/2;
        T1=[T1;k,a,f1(a,H8),b,f1(b,H8),m,f1(m,H8)];
    end
    if isnan(n1)
        n1=double( limit(ff2,nn,n));
    end
    if isnan(n2)
        n2=double( limit(ff2,nn,a));
    end
    if  n1*n2==0
        Tn=[Tn;k,a,f2(a,H5),b,f2(b,H5),n,f2(n,H5)];
        break
    elseif  n1*n2>0
        a=n;
        b=b;
        n=(a+b)/2;
        T2=[T2;k,a,f2(a,H5),b,f2(b,H5),n,f2(n,H5)];
    elseif  n1*n2<0
        a=a;
        b=n;
        n=(a+b)/2;
        T2=[T2;k,a,f2(a,H5),b,f2(b,H5),n,f2(n,H5)];
    end
    H8=n;
    H5=m;
end
disp(m)
disp(n)

