def main():
fhandle=open("samplefile.md","w+")
fhandle.write("123456")
print(fhandle.read())
