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
    # ���IP��
    start_ip = args.ip.split('-')[0]
    end_ip = args.ip.split('-')[1]

    # ��������
    if args.n <=0:
        raise RuntimeError("args.n", "�������������0! ") 
    concurrent = args.n

    # ɨ������
    task_type = args.f
    
    # �Ƿ񱣴���
    save_file = args.w
    
    # �Ƿ��ӡ��ʱ��Ϣ
    verbose = args.v
    
    # ��ʼ������
    tasks =[]
    results = []
    start_time = time.time()

    # ��ʼ���̳߳�
    with ThreadPoolExecutor(max_workers=concurrent) as executor:
        start_ip = ipaddress.IPv4Address(start_ip)
        end_ip = ipaddress.IPv4Address(end_ip)
        if start_ip > end_ip:
            raise RuntimeError("��ʼIP����С�ڽ���IP! ")

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
        
        # ��ӡ���к�ʱ
        if verbose:
            end_time = time.time()
            print("�����ʱ(��)��",end_time-start_time)

        # ������
        if not save_file is None:
            with open(save_file,'w') as f:
                json.dump(results,f)

        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='����˵��:')
    parser.add_argument('-n', type=int, default=20, help='ָ����������')
    parser.add_argument('-f', type=str, choices=['ping','tcp'], required=True, help='[ping]����ping����;[tcp]���ж˿ڲ���')
    parser.add_argument('-ip', type=str, required=True, help='���� IP ��ַ֧�� 192.168.0.1-192.168.0.100 д��')
    parser.add_argument('-w', type=str, default=None, help='����ɨ����')
    parser.add_argument('-v', action='store_true', help='��ӡ���к�ʱ')
    args = parser.parse_args()

    exec_task(args)