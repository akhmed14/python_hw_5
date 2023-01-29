stt = 'gfhw jhgfj gdfgs gdygyg ugdrsjw '.split()
print(stt)
stt = list(filter(lambda x: not 'gd' in x.lower(), stt))
print(stt)