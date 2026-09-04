from graphify.extract import collect_files, extract
from pathlib import Path
import time

if __name__ == '__main__':
    core_scripts = collect_files(Path('.agents/scripts'))
    print(f'Core scripts: {len(core_scripts)} files')
    t0 = time.time()
    res = extract(core_scripts)
    nodes = res.get('nodes', [])
    edges = res.get('edges', [])
    print(f'Extracted {len(nodes)} nodes, {len(edges)} edges in {time.time()-t0:.2f}s')
