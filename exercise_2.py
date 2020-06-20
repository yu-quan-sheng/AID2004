

from multiprocessing import Pool,Queue
import os

q = Queue() # 创建消息队列

# 进程池函数 --> 拷贝一个文件
def copy(old_folder,new_folder,file):
    """
    :param old_folder: 从哪拷贝
    :param new_folder: 拷贝到哪
    :param file: 拷贝什么文件
    """
    fr = open(old_folder+'/'+file,'rb')
    fw = open(new_folder+'/'+file,'wb')
    while True:
        data = fr.read(1024)
        if not data:
            break
        n = fw.write(data)
        q.put(n) #  已经拷贝的字节数
    fr.close()
    fw.close()

# 获取文件夹大小
def get_size(dir):
    total_size = 0
    for file in os.listdir(dir):
        total_size += os.path.getsize(dir+'/'+file)
    return total_size

def main():
    old_folder = input("要拷贝的目录:")
    new_folder = old_folder + "-备份"
    os.mkdir(new_folder)
    total_size = get_size(old_folder) # 获取目录大小

    #　创建进程池
    pool = Pool(4)

    # 向进程池事件队列中加入事件
    for file in os.listdir(old_folder):
        pool.apply_async(func=copy,args=(old_folder,new_folder,file))

    copy_size = 0
    while copy_size < total_size:
        copy_size += q.get() # 从消息队列中实时获取已经拷贝的字节数
        print("拷贝了%.2f%%"%(copy_size/total_size*100))

    pool.close()
    pool.join()

main()