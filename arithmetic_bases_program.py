print('\nThis program converts a number from one arithmetic system with base 2 to 16 to another with base 2 to 16.')
while True:
    print('\n')
    n1=str(input('Give a number: '))
    r=int(input('Select the arithmetic system to which the above number belongs: '))
    q=int(input('Select the arithmetic system to which you want to convert the number: '))
    y=0
    abc='ABCDEF'
    abc123=list(range(10,16))
    s1=0
    if r<2 or r>16 or q<2 or q>16:
        print('\nThe bases must be 2 to 16 strictly. Try again.')
    else:
        for i in range(len(n1)-1,-1,-1):
            if r>10 and n1[i].isalpha():
                x=abc.find(n1[i])
                a=int(abc123[x])*r**(len(n1)-1-i)
                if n1[i]>abc[r-11]:
                    y=1
                    break
            elif r<=10 and n1[i].isalpha():
                y=1
                break
            else:
                a=int(n1[i])*r**(len(n1)-1-i)
                if int(n1[i])>=r:
                    y=1
                    break
            s1=s1+a
        b=1
        s2=''
        c=s1
        if y==0:
            while b!=0 or c!=0:
                b=c%q
                c=c//q
                if b>=10:
                    b=abc[b%10]
                s2=str(b)+s2
            if s2[0]=='0':
                n2=s2[1:]
            else:
                n2=s2
            print('\nThe number',n1,'(',r,')','is the number',n2,'(',q,').')
        else:
            print("\nThe number",n1,"doesn't belong to this arithmetic system",'(',r,'). Try again.')