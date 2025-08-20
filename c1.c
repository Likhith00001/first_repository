#include<stdio.h>

void main()
{
	int a;
	int b;
	scanf("input%d",&a);
	scanf("input%d",&b);
	if a>b:
		add();
	elseif b>a:
		sub();
	elseif a==b:
		mul();
	else:
		printf("error");
		return 0;
}

int add(a,b)
{
	c=a+b;
	printf("add of %d",c);
	return c;
}