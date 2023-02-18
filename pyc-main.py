import dis, marshal
pyc_path = input("PYC filename : ")
with open(pyc_path, 'rb') as f:
    pyc_header = f.read(16)
    code_obj = marshal.load(f)
it = dis.get_instructions(code_obj)

a = ""

for i in it:
    if i.opcode == 100 and i.arg == 10:
        a = i.argval
        break

exec(';'.join(a.split(";")[:-1]))
print("Deobfuscated code : \n" + code)
open(pyc_path + ".deobf","w").write(code)
print("\n\n\nSaved at : " + pyc_path + ".deobf")