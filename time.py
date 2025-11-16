x = float(input("Enter minutes: "))
seconds = x*60
hours = int(seconds//3600)
minutes = int((seconds%3600)//60)
seconds = int(seconds%60)

print(f"{hours}:{minutes}:{seconds}")