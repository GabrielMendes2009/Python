segs = int(input ("Insira os segundos desejados: "))

horas = segs // 3600

minutos = horas % 3600

total_seg = segs % 60

print(horas, "hora(s),", minutos, "minuto(s) e", total_seg, "segundo(s).")