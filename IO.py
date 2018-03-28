import re


def reddy_ncs(file_path):
    ncs = []
    scores = []
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
        for l in lines:
            # res = re.search('(\w+)-\w+\s(\w+)-\w+\s', l)
            res = re.match('(\w+)-\w+\s(\w+)-\w+\t([\s0-9.]+)$', l)
            if res:
                nc = res.group(1) + ' ' + res.group(2)
                ncs.append(nc)
                scores.append(float(res.group(3).split(" ")[4]))
    return ncs, scores