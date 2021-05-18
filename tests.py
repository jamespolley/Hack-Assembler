import filecmp

file_path = './assets/'
files_to_compare = [
    'Add', 'Max', 'MaxL', 'Pong', 'PongL', 'Rect', 'RectL']

test = 1
for file in files_to_compare:
    file_assembled = file_path + file + '.hack'
    file_expected = file_path + file + '_Expected.hack'
    test_passed = filecmp.cmp(file_assembled, file_expected)
    if test_passed:
        print('Test {0} passed!'.format(str(test)))
        
        print(file + '.asm successfully assembled into ' + file + '.hack.\n')
    else:
        print('Test {0} failed!'.format(str(test)))
        print('{0} did not match {1}.\n'.format(file_assembled, file_expected))
    test += 1
