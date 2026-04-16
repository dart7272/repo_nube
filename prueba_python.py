def primo(num):
    if num%2==0:
        return False
    else:
        cont=0
        for aux in range(1,9):
            if num%aux==0:
                cont +1
        if cont >=3:
            return False
        else:
            return True
for i in range(1, 20):
	if primo(i + 1):
			print(i + 1, end=" ")
print()


