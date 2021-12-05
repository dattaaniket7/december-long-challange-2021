t=int(input())
for i in range(t):
    companies = list(map(str, input().split()))
    offer = list(map(str, input().split()))
    
    for i in range (len(companies)):
        if companies[i] == offer[0] or companies[i] == offer[1]:
            print(companies[i])
            break