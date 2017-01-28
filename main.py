import socket
import time
import uuid
import datetime

if __name__ == '__main__':
    main_domain = "test.catofes.com"
    while True:
        time.sleep(0.5)
        prefix = str(uuid.uuid4())
        domain = "%s.%s" % (prefix, main_domain)
        try:
            data = []
            results = socket.getaddrinfo(domain, None)
            for result in results:
                data.append(result[4][0])
            print("[%s]: Test: %s Result: %s" % (datetime.datetime.now(), domain, ' '.join(data)))
        except:
            print("[%s]: Test: %s Result: Failed" % (datetime.datetime.now(), domain))
