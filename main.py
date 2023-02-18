import base64, lzma
filename = input("Obf file name : ")
obf_data = open(filename).read()
obf_content = obf_data.split("\n")[-1]
base64_data = obf_content.split("''';'''")[-3].split("'''")[2].split("'")[1]
lzma_data = base64.urlsafe_b64decode(base64_data)
real_content = lzma.decompress(lzma_data).decode('utf-8')
print("Deobfuscated code : \n" + real_content)
open(filename + ".deobf","w").write(real_content)
print("\n\n\nSaved at : " + filename + ".deobf")