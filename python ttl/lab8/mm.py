def workingWeeks(projC):
    
    if not projC:
        return 0
    projC.sort(reverse=True)
    max_modules = projC[0]
    total_modules = sum(projC) - max_modules
    if max_modules <= total_modules:
        return total_modules + max_modules
    else:
        return 2 * total_modules + 1

def main():
    # Input for projC
    projC = []
    projC_size = int(input())
    projC = list(map(int, input().split()))
    
    result = workingWeeks(projC)
    print(result)

if _name_ == "_main_":
    main()