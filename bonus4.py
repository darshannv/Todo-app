filenames = ['1.raw Data.txt', '2.Reports.txt', '3.Presentations.txt']

for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)