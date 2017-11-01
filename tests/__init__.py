import sys, os

pack_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../src')
pack_path = os.path.abspath(pack_path)
print pack_path
sys.path.insert(0, pack_path)
