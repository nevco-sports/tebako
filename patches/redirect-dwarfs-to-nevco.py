#!/usr/bin/env python3
"""
Patch tamatebako/libdwarfs CMakeLists.txt to use nevco-sports/dwarfs instead
of tamatebako/dwarfs. The nevco-sports fork includes a fix for mkdwarfs
crashing on Windows with GCC 16 when symlink_status returns not_found.

This script runs in the libdwarfs source directory as a PATCH_COMMAND for
the _dwarfs_wr ExternalProject in tebako's CMakeLists.txt.

See: https://github.com/mhx/dwarfs/commit/51bd06e (adapted for v0.7.x)
"""
import sys

cmake_file = 'CMakeLists.txt'
with open(cmake_file) as f:
    content = f.read()

changes = [
    (
        'https://github.com/tamatebako/dwarfs.git',
        'https://github.com/nevco-sports/dwarfs.git',
    ),
    (
        'def_ext_prj_g(DWARFS "tebako-v0.9.0")',
        'def_ext_prj_g(DWARFS "tebako-v0.9.0-gcc16")',
    ),
]

for old, new in changes:
    if old not in content:
        print(f'WARNING: expected pattern not found: {old!r}', file=sys.stderr)
        sys.exit(1)
    content = content.replace(old, new, 1)

with open(cmake_file, 'w') as f:
    f.write(content)

print('Redirected _dwarfs -> nevco-sports/dwarfs @ tebako-v0.9.0-gcc16')