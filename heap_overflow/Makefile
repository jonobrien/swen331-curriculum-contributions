build: 
	gcc -fno-stack-protector -g -o heapfixed heapfixed.c
	gcc -fno-stack-protector -g -o heap heap.c
unsafe:
	./heap `python heap.py`
safe:
	./heapfixed `python heap.py`
