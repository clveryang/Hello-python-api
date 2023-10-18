import subprocess

'''
this example shows how to start a process through subprocess and keep the execution log
'''

if __name__ == '__main__':
    cmd="ls"
    with open('test.txt', 'w', encoding='utf-8') as file_handler:
        # file_handler.write(f"{cmd}")
        process_res = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        for line in iter(process_res.stdout.readline, b''):
            line = line.decode('utf-8')
            print(line, end='')  # 输出到屏幕
            file_handler.write(line)  # 追加到文件

        process_res.wait()
        return_code = process_res.returncode
 



