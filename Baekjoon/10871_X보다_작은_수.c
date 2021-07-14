#include <stdio.h>

int main()
{
    int n,x,answer;
    
    scanf("%d %d",&n,&x);
    
    for(int i=0; i<n; i++)
    {
        scanf("%d ",&answer);
        
        if(answer<x)
        {
            printf("%d ",answer);
        }
        
        
    }

    return 0;
}
