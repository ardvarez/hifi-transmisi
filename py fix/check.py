import glob
files = glob.glob(r'c:\KERJAAN\Project\hifi-ers\hifi-ers\Mutasi\*.html')
for f in files:
    content = open(f, encoding='utf-8').read()
    count = content.count("<style")
    print(f"{f.split('\\')[-1]}: {count}")
