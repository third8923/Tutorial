import requests
import time

# 定义要监测的地址列表
urls = [
    "cr.laoyou.ip-ddns.com",
    "docker.1panel.live",
    "image.cloudlayer.icu",
    "hub.fast360.xyz",
    "docker-0.unsee.tech",
    "docker.1panelproxy.com",
    "docker.tbedu.top",
    "dockerpull.cn",
    "docker.m.daocloud.io",
    "hub.rat.dev",
    "docker.kejilion.pro",
    "docker.hlmirror.com",
    "docker.imgdb.de",
    "docker.melike.me.cn",
    "ccr.ccs.tencentyun.com",
    "pull.loridocker.com"
]

for url in urls:
    try:
        start_time = time.time()
        response = requests.head(f"http://{url}", timeout=5)
        end_time = time.time()
        latency = (end_time - start_time) * 1000  # 转换为毫秒
        print(f"{url} 连通性：正常，延时：{latency:.2f} 毫秒")
    except requests.RequestException as e:
        print(f"{url} 连通性：异常，原因：{str(e)}")