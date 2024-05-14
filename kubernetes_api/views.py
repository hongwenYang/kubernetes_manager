from django.http import JsonResponse
from kubernetes import client, config


def list_pods(request):
    # 加载Kubernetes配置文件
    config.load_kube_config('H:\juchuang\wjconfig')

    # 创建Kubernetes API客户端
    v1 = client.CoreV1Api()

    # 获取所有Pods
    pods = v1.list_pod_for_all_namespaces(watch=False)

    # 提取Pod信息并返回JSON响应
    pod_list = []
    for pod in pods.items:
        pod_list.append({
            "name": pod.metadata.name,
            "namespace": pod.metadata.namespace,
            "status": pod.status.phase
        })

    return JsonResponse({"pods": pod_list})
