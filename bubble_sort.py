unsorted_list = [10, 7, 8, 9, 6, 1, 2, 3, 4, 5, 99, 66, 55, 43, 23, 12, 45, 65]

print(unsorted_list)   # Liste vor dem Sortieren ausgeben

switch = True  # Kontrollvariable: True, solange noch getauscht wird

while switch:
    start = 0
    step = 0
    switch = False  # Wird bei einem Tausch wieder auf True gesetzt

    while start <= len(unsorted_list) - 2:  # Vergleich benachbarter Elemente
        step = start + 1

        if unsorted_list[start] > unsorted_list[step]:
            # Elemente tauschen
            temp = unsorted_list[start]
            unsorted_list[start] = unsorted_list[step]
            unsorted_list[step] = temp
            switch = True  # Ein Tausch wurde durchgeführt
            start += 1

        elif unsorted_list[start] < unsorted_list[step]:
            start += 1  # Kein Tausch nötig, nächstes Paar prüfen

print(unsorted_list)  # Sortierte Liste ausgeben
