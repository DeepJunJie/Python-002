import argparse
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import ipaddress
import json
import os 

def scan_ping(target_ip):
    response = os.system('ping -c 1 -w 1' +' '+ target_ip +" > nul 2>&1")
    if response == 0:
        return (target_ip,"alive")


def scan_tcp(target_ip, target_port):
    s = socket.socket()
    s.settimeout(0.1)
    
    if s.connect_ex((target_ip, target_port)) == 0:
        record = [target_ip, target_port, 'open']
    else:
        record = [target_ip, target_port, 'close']
    s.close()
    return record

    
def exec_task(args):
    # 检查IP段
    start_ip = args.ip.split('-')[0]
    end_ip = args.ip.split('-')[1]

    # 并发数量
    if args.n <=0:
        raise RuntimeError("args.n", "并发数必须大于0! ") 
    concurrent = args.n

    # 扫描类型
    task_type = args.f
    
    # 是否保存结果
    save_file = args.w
    
    # 是否打印耗时信息
    verbose = args.v
    
    # 初始化变量
    tasks =[]
    results = []
    start_time = time.time()

    # 初始化线程池
    with ThreadPoolExecutor(max_workers=concurrent) as executor:
        start_ip = ipaddress.IPv4Address(start_ip)
        end_ip = ipaddress.IPv4Address(end_ip)
        if start_ip > end_ip:
            raise RuntimeError("起始IP必须小于结束IP! ")

        if task_type == 'tcp':
            for int_ip in range(int(start_ip), int(end_ip)+1 ):
                str_ip=str(ipaddress.IPv4Address(int_ip))
                for port in range(1,1024):
                   tasks.append(executor.submit(scan_tcp, str_ip, port ))    
        elif task_type == 'ping':
            for int_ip in range(int(start_ip),int(end_ip)+1):
                str_ip=str(ipaddress.IPv4Address(int_ip))
                tasks.append(executor.submit(scan_ping, str_ip))

        for future in as_completed(tasks):
            if not future.result() is None:
                if task_type == 'tcp':
                    if future.result()[2] == 'open':
                        print(future.result())
                        results.append(future.result())
                elif task_type == 'ping':
                    print(future.result())
                    results.append(future.result())
        
        # 打印运行耗时
        if verbose:
            end_time = time.time()
            print("任务耗时(秒)：",end_time-start_time)

        # 保存结果
        if not save_file is None:
            with open(save_file,'w') as f:
                json.dump(results,f)

        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='参数说明:')
    parser.add_argument('-n', type=int, default=20, help='指定并发数量')
    parser.add_argument('-f', type=str, choices=['ping','tcp'], required=True, help='[ping]进行ping测试;[tcp]进行端口测试')
    parser.add_argument('-ip', type=str, required=True, help='连续 IP 地址支持 192.168.0.1-192.168.0.100 写法')
    parser.add_argument('-w', type=str, default=None, help='保存扫描结果')
    parser.add_argument('-v', action='store_true', help='打印运行耗时')
    args = parser.parse_args()

    exec_task(args)