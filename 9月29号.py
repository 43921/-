# #LEGB global nonlocal
# x = 100
#
#
# def func1():
#     global x
#     x = 200
#
#
# func1()
# print(x)
#
#
# def outer():
#     num = 10
#
#     def inner():
#         nonlocal num
#         num = 99
#
#     inner()
#     print(num)
#
#
# outer()
#
# # return多值
# def calc(a, b):
#     add = a + b
#     sub = a - b
#     return add, sub
#
#
# res1, res2 = calc(1, 2)
# print(res1, res2)
#
# # lambda和高阶函数
# nums = [1, 2, 3, 4, 5, 6]
# # filter过滤偶数
# even = list(filter(lambda x: x % 2 == 0, nums))
# print(even)
# square = list(map(lambda x: x ** 2, nums))
# print(square)
# # sorted按字典age排序
# data = [{"name": "a", "age": 20}, {"name": "b", "age": 18}]
# new_data = sorted(data, key=lambda item: item["age"])
# print(new_data)
#
# # 文件操作和编码
##with open读写文本
# with open("text.txt", "w", encoding="utf-8") as f:
#     f.write("你好Python\n")
# with open("text.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())
#
# # 二进制拷贝图片
# with open("a.jpg", "rb") as fr, open("b.jpg", "wb") as fw:
#     content = fr.read()
#     fw.write(content)
# # str bytes编码译码
# s = "中国"
# b = s.encode("utf-8")
# print(b)
# s2 = b.decode("utf-8")
# print(s2)
#
# # 三.常用模块
# # json序列化
# import json
#
# info = {"name": "小明", "age": 18}
# json_str = json.dumps(info, ensure_ascii=False)
# print(json_str)
# data = json.loads(json_str)
# print(data["name"])
# # datetime时间处理
# from datetime import datetime, timedelta
#
# now = datetime.now()
# print(now)
#
# # 时间加3天
# later = now + timedelta(days=3)
# print(later.strftime("%Y-%m-%d %H:%M:%S"))
# import os
#
# base = "/home/project"
# full_path = os.path.join(base, "data.txt")
# print(full_path)
# print(os.path.exists(full_path))

## 四.模块与包
## __name__直接运行值为‘__main__’ __name__被导入时值为所在文件名
## ①一个文件demo1.py
## def hello():
##     print("hello")
##
##
## if __name__ == "__main__":  # 区分不同执行方式
##     print("直接运行才会打印")
##     hello()
## ②一个文件main.py
## import demo1
##
## demo1.hello()
# # 五.面向对象
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def bark(self):
#         print(f"{self.name}汪汪叫")
#
#
# d = Dog("旺财", 2)
# d.bark()
# print(d.name)
#
# # 类方法 @classmethod  静态方法@staticthod
# class Tool:
#     count = 0
#
#     def __init__(self):
#         Tool.count += 1
#
#     @classmethod
#     def show_count(cls):
#         print(f"实例总数：{cls.count}")
#
#     @staticmethod
#     def tips():
#         print("工具类提示")
#
#
# t1 = Tool()
# Tool.show_count()
# Tool.tips()
# 继承super
# class Animal:
#     def eat(self):
#         print("动物吃东西")
#
#
# class Cat(Animal):
#     def eat(self):
#         super().eat()
#         print("猫吃鱼")
#
#
# c = Cat()
# c.eat()
#
# # 封装
# class Student:
#     def __init__(self, score):
#         self.__score = score
#
#     @property
#     def score(self):
#         return self.__score
#
#     @score.setter
#     def score(self, val):
#         if 0 <= val <= 100:
#             self.__score = val
#         else:
#             raise ValueError("分数0~100")
#
#
# s = Student(80)
# print(s.score)
# s.score = 95
# print(s.score)
#
# # try except 异常捕获
# try:
#     num = int(input("输入数字："))
#     res = 10 / num
# except ValueError:
#     print("请输入合法数字")
# except ZeroDivisionError:
#     print("不能除以0")
# else:
#     print("结果", res)
# finally:
#     print("程序结束")
#
# # 网络编程 Socket TCP
# # TCP 服务端 server.py
# import socket
#
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(("127.0.0.1", 8899))
# server.listen(5)
# print("服务端启动，等待连接...")
#
# conn, addr = server.accept()  # 阻塞
# print("客户端地址", addr)
#
# data = conn.recv(1024).decode("utf-8")
# print("收到：", data)
# conn.send(data.upper().encode("utf-8"))
#
# conn.close()
# server.close()
# # TCP 客户端 client.py
# import socket
#
# client = socket.socket()
# client.connect(("127.0.0.1", 8899))
#
# msg = "hello socket"
# client.send(msg.encode("utf-8"))
#
# resp = client.recv(1024).decode("utf-8")
# print("服务端返回：", resp)
# client.close()
# # struct 解决粘包
# import struct
#
#
# data = "消息内容".encode("utf-8")
# # 打包长度为4字节
# pack_len = struct.pack("i", len(data))
#
# # --------发送端--------
# # sock.send(pack_len)
# # sock.send(data)
#
# # --------接收端--------
# # head = sock.recv(4)
# # real_len = struct.unpack("i", head)[0]
# # real_data = sock.recv(real_len)

# 并发编程
# threading 多线程
# import threading
# import time
#
# def work(name,delay):
#     print(f"{name} 开始")
#     time.sleep(delay)
#     print(f"{name} 结束")
#
# t1 = threading.Thread(target=work, args=("线程A",1))
# t2 = threading.Thread(target=work, args=("线程B",2))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
# print("全部完成")
# 线程池 ThreadPoolExecutor
# from concurrent.futures import ThreadPoolExecutor
# import time
#
# def task(n):
#     time.sleep(1)
#     return n*n
#
# with ThreadPoolExecutor(max_workers=3) as pool:
#     futures = [pool.submit(task,i) for i in range(5)]
#     result = [f.result() for f in futures]
#
# print(result)
# # 互斥锁lock
# import threading
#
# count = 0
# lock = threading.Lock()
#
#
# def add():
#     global count
#     for _ in range(100000):
#         lock.acquire()
#         try:
#             count += 1
#         finally:
#             lock.release()
#
#
# t1 = threading.Thread(target=add)
# t2 = threading.Thread(target=add)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(count)
#
# # asyncio 协程
# import asyncio
#
#
# async def demo(num):
#     print(f"任务{num}开始")
#     await asyncio.sleep(2)
#     return num * 10
#
#
# async def main():
#     t1 = asyncio.create_task(demo(1))
#     t2 = asyncio.create_task(demo(2))
#     res = await asyncio.gather(t1, t2)
#     print(res)
#
#
# asyncio.run(main())
