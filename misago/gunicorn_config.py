# gunicorn_config.py

bind = "0.0.0.0:3031"
workers = 4  # 减少进程数（因为每个进程有多个线程）
threads = 25  # 每个 worker 开 4 个线程
worker_class = "gthread"  # 必须指定为 'gthread'

chdir = "/misago"
pythonpath = "/misago"

accesslog = "/misago/logs/gunicorn-access.log"
errorlog = "/misago/logs/gunicorn-error.log"
loglevel = "info"

max_requests = 1000
max_requests_jitter = 100
timeout = 30
