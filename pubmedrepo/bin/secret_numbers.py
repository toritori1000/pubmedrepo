import pubmed.learn.secret_file as secret_file


file_path = 'numbers.txt'
secret_file.write(file_path)
secret_numbers = secret_file.read(file_path)

for num in secret_numbers:
    print(num)
