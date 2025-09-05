string="python"
try:
    print(string[3])
except IndexError as error:
    print(error)

else:
    print("original string: ",string)

print("string program completed")           