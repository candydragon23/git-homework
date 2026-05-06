import ast, sys, re
from pathlib import Path
from collections import defaultdict

def get_external_imports(py_file, local_pkgs):
    with open(py_file) as f:
        tree = ast.parse(f.read())
    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                top = alias.name.split('.')[0]
                imports.add(top)
        elif isinstance(node, ast.ImportFrom) and node.module:
            top = node.module.split('.')[0]
            imports.add(top)
    stdlib = set(sys.builtin_module_names)
    try:
        from sys import stdlib_module_names
        stdlib.update(stdlib_module_names)
    except: pass
    return {i for i in imports if i not in stdlib and i not in local_pkgs}

def main():
    root = Path.cwd()
    req_file = root / 'requirements.txt'
    local = {str(p.parent.relative_to(root)).replace('/', '.')
             for p in root.rglob('__init__.py') if p.parent != root}
    all_imports = set()
    for py in root.rglob('*.py'):
        if '.venv' in py.parts or 'venv' in py.parts: continue
        all_imports.update(get_external_imports(py, local))
    declared = set()
    if req_file.exists():
        for line in req_file.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith(('#','-','git+')):
                pkg = re.split(r'[=<>!\[\]~;]', line)[0].strip()
                if pkg: declared.add(pkg)
    missing = all_imports - declared
    unused = declared - all_imports
    if missing:
        print("Missing dependencies found: ", *sorted(missing), sep='\n  ')
    if unused:
        print("Unused dependencies found: ", *sorted(unused), sep='\n  ')
    if not missing and not unused:
        sys.exit(0)
    sys.exit(1)

if __name__ == '__main__':
    main()