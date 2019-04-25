main()
{
int fact=1,i,n;
printf("enter the value of n");
scanf("%d",&n);
while(n)
{
    fact = fact *  n;
    n--;
}printf("factorial is %d",fact);

}
